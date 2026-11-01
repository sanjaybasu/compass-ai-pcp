**Predetermined Change Control Plan (Outline): COMPASS**

|  |  |
| :-: | :-: |
| **Document ID** | PCCP-PCP-001 |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | Marketing Submission Recommendations for a PCCP for AI-Enabled Device Software Functions (final, December 2024); SOP-RM-001 §7.2; SOP-DD-001 §6.9.5 |
| **Parent File** | DHF-001 |
| **Code Baseline** | `waymark-care/compass-pcp` `0d604b1` |

# 1. PURPOSE

This outline describes the planned changes that Waymark proposes to make without a new marketing submission. It applies only to the device functions (rung 2 and rung 3 lanes) in an authorized submission. Under SOP-RM-001 §7.2.2, a PCCP has three parts: a description of the modifications, the methodology to develop, validate, and implement them, and an impact assessment. Sections 3, 4, and 5 follow that order.

# 2. BOUNDS

1. A modification stays inside the authorized intended use, lanes, and user population.
2. A modification does not add a lane, add an action to `lanes.py::LANE_ACTIONS`, or move a lane to a higher rung. Each of these needs a new submission or design change review [TO CONFIRM with regulatory counsel].
3. A modification does not weaken a risk control in RAW-PCP-001. For example, it does not make the gate advisory, set `WorkupConfig.enforce_stopping_rule` to False, set `fixed_question_order` to True, remove the second extractor, or lower `n_runs` below 3.
4. All modifications are manual. A person approves each one. The system does not learn in the field.

# 3. DESCRIPTION OF MODIFICATIONS

| ID | Type | What can change | What cannot change |
| :-: | :-: | :-: | :-: |
| M1 | Model swap | The model id or version of the backbone, extractor A, extractor B, or verifier, including a vendor change | Vendor separation (`runner.py::VendorPolicy`); the deterministic layer |
| M2 | Prompt edit | Prompt text and prompt label for interviewing, parsing, drafting, or verifying | Output schema (`findings.py::Finding`, `runner.py::SystemOutput`) |
| M3 | Rule addition or update | A new or changed gate rule, lab-recency rule, monitoring contract, illness-script feature, diagnosis, prior, LR, miss weight, or noisy-OR leak, each with a `source` and sign-off; a new ANCHOR corpus commit | Removal of a cannot-miss diagnosis; a rule that cannot fire on unknown |
| M4 | Threshold change | Cannot-miss test and treat thresholds or their Pauker–Kassirer inputs (`benefit`, `harm`, `test_se`, `test_sp`, `test_harm`); `WorkupConfig.eta`, `question_budget`, `questions_per_message`, `lambda_cost`, `lambda_risk`; lab-recency windows; ANCHOR `min_severity` | A change that lowers any acceptance criterion in VVP-PCP-001 |

# 4. MODIFICATION PROTOCOL

## 4.1 Common steps

1. Open a change request under SOP-DD-001 §6.9 with the modification ID and type.
2. Update the risk analysis for the change.
3. Run `pytest` on the changed commit. All tests must pass.
4. Run the regression set: Cohort D in full, plus the PCCP verification set (Section 4.3).
5. Compare the results with the acceptance criteria in Section 4.2.
6. Update SOUP-PCP-001, MDC-PCP-001, and labeling as needed.
7. Get approval from Quality Assurance and the Medical Lead.
8. Deploy with the rollback plan in Section 4.4.
9. Record the change in the PCCP change log.

## 4.2 Verification per modification type

| Type | Harness reuse | Acceptance criteria |
| :-: | :-: | :-: |
| M1 Model swap | `runner.py::run_all` with three runs per episode over Cohorts A, B, C on the PCCP verification set; `VendorPolicy` check; HealthBench test split | Every VE criterion in VVP-PCP-001 §8 still met; no new Cohort D miss; run-to-run disagreement not higher than the authorized version [TO CONFIRM margin] |
| M2 Prompt edit | As M1 for the affected role; Cohort A for parser prompts | As M1 |
| M3 Rule addition | Unit test per rule in `tests/` (true, false, and unknown antecedent); `load_rules` or `load_script` validation; Cohort B for the lane and Cohort C for any changed cannot-miss diagnosis | VE-B1 and VE-C1/C2 for the affected lane and family; pharmacist or physician sign-off with source |
| M4 Threshold change | `engine/stopping.py`, `engine/workup.py` tests; Cohort C and Cohort B for affected lanes | VE-C1/C2 lower bounds still met; VE-B2 still met |

## 4.3 PCCP verification set

1. Reuse of the original test set for each change can overfit the system to that set over time.
2. Waymark reserves a sequestered PCCP verification set, held by the custodian, disjoint from the validation test set [TO CONFIRM size and refresh rule].
3. The freeze method (`prereg.py::freeze`, `verify`) applies to each PCCP run.

## 4.4 Rollback

1. Keep the prior authorized version deployable.
2. Roll back if post-deployment monitoring breaches a limit [TO CONFIRM limits; monitoring NOT BUILT].

# 5. IMPACT ASSESSMENT

For each modification, record the following.

1. Benefits and risks of the change.
2. Affected hazards and risk controls in RAW-PCP-001.
3. Effect on each lane and each subgroup in VVP-PCP-001 §12.
4. Effect of this change combined with earlier PCCP changes.
5. Labeling and user communication.

# 6. OPEN ITEMS

1. Confirm the PCCP guidance date and any later update. SOP-RM-001 cites an August 2025 update [UNVERIFIED].
2. Confirm with regulatory counsel which of M1–M4 FDA will accept in the PCCP for this device.
3. Define post-deployment monitoring and rollback limits.

# 7. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial outline |

# 8. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Data Science / ML Engineering |  |  |
| [TO CONFIRM] | Regulatory Affairs |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
