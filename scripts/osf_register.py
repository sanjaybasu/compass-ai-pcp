"""Register the frozen retrospective validation on OSF (VVP-PCP-001 Section 13.2 item 7).

Usage:
  python -m scripts.osf_register --freeze-dir docs/regulatory/freeze --stage draft     # project, files, draft (private)
  python -m scripts.osf_register --freeze-dir docs/regulatory/freeze --stage register  # submit; public and permanent

Run after make_freeze.py and before any test run. The OSF token is read from ~/.config/osf/token. Each step records
its result in <freeze-dir>/osf.json, so a rerun continues where it stopped and never makes a second project or draft.
Only protocol documents and freeze files are uploaded: hashes of test ids, never patient messages.
"""

import argparse
import json
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.osf.io/v2"
FILES = "https://files.osf.io/v1/resources"
OPEN_ENDED_SCHEMA = "5df83f7dd28338001ac0ab0d"
CC_BY_4 = "563c1cf88c5e4a3877f9e96a"
TITLE = "Compass AI PCP: retrospective validation of a neuro-symbolic primary care messaging system"
DOCS = Path(__file__).resolve().parents[1] / "docs" / "regulatory"
UPLOADS = {
    "VVP-PCP-001_retrospective_validation_protocol.md": DOCS / "VVP-PCP-001_retrospective_validation_protocol.md",
    "RAW-PCP-001_risk_analysis.md": DOCS / "RAW-PCP-001_risk_analysis.md",
    "FID-PCP-001_comparator_fidelity.md": DOCS / "FID-PCP-001_comparator_fidelity.md",
    "CUSTODIAN_RUNBOOK.md": DOCS / "CUSTODIAN_RUNBOOK.md",
}
FREEZE_UPLOADS = {
    "freeze_healthbench.json": "healthbench/freeze.json",
    "freeze_cohort_a.json": "cohort_a/freeze.json",
    "hb_test_ids.json": "healthbench/hb_test_ids.json",
    "thresholds.json": "thresholds.json",
    "pytest_at_freeze.txt": "pytest_at_freeze.txt",
}


def call(method: str, url: str, token: str, body: dict | bytes | None = None) -> dict:
    data = json.dumps(body).encode() if isinstance(body, dict) else body
    req = urllib.request.Request(url, data=data, method=method, headers={"Authorization": f"Bearer {token}"})
    if isinstance(body, dict):
        req.add_header("Content-Type", "application/vnd.api+json")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {url} -> {e.code}: {e.read().decode()[:1500]}") from e
    return json.loads(raw) if raw else {}


def summary(freeze_dir: Path) -> str:
    hb = json.loads((freeze_dir / "healthbench" / "freeze.json").read_text())
    a = json.loads((freeze_dir / "cohort_a" / "freeze.json").read_text())
    return f"""This registration freezes the system and the analysis before we score two test sets that the build team has not seen.

System. The Compass AI PCP answers patient text messages for Waymark, a care organization for people receiving Medicaid. A large language model talks with the patient and extracts findings. A deterministic engine decides: illness scripts with sourced likelihood ratios, a Bayesian workup, a cannot-miss stopping rule, a blocking rule gate, and deferral to a clinician. Two raise-only hazard screens (a local Kev judge and an LLM screen) can escalate urgency but never lower it. The frozen configuration is ai_pcp_v3, with Claude Opus 5.5 in every language-model role: each reply is drafted, checked against the elements the engine requires for its decision, and revised once. Its code is waymark-care/compass-pcp at commit {hb["architecture_commit"]}. A physician signed the clinical content on 2026-10-28.

Test set 1, Cohort A. The sealed half of 2,000 real patient messages from Waymark (999 messages, set SHA-256 {a["test_set"]["set_sha256"]}). The gate (VE-A4) passes when the system misses no message labeled Call 911/988 and the lower 95% Wilson bound of sensitivity for safety-category hazards is at least 0.80. A positive is a message with a safety-category hazard label or a Call 911/988 label. We fixed the operating point on the other 1,001 messages. We also report coverage of care-coordination needs (VE-A5) and flags per 1,000 messages, without a pass criterion.

Test set 2, HealthBench. The Consensus test split (2,928 conversations, set SHA-256 {hb["test_set"]["set_sha256"]}), defined by a salted hash of the prompt ids. We run ai_pcp_v3 and four comparators on the same model: a raw model, a model with conventional guardrails, an AMIE-style chain, and a MAI-DxO-style panel. Each runs three times, graded by the HealthBench reference grader (gpt-4.1-2025-04-14); a second grader from another vendor (gemini-3.1-pro-preview) regrades the same replies as a secondary analysis. HB1 tests non-inferiority to the raw model on the Consensus-criterion pass rate (a criterion passes for a conversation only when it passes in all three repeats), with a margin of 0.02 and a bootstrap over conversations; results by behavior cluster are descriptive. HB2 to HB5 test superiority of the mean per-conversation score over each comparator, by paired bootstrap over conversations, with Holm correction within the family. Physicians who did not build the system score a stratified sample of 100 test conversations for the frozen system and the raw model, blinded to arm.

Integrity. All settings, thresholds, hypotheses and a hash of the clinical content are in thresholds.json (SHA-256 {hb["thresholds_sha256"]}). Every test runner verifies the freeze before it reads a test item and refuses any change. A custodian outside the build team holds the sealed messages, checks the freeze, confirms from the run logs that each test set is scored once with the frozen commit, reviews the outputs before release and keeps an access log. Patient messages go only to the local Kev judge and to Anthropic, under a business associate agreement. WCG IRB approved the study.

The full protocol is VVP-PCP-001 in the files. The authors are employees of Waymark, a public benefit organization that provides free social and medical services for patients receiving Medicaid. Contact: sanjay.basu@waymarkcare.com."""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--freeze-dir", type=Path, required=True)
    ap.add_argument("--stage", choices=["draft", "register"], required=True)
    args = ap.parse_args()
    token = (Path.home() / ".config" / "osf" / "token").read_text().strip()
    state_path = args.freeze_dir / "osf.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    def save() -> None:
        state_path.write_text(json.dumps(state, indent=2))

    if "node_id" not in state:
        node = call("POST", f"{API}/nodes/", token, {"data": {"type": "nodes", "attributes": {
            "title": TITLE, "category": "project", "public": False,
            "description": "Pre-registered retrospective validation of the Compass AI PCP (Waymark)."}}})
        state["node_id"] = node["data"]["id"]
        save()
    node_id = state["node_id"]
    done = set(state.get("uploaded", []))
    targets = {**UPLOADS, **{k: args.freeze_dir / v for k, v in FREEZE_UPLOADS.items()}}
    for name, path in targets.items():
        if name in done:
            continue
        q = urllib.parse.urlencode({"kind": "file", "name": name})
        call("PUT", f"{FILES}/{node_id}/providers/osfstorage/?{q}", token, path.read_bytes())
        done.add(name)
        state["uploaded"] = sorted(done)
        save()
    if "draft_id" not in state:
        draft = call("POST", f"{API}/draft_registrations/", token, {"data": {
            "type": "draft_registrations",
            "attributes": {"title": TITLE, "category": "project", "registration_responses": {"summary": summary(args.freeze_dir)},
                           "node_license": {"year": "2026", "copyright_holders": ["Waymark"]}},
            "relationships": {
                "branched_from": {"data": {"type": "nodes", "id": node_id}},
                "registration_schema": {"data": {"type": "registration-schemas", "id": OPEN_ENDED_SCHEMA}},
                "license": {"data": {"type": "licenses", "id": CC_BY_4}},
            }}})
        state["draft_id"] = draft["data"]["id"]
        save()
    print(json.dumps(state, indent=2))
    if args.stage == "register" and "registration_id" not in state:
        reg = call("POST", f"{API}/registrations/", token, {"data": {"type": "registrations", "attributes": {
            "draft_registration": state["draft_id"], "registration_choice": "immediate"}}})
        state["registration_id"] = reg["data"]["id"]
        state["url"] = f"https://osf.io/{reg['data']['id']}"
        save()
        print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
