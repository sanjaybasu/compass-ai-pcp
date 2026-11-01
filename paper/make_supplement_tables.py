"""Supplement tables generated from the signed clinical content (scripts and rules), so the appendix cannot drift.

Usage: python -m paper.make_supplement_tables --manuscript-dir <notebooks/compass-ai-pcp/manuscript>
"""

import argparse
from collections import Counter
from pathlib import Path

import yaml

from compass_pcp.engine.scripts import load_script
from compass_pcp.harness.frozen import DATA_DIR


def scripts_table() -> str:
    rows = ["| Complaint | Lane | Diagnoses | Must-not-miss diagnoses | Questions | Likelihood ratios | Red-flag questions |",
            "| :-- | :-- | :-- | :-- | :-- | :-- | :-- |"]
    for p in sorted((DATA_DIR / "scripts").glob("*.yaml")):
        if p.stem == "TEMPLATE":
            continue
        s = load_script(p)
        cm = ", ".join(d.label for d in s.diagnoses if d.cannot_miss)
        rows.append(f"| {s.complaint.replace('_', ' ')} | {s.lane.replace('_', ' ')} | {len(s.diagnoses)} | {cm} | "
                    f"{len(s.features)} | {sum(len(d.lrs) for d in s.diagnoses)} | {len(s.must_ask)} |")
    return "\n".join(rows) + "\n"


def rules_table() -> str:
    rows = ["| Rule file | Rules | Kinds | Lab recency rules | Physician sign-off | Pharmacist sign-off |",
            "| :-- | :-- | :-- | :-- | :-- | :-- |"]
    for name in ("refill.yaml", "titration.yaml", "contraception.yaml"):
        d = yaml.safe_load((DATA_DIR / "rules" / name).read_text())
        kinds = Counter(r.get("kind", "unspecified") for r in d.get("rules", []))
        rev = d.get("clinical_review", {})
        rows.append(f"| {name} | {len(d.get('rules', []))} | {', '.join(f'{k} {v}' for k, v in sorted(kinds.items()))} | "
                    f"{len(d.get('lab_recency', []))} | {rev.get('physician_approved_on') or 'pending'} | "
                    f"{rev.get('pharmacist_approved_on') or 'pending'} |")
    return "\n".join(rows) + "\n"


def prompts_appendix() -> str:
    """Every prompt that shapes a reply, copied from the code at build time."""
    from compass_pcp.arms import ai_pcp_v2 as v2
    from compass_pcp.arms import baselines as bl
    from compass_pcp.arms import hazard as hz

    blocks = [("COMPASS: permissions", v2.PERMISSIONS), ("COMPASS: router", v2.ROUTER), ("COMPASS: extractor", v2.EXTRACT),
              *[(f"COMPASS: reply, {k}", t) for k, t in v2.COMPOSE.items()], ("COMPASS: scope check", v2.SCOPE_CHECK),
              ("Hazard screen: LLM", hz.SCREEN), ("Hazard screen: local judge instructions", hz.KEV_INSTRUCTIONS),
              ("Hazard screen: local judge tiers", "\n".join(f"{k}: {v}" for k, v in hz.KEV_TIERS.items())),
              ("Shared output policy", bl.OUTPUT_LIMITS), ("LLM alone: persona", bl.PCP_PERSONA),
              ("Guardrail stack: input screen", bl.GUARD_INPUT), ("Guardrail stack: output review", bl.GUARD_OUTPUT),
              ("AMIE-style: analysis", bl.AMIE_ANALYZE), ("AMIE-style: draft", bl.AMIE_DRAFT), ("AMIE-style: refinement", bl.AMIE_REFINE),
              *[(f"MAI-DxO-style: {k.replace('_', ' ')} role", t) for k, t in bl.PANEL_ROLES.items()],
              ("MAI-DxO-style: decision", bl.PANEL_DECIDE)]
    return "\n\n".join(f"*{name}.*\n\n```\n{text.strip()}\n```" for name, text in blocks) + "\n"


def result_tables(numbers: dict) -> dict[str, str]:
    out = {}
    hb = numbers.get("_hb_analysis")
    if hb:
        g1 = hb["grader1"]
        rows = ["| Behavior cluster | Criteria | COMPASS pass rate | LLM alone pass rate | COMPASS only | LLM alone only | Exact P | Significant after Holm |",
                "| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |"]
        for c, v in sorted(g1["by_cluster_vs_raw"].items()):
            rows.append(f"| {c.replace('_', ' ')} | {v['n']} | {v['rate_a']:.3f} | {v['rate_b']:.3f} | {v['a_only']} | {v['b_only']} | "
                        f"{v['p_exact']:.3f} | {'Yes' if v['holm_significant'] else 'No'} |")
        out["s7_clusters.md"] = "\n".join(rows) + "\n"
        arms = list(g1["by_theme"])
        themes = sorted({t for a in arms for t in g1["by_theme"][a]})
        rows = ["| Theme | " + " | ".join(arms) + " |", "| :-- |" + " :-- |" * len(arms)]
        for t in themes:
            cells = [f"{g1['by_theme'][a][t]['mean_score']:.3f} (n = {g1['by_theme'][a][t]['n']})" if t in g1["by_theme"][a] else "NA" for a in arms]
            rows.append(f"| {t.replace('_', ' ')} | " + " | ".join(cells) + " |")
        out["s8_themes.md"] = "\n".join(rows) + "\n"
    ca = numbers.get("_cohort_a")
    if ca:
        rows = ["| Score | AUROC for safety hazards (bootstrap 95% CI) |", "| :-- | :-- |"]
        for k, v in ca["auroc_safety"].items():
            rows.append(f"| {k.replace('_', ' ')} | {v['estimate']:.3f} ({v['bootstrap95'][0]:.3f} to {v['bootstrap95'][1]:.3f}) |")
        rows += ["", "| Screen | Net benefit at 0.02 | at 0.05 | at 0.10 |", "| :-- | :-- | :-- | :-- |"]
        for k, m in ca["screens"].items():
            nb = m["net_benefit"]
            rows.append(f"| {k.replace('_', ' ')} | {nb['0.02']:.4f} | {nb['0.05']:.4f} | {nb['0.1']:.4f} |")
        rows += ["", "| Hazard category | Detected by the frozen screen |", "| :-- | :-- |"]
        rows += [f"| {c.replace('_', ' ')} | {v['caught']} of {v['positives']} |" for c, v in ca["recall_by_category"].items()]
        rows += ["", "| Screen compared with the frozen screen, on safety hazards | Frozen only | Other only | Exact P |", "| :-- | :-- | :-- | :-- |"]
        rows += [f"| {k.replace('_', ' ')} | {v['frozen_only']} | {v['other_only']} | {v['p_exact']:.3f} |"
                 for k, v in ca["mcnemar_vs_frozen_on_positives"].items()]
        out["s9_patient_message_secondary.md"] = "\n".join(rows) + "\n"
    return out


def fidelity_section() -> str:
    """Sections 2 to 7 of FID-PCP-001, unchanged, so the appendix and the controlled memo cannot differ."""
    text = (DATA_DIR.parents[1] / "docs" / "regulatory" / "FID-PCP-001_comparator_fidelity.md").read_text()
    body = text.split("## 2. ", 1)[1].split("## 8. ", 1)[0]
    return ("### 2. " + body).replace("\n## ", "\n### ").strip() + "\n"


def freeze_section(freeze_dir: Path) -> str | None:
    import json

    rows = ["| Test set | Items | Test-set SHA-256 | Settings SHA-256 | Frozen commit | Frozen at (UTC) |", "| :-- | :-- | :-- | :-- | :-- | :-- |"]
    for name, label in (("healthbench", "HealthBench Consensus test split"), ("cohort_a", "Patient messages, sealed half")):
        f = freeze_dir / name / "freeze.json"
        if not f.exists():
            return None
        d = json.loads(f.read_text())
        rows.append(f"| {label} | {d['test_set']['n']} | `{d['test_set']['set_sha256']}` | `{d['thresholds_sha256']}` | "
                    f"`{d['architecture_commit'][:12]}` | {d['created_utc'][:19]} |")
    return "\n".join(rows) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manuscript-dir", type=Path, required=True)
    ap.add_argument("--freeze-dir", type=Path, default=DATA_DIR.parents[1] / "docs" / "regulatory" / "freeze")
    args = ap.parse_args()
    supp = args.manuscript_dir / "supplement"
    supp.mkdir(parents=True, exist_ok=True)
    (supp / "s2_fidelity.md").write_text(fidelity_section())
    fz = freeze_section(args.freeze_dir)
    if fz:
        (supp / "s3_freeze.md").write_text(fz)
    out = args.manuscript_dir / "tables"
    out.mkdir(parents=True, exist_ok=True)
    (out / "s5_illness_scripts.md").write_text(scripts_table())
    (out / "s6_rules.md").write_text(rules_table())
    (out / "s12_prompts.md").write_text(prompts_appendix())
    canon = args.manuscript_dir / "CANONICAL_NUMBERS.json"
    if canon.exists():
        import json

        for name, text in result_tables(json.loads(canon.read_text())).items():
            (out / name).write_text(text)
    print("written")


if __name__ == "__main__":
    main()
