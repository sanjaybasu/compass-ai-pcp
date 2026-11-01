**Validation Report (Template): Retrospective Validation of the COMPASS Decision Layer**

|  |  |
| :-: | :-: |
| **Document ID** | VVR-PCP-001 |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft (template; no results) |
| **Effective Date** | [TO FILL, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | ISO 13485:2016 Clause 7.3.7; SOP-DD-001 §6.7.6; AI-enabled device software functions draft guidance (January 2025) Section X |
| **Parent File** | DHF-001 |
| **Protocol** | VVP-PCP-001 version [TO FILL] |

# 1. PURPOSE

This report gives the results of the validation in VVP-PCP-001. Every number comes from the harness output named in each table's Source column. No number is typed by hand.

# 2. EXECUTION RECORD

| Item | Value | Source |
| :-: | :-: | :-: |
| Architecture commit | 32b907dceb6b | freeze file `architecture_commit` |
| Compass commit | 67952319dda9 | freeze file `compass_commit` |
| Thresholds SHA-256 | d1ed0aca06dc40fc… (both test sets) | freeze file `thresholds_sha256` |
| Test-set SHA-256 and n | HealthBench Consensus test 22c13f2b1e3b12cb…, n = 2,928; Cohort A sealed half 76a8b7e1182f464c…, n = 999 | freeze file `test_set.set_sha256`, `test_set.n` |
| Freeze created (UTC) | 2026-10-28 23:45:00 | freeze file `created_utc` |
| OSF registration | aypqk, registered 2026-10-28 23:45:42 UTC, approved 2026-10-30; https://doi.org/10.17605/OSF.IO/AYPQK | OSF |
| `prereg.py::verify` result before each run | Passed for every run (access log and run logs); later runs accepted only changes listed in DEVIATIONS.json | run log |
| pytest result at frozen commit | 121 passed (freeze/pytest_at_freeze.txt) | RTM-PCP-001 |
| Model ids and versions per role | Dialogue and comparators: anthropic:claude-opus-5-5; second extractor: google:gemini-3.8-flash; LLM hazard screen: anthropic:claude-sonnet-5-5; local judge: kev-4b@v1.0; reference grader: openai:gpt-4.1-2025-04-14; second grader: google:gemini-3.1-pro-preview (thinking LOW) | `SystemOutput.versions`; SOUP-PCP-001 |
| Run dates | Cohort A sealed half 2026-10-28; HealthBench test 2026-10-28 to 2026-10-31 | run log |

# 3. DEVIATIONS

| ID | Date | Description | Impact | Disposition | QA approval |
| :-: | :-: | :-: | :-: | :-: | :-: |
| DEV-PCP-001 (D1) | 2026-10-29 | Guardrail comparator sent an empty draft to its output check; it now returns its clinician handoff for an empty draft (`compass_pcp/arms/baselines.py`, `harness/frozen.py`) | Guardrail comparator only; no existing reply changed | Logged with blob hashes in DEVIATIONS.json | [TO FILL] |
| DEV-PCP-002 (D2) | 2026-10-30 | Second grader blocked one grading prompt and returned no text; three empty replies now score the item as not met (`scripts/run_healthbench.py`) | Second grader only; no reply or reference-grader label changed | Logged with blob hash in DEVIATIONS.json | [TO FILL] |

# 4. COHORT FLOW AND CHARACTERISTICS

## 4.1 Flow

| Step | A | B (per lane) | C positives | C controls | D | HB |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Extracted | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Excluded, with reason | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Dropped for patient overlap (`Split.dropped_for_patient_overlap`) | [ ] | [ ] | [ ] | [ ] | — | — |
| Analyzed | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Selected for adjudication (by reason) | [ ] | [ ] | [ ] | [ ] | — | — |

## 4.2 Characteristics of test data

Source: episode subgroup fields [NOT BUILT at `0d604b1`; VVP-PCP-001 §12].

| Characteristic | Category | n (%) |
| :-: | :-: | :-: |
| State | WA / VA / OH | [ ] |
| Race and ethnicity | [categories TO CONFIRM] | [ ] |
| Preferred language | [ ] | [ ] |
| Age band | [ ] | [ ] |
| Sex | [ ] | [ ] |

# 5. RESULTS AGAINST ACCEPTANCE CRITERIA

Source for each row: `runs/<configuration>.jsonl`, adjudication labels, and the `harness/metrics.py` function named in VVP-PCP-001 §8.

| ID | Endpoint | Numerator / denominator | Estimate | 95% interval | Criterion | Pass / fail |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| VE-A1 | Red-flag polarity accuracy | [ ] / [ ] | [ ] | [ ] | Lower ≥ 0.98 | [ ] |
| VE-A2 | Code accuracy | [ ] / [ ] | [ ] | [ ] | Lower ≥ 0.95 | [ ] |
| VE-A3 | Medication and allergy recall | [ ] / [ ] | [ ] | [ ] | Lower ≥ 0.97 | [ ] |
| VE-C1 | Cannot-miss sensitivity, pooled | [ ] / [ ] | [ ] | [ ] | Lower ≥ 0.95 | [ ] |
| VE-C3 | Escalation and deferral on controls | [ ] / [ ] | [ ] | [ ] | Report | — |
| VE-HB1 | Consensus critical behaviors vs `raw_llm` | per behavior (Section 8) | [ ] | [ ] | Not worse on any | [ ] |
| VE-I1 | Gatekeeper leakage; fabrication | [ ] / 100; [ ] / 100 | [ ] | [ ] | Each < 2% | [ ] |

## 5.0 Results executed in this report (Cohort A sealed half and HealthBench test)

Cohorts B, C and D, and endpoints VE-A1 to VE-A3, VE-C1 to VE-C3 and VE-I1, are not executed in this report; their rows above remain open.

| ID | Endpoint | Numerator / denominator | Estimate | 95% interval | Criterion | Pass / fail |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| VE-A4 | Safety-hazard sensitivity of the frozen hazard screens, sealed half | 19 / 25 | 0.760 (95% CI, 0.566 to 0.885) | Wilson | 0 missed Call 911/988 and lower bound ≥ 0.80 (≥ 24 of 25) | Fail |
| VE-A4 | Call 911/988 messages flagged | 5 / 5 | all flagged at urgent same-day tier or higher; 1 at possible-emergency tier; 0 at emergency tier | Wilson lower 0.566 | 0 missed | Met |
| VE-A5 | Coordination coverage | 38 / 57 | | | Report | — |
| HB1 | Consensus criterion pass rate, COMPASS minus raw_llm | 2,928 conversations | -0.001 (95% CI, -0.011 to +0.008) | bootstrap | Non-inferior, margin 0.02 | Met |
| HB2 | HealthBench score vs raw_llm (reference grader) | 2,928 | +0.008 (95% CI, +0.002 to +0.014) | bootstrap | Superiority, Holm | Met under reference grader; reversed under second grader (-0.008 (95% CI, -0.014 to -0.002)) |
| HB3 | vs llm_standard_guardrails | 2,928 | +0.067 (95% CI, +0.057 to +0.077) | bootstrap | Superiority, Holm | Met |
| HB4 | vs amie_style | 2,928 | +0.025 (95% CI, +0.018 to +0.033) | bootstrap | Superiority, Holm | Met |
| HB5 | vs mai_dxo_style | 2,928 | +0.002 (95% CI, -0.004 to +0.007) | bootstrap | Superiority, Holm | Not met |

Physician check (100 conversations, 2 physicians): COMPASS minus raw_llm +0.023 (95% CI, -0.017 to +0.064). Full results, tables and figures: manuscript package in notebooks/compass-ai-pcp/manuscript (CANONICAL_NUMBERS.json, verified by paper/verify_canonical.py).

## 5.1 Cohort B per lane

| Lane | n | VE-B1 unsafe orders (k / n; upper bound) | VE-B2 under-triage difference (95% CI) | VE-B3 top-3 (k / n; 95% CI) | All B criteria met |
| :-: | :-: | :-: | :-: | :-: | :-: |
| refill | [ ] | [ ] | [ ] | [ ] | [ ] |
| dysuria | [ ] | [ ] | [ ] | [ ] | [ ] |
| uri | [ ] | [ ] | [ ] | [ ] | [ ] |
| conjunctivitis | [ ] | [ ] | [ ] | [ ] | [ ] |
| contraception | [ ] | [ ] | [ ] | [ ] | [ ] |
| htn_titration | [ ] | [ ] | [ ] | [ ] | [ ] |
| dm_titration | [ ] | [ ] | [ ] | [ ] | [ ] |
| undifferentiated_high_risk | [ ] | [ ] | [ ] | [ ] | [ ] |

## 5.2 Cohort C per family (VE-C2)

| Cannot-miss family | Caught / positives | Sensitivity | 95% interval | Lower ≥ 0.90 |
| :-: | :-: | :-: | :-: | :-: |
| [family] | [ ] / [ ] | [ ] | [ ] | [ ] |

## 5.3 Cohort D (never pooled)

| Case id | Type (authored / adversarial / known-miss) | Expected | Observed (3 runs) | Caught |
| :-: | :-: | :-: | :-: | :-: |
| [ ] | [ ] | [ ] | [ ] | [ ] |

# 6. COMPARATORS AND ABLATIONS

Source: `configurations.py::prespecified_hypotheses`; `metrics.py::mcnemar_exact_p`, `paired_bootstrap_diff`; `configurations.py::holm`.

| ID | Contrast | Endpoint | `ai_pcp` estimate | Comparator estimate | Difference (95% CI) | p | Holm-rejected |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| P1 | vs `raw_llm` | Cannot-miss sensitivity (C) | [ ] | [ ] | [ ] | [ ] | [ ] |
| P2 | vs `llm_standard_guardrails` | same | [ ] | [ ] | [ ] | [ ] | [ ] |
| P3 | vs `amie_style` | same | [ ] | [ ] | [ ] | [ ] | [ ] |
| P4 | vs `mai_dxo_style` | same | [ ] | [ ] | [ ] | [ ] | [ ] |
| HB1–HB4 | vs each external comparator | Consensus pass rate (HB) | [ ] | [ ] | [ ] | [ ] | [ ] |
| A1–A5 | vs each ablation | Cannot-miss sensitivity (C) | [ ] | [ ] | [ ] | [ ] | [ ] |
| — | vs historical clinician (B) | Under-triage | [ ] | [ ] | [ ] | — | — |

# 7. SUBGROUP RESULTS

Repeat for each VE endpoint. Source: as Section 5, stratified by the subgroup field.

| Subgroup | Category | k / n | Estimate | 95% interval |
| :-: | :-: | :-: | :-: | :-: |
| State | WA / VA / OH | [ ] | [ ] | [ ] |
| Leave-one-state-out | held-out state | [ ] | [ ] | [ ] |
| Race and ethnicity | [ ] | [ ] | [ ] | [ ] |
| Preferred language | [ ] | [ ] | [ ] | [ ] |
| Age band | [ ] | [ ] | [ ] | [ ] |
| Sex | [ ] | [ ] | [ ] | [ ] |

# 8. HEALTHBENCH CONSENSUS DETAIL

Source: `healthbench.py::compare_consensus` per critical behavior.

| Behavior | n | `ai_pcp` only pass | `raw_llm` only pass | Exact McNemar p | Not worse |
| :-: | :-: | :-: | :-: | :-: | :-: |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

# 9. VALIDATION CONTROLS

| Control | Result | Source |
| :-: | :-: | :-: |
| Component failures by configuration (VE-I2) | [ ] | `RunRecord.status`, `missing_components` |
| Error runs by configuration | [ ] | `RunRecord.status == error` |
| Run-to-run disagreement by configuration and field (VE-I3) | [ ] | `runner.py::run_to_run_disagreement` |
| Rater agreement, Gwet AC1 and Fleiss kappa (VE-I4) | [ ] | `adjudication.py::gwet_ac1`, `fleiss_kappa` |
| Test-set access log reviewed | [ ] | custodian log |
| Vendor separation check passed | [ ] | `runner.py::VendorPolicy` |

# 10. ANOMALIES

| SPR id | Description | Safety impact | Resolution |
| :-: | :-: | :-: | :-: |
| SPR-[YYYY]-[NNN] | [ ] | [ ] | [ ] |

# 11. LIMITATIONS

Copy and update VVP-PCP-001 §18. State each result as an association with the reference standard in this population.

# 12. CONCLUSION PER LANE

| Lane | All gates for the target rung met | Recommended rung | Residual risk acceptable (RAW-PCP-001) |
| :-: | :-: | :-: | :-: |
| [lane] | [ ] | [ ] | [ ] |

# 13. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial template |

# 14. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Project Lead |  |  |
| [TO CONFIRM] | Statistician |  |  |
| [TO CONFIRM] | Medical Lead |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
