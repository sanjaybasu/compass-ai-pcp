#!/bin/zsh
# HealthBench Consensus test split, once, with the frozen settings (custodian; VVP-PCP-001 Section 14 step 7).
# Usage: scripts/custodian/run_healthbench_test.sh <output directory outside the repository> [configuration ...]
# With no configurations it runs all five frozen ones in sequence. To finish sooner, run several copies at once with
# different configurations and the same output directory; each writes its own result and cache files.
# The runner refuses to start unless docs/regulatory/freeze/healthbench/freeze.json verifies against this checkout and
# the arguments below match the frozen settings. Resumable: rerun the same command after sleep or a crash.
set -e
OUT=${1:?usage: run_healthbench_test.sh <output directory> [configuration ...]}
shift
CONFIGS=(${@:-ai_pcp_v3 raw_llm llm_standard_guardrails amie_style mai_dxo_style})
cd "$(dirname "$0")/../.."
source scripts/env.sh
scripts/ensure_kev.sh
caffeinate -i .venv/bin/python scripts/run_healthbench.py --subset consensus --split test --repeats 3 --threads 6 \
  --grader openai:gpt-4.1-2025-04-14 --grader2 google:gemini-3.1-pro-preview@LOW \
  --freeze docs/regulatory/freeze/healthbench/freeze.json \
  --configs ${=CONFIGS} \
  --backbone anthropic:claude-opus-5-5 --deliberate anthropic:claude-opus-5-5 --second google:gemini-3.8-flash \
  --out "$OUT"
