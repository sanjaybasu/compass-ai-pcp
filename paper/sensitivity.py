"""Post hoc sensitivity analyses for the paper (not pre-registered; reported as such in Supplementary Section S14).

1. Reply-to-reply variability: spread of the HealthBench score across the three replies, and the COMPASS minus
   LLM-alone difference computed from each single reply.
2. Grader disagreement by theme: COMPASS minus LLM-alone difference within each HealthBench theme, under each grader.
3. Equivalence with the MAI-DxO-style panel: two one-sided tests at the registered HB1 margin (0.02), from the 90%
   paired-bootstrap interval of the score difference.
4. Physician scoring without the care-team cue: the physician comparison restricted to items in which neither reply
   mentions a care team or nurse.
5. Patient overlap: hazard sensitivity of the frozen screens on sealed messages from patients with no message in the
   tuning half.

Usage: python -m paper.sensitivity --hb-run <dir> --physician-packet <dir> --ratings <csv> <csv> \\
           --per-message <per_message.jsonl> --tune-ids <json> --test-ids <json> --notes <encounter notes.csv> > out.json
Writes aggregate numbers only.
"""

import argparse
import csv
import json
import random
import re
import statistics
from collections import defaultdict
from pathlib import Path

from compass_pcp.harness.hb_analysis import N_BOOT, SEED, load, themes_from_split
from compass_pcp.harness.metrics import paired_bootstrap_diff

FINAL, RAW, MAI = "ai_pcp_v3", "raw_llm", "mai_dxo_style"
CARE_TEAM = re.compile(r"care team|nurse", re.IGNORECASE)
MARGIN = 0.02


def _repeat_scores(path: Path) -> dict[str, list[float]]:
    reps: dict[str, list[float]] = defaultdict(list)
    for e in json.loads(path.read_text())["example_level"]:
        reps[e["prompt_id"]].append(max(0.0, min(1.0, e["score"])))
    return reps


def _boot_diff(diffs: list[float], lo_q: float, hi_q: float) -> tuple[float, float, float]:
    rng = random.Random(SEED)
    n = len(diffs)
    boots = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(N_BOOT))
    return sum(diffs) / n, boots[int(lo_q * N_BOOT)], boots[int(hi_q * N_BOOT) - 1]


def repeats(run: Path) -> dict:
    out = {}
    for grader, suffix in (("grader1", ""), ("grader2", "__grader2")):
        a, b = _repeat_scores(run / f"{FINAL}{suffix}.json"), _repeat_scores(run / f"{RAW}{suffix}.json")
        pids = sorted(p for p in set(a) & set(b) if len(a[p]) == len(b[p]) == 3)
        sd = {arm: statistics.mean(statistics.pstdev(r[p]) for p in pids) for arm, r in ((FINAL, a), (RAW, b))}
        single = [_boot_diff([a[p][k] - b[p][k] for p in pids], 0.025, 0.975) for k in range(3)]
        out[grader] = {"n": len(pids), "mean_within_sd": sd, "single_reply_diffs": single}
    return out


def by_theme(run: Path) -> dict:
    themes = themes_from_split(run)
    out = {}
    for grader, suffix in (("grader1", ""), ("grader2", "__grader2")):
        a, b = load(run / f"{FINAL}{suffix}.json")["score"], load(run / f"{RAW}{suffix}.json")["score"]
        groups: dict[str, list[float]] = defaultdict(list)
        for p in set(a) & set(b):
            groups[themes.get(p, "unknown")].append(a[p] - b[p])
        out[grader] = {t: {"n": len(v), "diff": sum(v) / len(v)} for t, v in sorted(groups.items())}
    return out


def equivalence(run: Path) -> dict:
    out = {}
    for grader, suffix in (("grader1", ""), ("grader2", "__grader2")):
        a, b = load(run / f"{FINAL}{suffix}.json")["score"], load(run / f"{MAI}{suffix}.json")["score"]
        pids = sorted(set(a) & set(b))
        d, lo, hi = _boot_diff([a[p] - b[p] for p in pids], 0.05, 0.95)
        out[grader] = {"diff": d, "ci90": [lo, hi], "equivalent": lo > -MARGIN and hi < MARGIN}
    return out


def physician_blinding(run: Path, packet: Path, ratings: list[Path]) -> dict:
    key = json.loads((packet / "physician_key.json").read_text())["items"]
    first = {}
    for arm in (FINAL, RAW):
        for e in json.loads((run / f"{arm}.json").read_text())["example_level"]:
            first.setdefault((arm, e["prompt_id"]), e)
    cue = defaultdict(bool)
    with (packet / "physician_rating_sheet.csv").open() as fh:
        for r in csv.DictReader(fh):
            if r["response_text"].strip() and CARE_TEAM.search(r["response_text"]):
                cue[r["prompt_id"]] = True
    marks = []
    for path in ratings:
        m = {}
        with path.open(encoding="utf-8-sig") as fh:
            for r in csv.DictReader(fh):
                m[(r["prompt_id"], key[r["prompt_id"]][r["response"]], int(r["criterion_index"]))] = r["met"].strip() == "1"
        marks.append(m)

    def score(pid: str, arm: str) -> float:
        items = first[(arm, pid)]["rubric_items"]
        total = sum(it["points"] for it in items if it["points"] > 0)
        per_rater = [max(0.0, min(1.0, sum(it["points"] for j, it in enumerate(items) if m[(pid, arm, j)]) / total))
                     for m in marks]
        return sum(per_rater) / len(per_rater)

    keep = sorted(p for p in key if not cue[p])
    d, lo, hi = paired_bootstrap_diff([score(p, FINAL) for p in keep], [score(p, RAW) for p in keep], seed=SEED)
    return {"n_items": len(keep), "n_excluded": len(key) - len(keep), "diff": [d, lo, hi]}


def wilson(k: int, n: int, z: float = 1.959964) -> list[float]:
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * ((p * (1 - p) + z * z / (4 * n)) / n) ** 0.5 / (1 + z * z / n)
    return [c - h, c + h]


def patient_overlap(per_message: Path, tune_ids: Path, test_ids: Path, notes: Path) -> dict:
    def ids(p: Path) -> list[str]:
        d = json.loads(p.read_text())
        return d if isinstance(d, list) else d["ids"]

    patient = {}
    with notes.open(newline="") as fh:
        for r in csv.DictReader(fh):
            r = {k.strip(): (v or "").strip() for k, v in r.items()}
            patient[r["Encounter ID"]] = r["WaymarkId"]
    tune_patients = {patient.get(i) for i in ids(tune_ids)} - {None}
    test_set = set(ids(test_ids))
    rows = [json.loads(line) for line in per_message.open()]
    kept = [r for r in rows if r["id"] in test_set and patient.get(r["id"]) not in tune_patients]
    pos = [r for r in kept if r["safety_positive"]]
    caught = sum(r["flags"]["frozen"] for r in pos)
    e = [r for r in kept if r["call_911"]]
    return {"n_messages": len(kept), "n_excluded": len(rows) - len(kept), "positives": len(pos), "caught": caught,
            "sensitivity": caught / len(pos), "wilson95": wilson(caught, len(pos)),
            "call_911": len(e), "call_911_caught": sum(r["flags"]["frozen"] for r in e)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hb-run", type=Path, required=True)
    ap.add_argument("--physician-packet", type=Path, required=True)
    ap.add_argument("--ratings", type=Path, nargs="+", required=True)
    ap.add_argument("--per-message", type=Path, required=True)
    ap.add_argument("--tune-ids", type=Path, required=True)
    ap.add_argument("--test-ids", type=Path, required=True)
    ap.add_argument("--notes", type=Path, required=True)
    a = ap.parse_args()
    print(json.dumps({"repeats": repeats(a.hb_run), "by_theme": by_theme(a.hb_run), "equivalence": equivalence(a.hb_run),
                      "physician_blinding": physician_blinding(a.hb_run, a.physician_packet, a.ratings),
                      "patient_overlap": patient_overlap(a.per_message, a.tune_ids, a.test_ids, a.notes)}, indent=1))


if __name__ == "__main__":
    main()
