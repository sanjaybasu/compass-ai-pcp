# Custodian runbook: sealed test sets

Custodian: Parth Sheth. Protocol: VVP-PCP-001, Sections 8.5, 13 and 14.

Two test sets are scored once each, with the frozen system: the sealed half of Cohort A (999 real patient messages) and the HealthBench Consensus test split (2,928 public conversations). The scripts do the work, and the build team may start them on Waymark-managed storage. Your job is to keep the sealed data private, check the freeze against OSF, confirm from the run log that each test set was scored once with the frozen commit, review the outputs before they are released, and keep the access log. Sections 3 to 5 list the commands, whoever starts them.

## 1. Before the freeze

1. Do no development work on compass-pcp from the freeze until the report is approved.
2. Receive two files from the data engineer through a Waymark-approved channel: the 2,000-message Cohort A file and `cohort_a_test_ids.json`.
3. Store both files on Waymark-managed storage that only you can read.
4. Make an output folder there for the Cohort A run. Keep it outside the repository.
5. Ask the Project Lead for the OSF registration link after the freeze.

## 2. Set up the machine

1. Clone `waymark-care/compass-pcp` and check out the frozen commit named in the OSF registration.
2. Make sure `git status` shows no changes. The runners refuse a changed checkout.
3. Create the environment: `python3.12 -m venv .venv && .venv/bin/pip install -r requirements.lock`.
4. Set a data folder outside the repository: `export COMPASS_PCP_DATA=<your path>`.
5. Run `scripts/setup_vendor.sh`. It fetches simple-evals and Kev at the pinned commits.
6. Set `export KEV_DIR=$COMPASS_PCP_DATA/vendor/kev`. Kev needs `uv` and an Apple silicon Mac.
7. Export `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` and `GOOGLE_API_KEY` in your shell.
8. Run `source scripts/env.sh`. It warns about any missing key.
9. Start the local Kev judge with `scripts/ensure_kev.sh`. It must answer on port 8009.
10. Run `.venv/bin/python -m pytest -q`. All tests must pass.

## 3. Check the freeze against OSF

1. Open `docs/regulatory/freeze/cohort_a/freeze.json` and `docs/regulatory/freeze/healthbench/freeze.json`.
2. Compare `architecture_commit`, `thresholds_sha256` and `test_set.set_sha256` in each file with the OSF registration.
3. Stop and tell the Project Lead if any value differs. Do not run a test set.

## 4. Run the sealed Cohort A half

1. Run this command, with your own paths:

   ```
   source scripts/env.sh
   .venv/bin/python -m scripts.custodian.run_cohort_a_sealed \
     --freeze docs/regulatory/freeze/cohort_a/freeze.json \
     --cases <your path>/realworld_cases_n2000_clean.json \
     --test-ids <your path>/cohort_a_test_ids.json \
     --out <your output folder> \
     --access-log <your output folder>/access_log.jsonl
   ```

2. If the laptop sleeps or the run stops, run the same command again. It continues from its cache.
3. Read `cohort_a_sealed_report.json` in the output folder. `VE_A4.pass` is the gate result.
4. Keep `per_message.jsonl`, the caches and the access log in the output folder. They contain message ids, not message text.

The script sends patient text only to the local Kev judge and to Anthropic, which is under the Waymark BAA. It sends nothing to Google or OpenAI.

## 5. Run the HealthBench test split

1. Run `scripts/custodian/run_healthbench_test.sh <output folder>`. Use a folder outside the repository.
2. Expect a long run. Five configurations run three times on 2,928 conversations.
3. If the run stops, run the same command again. It continues from its cache.
4. Read `summary.json` in the output folder when the run ends.

## 6. After the runs

1. Give the two reports to the statistician.
2. Do not give test outputs to the build team before the report is approved.
3. Keep the access log with the outputs. It is part of the design history file.
4. Tell the Project Lead the date and time of each run.

## If something fails

| Message | Meaning | Action |
| :-- | :-- | :-- |
| `freeze violated: architecture commit changed` | The checkout is not the frozen commit. | Check out the frozen commit again. |
| `freeze violated: thresholds changed` | Code, settings or clinical content changed after the freeze. | Stop. Tell the Project Lead. |
| `freeze violated: test set changed` | The id file differs from the frozen one. | Get the correct id file from the data engineer. |
| `working tree has uncommitted changes` | A file in the checkout was edited. | Run `git stash` or clone again. |
| `sealed ids are missing from --cases` | The message file is incomplete. | Get the full 2,000-message file. |
| Kev connection refused | The local judge is not running. | Run `scripts/ensure_kev.sh`. |
