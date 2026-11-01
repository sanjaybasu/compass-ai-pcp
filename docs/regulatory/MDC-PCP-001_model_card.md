**Model Card and Algorithm Description (Template): COMPASS**

|  |  |
| :-: | :-: |
| **Document ID** | MDC-PCP-001 |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | AI-enabled device software functions draft guidance (January 2025) Sections V, VI.B, IX, XIII and Appendix E; GMLP principle 9 (clear user information) |
| **Parent File** | DHF-001 |
| **Code Baseline** | `waymark-care/compass-pcp` `0d604b1` |

# 1. PURPOSE

This record follows the example model card in Appendix E of the AI draft guidance. FDA says that example is not a required template. Section 7 adds the algorithm description for the deterministic layer. Fill the performance fields only from VVR-PCP-001.

# 2. DEVICE INFORMATION

| Field | Entry |
| :-: | :-: |
| Name of the device | [TO CONFIRM] |
| Version | `compass-pcp` [frozen commit]; Compass [frozen commit] |
| Date created or last updated | [TO FILL] |
| Model architecture | LLM components for interviewing, parsing, and drafting (Section 6), plus a deterministic decision layer (Section 7) |

# 3. REGULATORY STATUS

| Field | Entry |
| :-: | :-: |
| Authorization status | [TO FILL] |
| File number | [TO FILL] |

# 4. DESCRIPTION

| Field | Entry |
| :-: | :-: |
| Intended users | Patients (SMS interview) and Waymark physicians who review and sign [TO CONFIRM wording] |
| Intended use and indications for use | [TO CONFIRM]. Limit to the lanes in `lanes.py::Lane` at their approved rungs. |
| Intended patient population | Medicaid managed-care members served by Waymark in WA, VA, OH, adults [TO CONFIRM age limits] |
| Instructions for use | [TO FILL] |
| Clinical benefits and limitations | [TO FILL from VVR-PCP-001]. Rung 0–1: a physician reviews and signs every item. |
| Clinical workflow phase | Patient triage; telehealth; clinical decision support |
| Inputs | Patient SMS messages; Clinical Context from the Waymark record (claims, pharmacy fills, labs, ADT) |
| Outputs | Next question, deferral, escalation, or completed encounter with draft disposition, orders, prescriptions, and patient messages; verifier findings; a replayable certificate |
| Degree of automation | Rung 0: draft only. Rung 1: physician signs every item. Rung 2: AI acts with batch review within 24 hours. Rung 3: AI acts with audit-sample review (`lanes.py::Rung`). |

# 5. PERFORMANCE AND LIMITATIONS

Fill each cell from VVR-PCP-001. Every estimate carries its two-sided 95% interval and denominator.

| Field | Entry |
| :-: | :-: |
| Accuracy: parser (VE-A1–A3) | [TO FILL] |
| Accuracy: unsafe orders per lane (VE-B1) | [TO FILL] |
| Accuracy: under-triage versus clinician (VE-B2) | [TO FILL] |
| Accuracy: top-3 differential (VE-B3) | [TO FILL] |
| Accuracy: cannot-miss sensitivity, pooled and per family (VE-C1, VE-C2) | [TO FILL] |
| Precision (reproducibility): run-to-run disagreement across three runs (VE-I3) | [TO FILL] |
| Known biases or failure modes | [TO FILL from subgroup tables and Cohort D] |
| Known gaps in data characterization | [TO FILL] |
| Limitations in development or evaluation | Retrospective replay; temporal split within one organization; claims lag; see VVP-PCP-001 §18 |
| Where inputs will not match development data | Non-SMS channels; languages not in the test set [TO CONFIRM]; complaints outside the lanes (the system defers) |
| Evidence | OSF registration [TO FILL]; publication identifiers [TO FILL] |
| Test data characterization | Sources, data types, sample size, reference standard, representativeness: DMP-PCP-001 and VVR-PCP-001 §4 |
| Methods that show intended use is met | Retrospective validation (VVP-PCP-001); usability evaluation [NOT DONE] |

# 6. LLM COMPONENTS

| Role | Model id and pin | Vendor | Prompt label and version |
| :-: | :-: | :-: | :-: |
| Router | SOUP-PCP-001 | SOUP-PCP-001 | [TO FILL] |
| Dialogue / generator | SOUP-PCP-001 | SOUP-PCP-001 | [TO FILL] |
| Extractor A | SOUP-PCP-001 | SOUP-PCP-001 | [TO FILL] |
| Extractor B | SOUP-PCP-001 | SOUP-PCP-001 | [TO FILL] |
| Verifier | SOUP-PCP-001 | SOUP-PCP-001 | [TO FILL] |

The LLMs are not trained or fine-tuned by Waymark [TO CONFIRM]. They propose. The deterministic layer decides.

# 7. ALGORITHM DESCRIPTION (DETERMINISTIC LAYER)

This section describes `0d604b1`. Update it at the freeze.

1. *Routing.* An LLM router picks one complaint script, or none. It also lists up to three suspected diagnoses. "None" or an unparseable reply hands the patient to a clinician (`arms/ai_pcp.py::AiPcpArm._route`).
2. *Parsing.* Two extractors from different vendors code the conversation into findings for the script's features. The layer accepts a finding only when both agree on code, polarity, and value. Otherwise the feature is disputed (`findings.py::reconcile`).
3. *Provenance.* For each feature, the structured record outranks a patient-confirmed record item, which outranks a new patient report, which outranks inference (`findings.py::Provenance`, `merge_with_record`).
4. *Truth bounds.* Each predicate has bounds [L, U] under Łukasiewicz logic. Unknown is [0, 1]. Conflicting assertions give L > U, which is a contradiction (`engine/truth.py`).
5. *Illness scripts.* One script per complaint lists diagnoses, priors, likelihood ratios, and test and treat thresholds for cannot-miss diagnoses. Thresholds are given, or computed by the Pauker–Kassirer method from benefit, harm, and the best remote test. Every number has a source. A production load needs physician sign-off (`engine/scripts.py`).
6. *Bayesian update.* logit p = logit prior + Σ ln LR, with LR+ for present and LR− for absent findings. Within a correlated group, only the strongest LR applies. For a cannot-miss diagnosis, an absent finding counts only if it came from the record or from an explicit confirmation answer. Each ln LR is drawn 200 times from its 95% CI with a seed from the inputs, so the result replays. The layer reports p05 and p95 and uses p95 for every safety decision (`engine/bayes.py`).
7. *Cannot-miss stopping rule.* If p95 < test threshold, the diagnosis is ruled out. If p95 ≥ treat threshold, the layer escalates. Between them, the encounter cannot close (`engine/stopping.py`).
8. *Next question.* The layer ranks questions by miss-weighted expected information gain (weight 10 for cannot-miss diagnoses by default) with a noisy-OR model of a positive answer, minus cost and risk terms. It never asks a known feature or one that cannot be asked remotely (`engine/next_action.py`).
9. *Deferral.* The layer defers when the complaint is outside the lane; facts conflict; a decision-relevant finding is still unconfirmed after it was asked; a cannot-miss diagnosis is in the middle zone with no remote test left, or after the question budget; repeated runs disagree; residual uncertainty stays above eta after the budget; or the LLM proposed a diagnosis that is not in the script (`engine/deferral.py`, `engine/workup.py`).
10. *Gate.* Rules are data, with OR terms allowed. A rule blocks when its antecedent is definitely true. It holds and asks for the missing fact when the antecedent could be true. A missing or stale lab is unknown. Conflicting facts make the gate defer. At rung 0–1, a finding blocks sign-off until it is accepted or overridden with a coded reason. At rung 2–3, a finding halts the action and escalates (`gate.py`).
11. *ANCHOR corpus.* Each fired ANCHOR rule on a drafted plan becomes a blocking finding. ANCHOR under-triage rules also run over patient text as a red-flag floor. The corpus commit is recorded with each result (`anchor_bridge.py`).
12. *Lanes.* Each lane has an allow-list of actions (`lanes.py`).
13. *Monitoring contracts.* Each order carries a lab contract. A breach or an overdue lab reopens the case (`monitoring.py`).
14. *Certificate.* Each step records its inputs, posteriors, LR sources, thresholds, deferral reasons, and candidate actions, so a reviewer can replay it (`engine/workup.py::Certificate`).
15. *Repeated runs.* Each patient-visible message runs the pipeline three times. Any difference in route, decision, or asked features defers (`arms/ai_pcp.py::AiPcpArm.next_message`).

# 8. RISK MANAGEMENT

| Field | Entry |
| :-: | :-: |
| Potential risks | RAW-PCP-001 hazards HAZ-01 to HAZ-14 |
| Information that could change risk over the lifecycle | Vendor model changes; new lanes; script and rule changes; population change |
| Deployment and updates | PCCP-PCP-001 |
| Ongoing performance monitoring | [NOT BUILT; TO CONFIRM plan] |
| Software quality | IEC 62304, ISO 14971, ISO 13485 per SOP-SDLC-001, SOP-RM-001, SOP-DD-001 |

# 9. DEVELOPMENT DATA

| Field | Entry |
| :-: | :-: |
| Data sources | messenger, lighthouse, coredb (`dbt_tuva_core`); BMC messages; DMP-PCP-001 §3 |
| Data types | Unstructured text (SMS); structured claims, fills, labs, ADT |
| Sample size, reference standard, representativeness | [TO FILL from dev split] |

# 10. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial template |

# 11. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Project Lead |  |  |
| [TO CONFIRM] | Medical Lead |  |  |
| [TO CONFIRM] | Regulatory Affairs |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
