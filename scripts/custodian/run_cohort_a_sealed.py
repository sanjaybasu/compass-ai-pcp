"""Score the sealed Cohort A half once, with the frozen hazard screens (custodian only; VVP-PCP-001 Sections 8.5, 13.2).

Usage (custodian): python -m scripts.custodian.run_cohort_a_sealed --freeze docs/regulatory/freeze/cohort_a/freeze.json \\
    --cases <custodian copy of the 2,000-message file> --test-ids <custodian copy of cohort_a_test_ids.json> \\
    --out <custodian-only directory> --access-log <custodian-only directory>/access_log.jsonl

Optional: --floor-results <cohort_a_floor_per_message.jsonl> adds the deterministic floors as comparators.
Refuses to run unless the freeze verifies against this checkout. Patient text goes only to the local Kev judge and to
the Anthropic screen (BAA). Resumable: each screen result is cached in --out, so rerun the same command after an
interruption. Writes per-message results and the VE-A4/VE-A5 report to --out; nothing is written inside the repository.
"""

import argparse
import concurrent.futures as cf
import getpass
import json
from datetime import UTC, datetime
from pathlib import Path

from compass_pcp.arms.hazard import KEV_INSTRUCTIONS, KEV_TIERS, kev_tier, patient_text, screen
from compass_pcp.arms.llm import KevJudge
from compass_pcp.harness import frozen
from compass_pcp.harness.cache import ResponseCache
from compass_pcp.harness.cohort_a import analyze, flags, label
from compass_pcp.harness.episode import hash_ids
from scripts.run_healthbench import make_llm


def log_access(path: Path, action: str, ids_sha: str) -> None:
    rec = {"utc": datetime.now(UTC).isoformat(), "user": getpass.getuser(), "action": action, "test_ids_sha256": ids_sha}
    with path.open("a") as fh:
        fh.write(json.dumps(rec) + "\n")


def message_fields(c: dict) -> tuple[str, str]:
    return c.get("message_id") or c.get("case_id") or c.get("name"), c.get("message") or c.get("prompt") or ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--freeze", type=Path, required=True)
    ap.add_argument("--cases", type=Path, required=True)
    ap.add_argument("--test-ids", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--access-log", type=Path, required=True)
    ap.add_argument("--floor-results", type=Path, default=None)
    ap.add_argument("--threads", type=int, default=4)
    args = ap.parse_args()
    if frozen.REPO in args.out.resolve().parents or frozen.REPO in args.access_log.resolve().parents:
        raise SystemExit("--out and --access-log must be outside the repository")
    test_ids = json.loads(args.test_ids.read_text())
    ids_sha = hash_ids(test_ids)["set_sha256"]
    args.out.mkdir(parents=True, exist_ok=True)
    log_access(args.access_log, "verify_freeze", ids_sha)
    frozen.verify_current(args.freeze, test_ids)  # raises before any message is read
    keep = set(test_ids)
    cases = [c for c in json.loads(args.cases.read_text()) if message_fields(c)[0] in keep]
    if len(cases) != len(keep):
        raise SystemExit(f"{len(keep) - len(cases)} sealed ids are missing from --cases")
    log_access(args.access_log, "score_start", ids_sha)

    judge, llm = KevJudge(), make_llm(frozen.HAZARD_LLM)
    kev_cache, llm_cache = ResponseCache(args.out / "cache_kev.jsonl"), ResponseCache(args.out / "cache_llm.jsonl")

    floors = {}
    if args.floor_results:
        floors = {r["message_id"]: r for r in map(json.loads, args.floor_results.read_text().splitlines()) if r["message_id"] in keep}

    def one(c: dict) -> dict:
        cid, msg = message_fields(c)
        msgs = [{"role": "user", "content": msg}]
        probs = kev_cache.get_or_call({"id": cid}, lambda: judge.choice(patient_text(msgs), KEV_INSTRUCTIONS, KEV_TIERS))
        k = int(kev_tier(probs))
        m = llm_cache.get_or_call({"id": cid}, lambda: int(screen(llm, msgs, 1).tier))
        urgent = sum(probs.get(t, 0.0) for t in ("urgent_same_day", "possible_emergency", "emergency_now"))
        return {"id": cid, "kev_tier": k, "llm_tier": m, "kev_urgent": urgent,
                "flags": flags(k, m, floors.get(cid) if args.floor_results else None), **label(c)}

    with cf.ThreadPoolExecutor(args.threads) as ex:
        rows = list(ex.map(one, cases))
    (args.out / "per_message.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    report = {"scored_utc": datetime.now(UTC).isoformat(), "freeze": str(args.freeze), **analyze(rows)}
    (args.out / "cohort_a_sealed_report.json").write_text(json.dumps(report, indent=2))
    log_access(args.access_log, "score_complete", ids_sha)
    print(json.dumps({k: report[k] for k in ('n', 'VE_A4', 'VE_A5')}, indent=2))


if __name__ == "__main__":
    main()
