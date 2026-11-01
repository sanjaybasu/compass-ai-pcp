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
| Architecture commit | [TO FILL] | freeze file `architecture_commit` |
| Compass commit | [TO FILL] | freeze file `compass_commit` |
| Thresholds SHA-256 | [TO FILL] | freeze file `thresholds_sha256` |
| Test-set SHA-256 and n | [TO FILL] | freeze file `test_set.set_sha256`, `test_set.n` |
| Freeze created (UTC) | [TO FILL] | freeze file `created_utc` |
| OSF registration | [TO FILL] | OSF |
| `prereg.py::verify` result before each run | [TO FILL] | run log |
| pytest result at frozen commit | [TO FILL] | RTM-PCP-001 |
| Model ids and versions per role | [TO FILL] | `SystemOutput.versions`; SOUP-PCP-001 |
| Run dates | [TO FILL] | run log |

# 3. DEVIATIONS

| ID | Date | Description | Impact | Disposition | QA approval |
| :-: | :-: | :-: | :-: | :-: | :-: |
| DEV-PCP-[NNN] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |

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
