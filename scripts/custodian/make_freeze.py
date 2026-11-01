"""Write the freeze files (custodian step, VVP-PCP-001 Section 13.2 item 7). Run once, on a clean checkout of the
commit to be frozen, after the full test suite passes.

Usage: python -m scripts.custodian.make_freeze --compass-commit <sha> --cohort-a-test-ids <custodian path> --out docs/regulatory/freeze

Writes, under --out:
  healthbench/freeze.json, healthbench/hb_test_ids.json  (public HealthBench prompt ids)
  cohort_a/freeze.json                                   (hashes of the sealed ids only; the ids stay with the custodian)
  thresholds.json                                        (the frozen settings, for reading; verification rebuilds them from code)
Then post the two freeze.json files to OSF before any test run.
"""

import argparse
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

from compass_pcp.harness import frozen
from compass_pcp.harness.healthbench import DATA_URLS, dev_split
from compass_pcp.harness.prereg import freeze


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--compass-commit", required=True, help="waymark-care/compass main commit at the freeze (traceability)")
    ap.add_argument("--cohort-a-test-ids", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    tests = subprocess.run([sys.executable, "-m", "pytest", "-q"], check=False, cwd=frozen.REPO, capture_output=True, text=True)
    if tests.returncode != 0:
        sys.exit("pytest fails on this commit; nothing frozen\n" + tests.stdout[-2000:])
    arch = frozen.architecture_commit()
    thresholds = frozen.frozen_thresholds()
    with urllib.request.urlopen(DATA_URLS["consensus"], timeout=120) as fh:
        rows = [json.loads(line) for line in fh.read().decode().splitlines() if line.strip()]
    _, hb_test = dev_split([r["prompt_id"] for r in rows], salt=frozen.HB_SALT)
    a_test = json.loads(args.cohort_a_test_ids.read_text())
    (args.out / "healthbench").mkdir(parents=True, exist_ok=True)
    (args.out / "cohort_a").mkdir(parents=True, exist_ok=True)
    (args.out / "healthbench" / "hb_test_ids.json").write_text(json.dumps(sorted(hb_test)))
    (args.out / "thresholds.json").write_text(json.dumps(thresholds, indent=2))
    common = {"architecture_commit": arch, "compass_commit": args.compass_commit, "thresholds": thresholds}
    hb = freeze(args.out / "healthbench" / "freeze.json", test_ids=hb_test, **common)
    a = freeze(args.out / "cohort_a" / "freeze.json", test_ids=a_test, **common)
    (args.out / "pytest_at_freeze.txt").write_text(tests.stdout)
    print(json.dumps({"architecture_commit": arch, "thresholds_sha256": hb.thresholds_sha256,
                      "healthbench_test": {"n": hb.test_set["n"], "set_sha256": hb.test_set["set_sha256"]},
                      "cohort_a_test": {"n": a.test_set["n"], "set_sha256": a.test_set["set_sha256"]}}, indent=2))


if __name__ == "__main__":
    main()
