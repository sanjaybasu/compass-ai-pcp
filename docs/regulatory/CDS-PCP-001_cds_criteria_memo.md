**Non-Device CDS Criteria Memo (Template): COMPASS at Rung 0 and Rung 1**

|  |  |
| :-: | :-: |
| **Document ID** | CDS-PCP-001 |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | FD&C Act section 520(o)(1)(E); Clinical Decision Support Software final guidance (issued January 6, 2026; re-issued January 29, 2026); SOP-DD-001 §6.1.1 |
| **Parent File** | DHF-001 |
| **Code Baseline** | `waymark-care/compass-pcp` `0d604b1` |

# 1. PURPOSE

This memo records, function by function, whether each software function of the COMPASS meets the four non-device CDS criteria at rung 0 and rung 1. The design document says the product aims to be non-device CDS while a physician signs every item. Rung 2 and rung 3 are device functions and are out of scope here.

# 2. THE FOUR CRITERIA

A software function is non-device CDS only if it meets all four criteria (SOP-DD-001 §6.1.1).

1. It is not intended to acquire, process, or analyze a medical image, a signal from an in vitro diagnostic device, or a pattern or signal from a signal acquisition system.
2. It is intended to display, analyze, or print medical information about a patient or other medical information.
3. It is intended to support or provide recommendations to a health care professional (HCP) about prevention, diagnosis, or treatment of a disease or condition.
4. It is intended to enable the HCP to independently review the basis for the recommendations, so that the HCP does not rely primarily on them to make a clinical diagnosis or treatment decision about an individual patient.

Counsel must check the wording above against the statute text [TO CONFIRM].

# 3. POINTS FROM THE JANUARY 2026 GUIDANCE

FDA's CDRH town hall of March 11, 2026 described these points. Counsel must confirm each against the guidance text [TO CONFIRM].

1. Criterion 3 covers software for an HCP that gives options, a prioritized list of options, or next-step options. It does not cover a specific preventive, diagnostic, or treatment output or directive.
2. FDA intends to use enforcement discretion for a function that fails criterion 3 only because it gives one specific output, where only one clinically appropriate recommendation exists, and that meets the other criteria.
3. For criterion 4, FDA considers the level of automation and the time-critical nature of the HCP's decision. Time-criticality is no longer part of criterion 3.
4. The guidance names automation bias: errors of commission (following wrong advice) and errors of omission (failing to act when not prompted). Urgent situations increase it.
5. The software or labeling should give plain-language background on underlying sources. It should present the basis without information overload.

# 4. FUNCTION INVENTORY AND EVALUATION

Complete one row per function. "Evidence" cites the code path, screen, labeling, or test.

| # | Function | Who sees the output | C1 met? Evidence | C2 met? Evidence | C3 met? Evidence | C4 met? Evidence | Conclusion |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| F1 | SMS interview: next question to the patient (`engine/next_action.py`, Compass) | Patient | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F2 | Routing to a complaint script and parsing messages into findings (`arms/ai_pcp.py::_route`, `_extract`; `findings.py`) | None directly; feeds F3–F7 | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F3 | Differential with posteriors and LR sources (`engine/bayes.py`, `Certificate`) | Physician | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F4 | Cannot-miss escalation (`engine/stopping.py`, `workup.py`) | Physician; patient [TO CONFIRM] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F5 | Deferral to a clinician with reasons (`engine/deferral.py`) | Physician | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F6 | Draft disposition, orders, prescriptions (Compass drafts; `lanes.py` allow-list) | Physician signs | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F7 | Verifier findings that block sign-off (`gate.py`; ANCHOR plan concordance, `anchor_bridge.py::plan_findings`) | Physician, pharmacist | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F8 | Monitoring contract reopen (`monitoring.py`) | Physician | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F9 | Patient messages after sign-off | Patient | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |
| F10 | ANCHOR triage floor (Compass BE-FAST floor; `anchor_bridge.py::red_flag_floor`) | Physician; patient [TO CONFIRM] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] | [TO FILL] |

# 5. ISSUES FOR COUNSEL [TO CONFIRM]

1. F1 and F9 deliver content to patients, not to an HCP. Criterion 3 concerns recommendations to an HCP. The memo must state how patient-facing functions are classified and which FDA policy applies to them.
2. F4 and F10 support emergency escalation. The decision is time-critical, which bears on criterion 4.
3. F4, F6, and F7 can give one specific output (for example "escalate" or a single drug and dose). Record whether criterion 3 fails and whether the single-output enforcement discretion policy applies.
4. Rung 1 requires a physician signature on every item (`lanes.py::needs_physician_signature`). At `0d604b1`, no test verifies this (RTM-PCP-001 REQ-PCP-030).
5. Criterion 4 evidence depends on how the certificate is shown to the physician. The review interface is not built, and no usability evaluation has been done (RAW-PCP-001 RC-30).
6. If any function fails, record whether the product becomes a device at rung 0–1 and which pathway applies.

# 6. CONCLUSION

[TO FILL after Section 4 and Section 5 are complete. Sign by Regulatory Affairs and counsel.]

# 7. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial template |

# 8. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Regulatory Affairs |  |  |
| [TO CONFIRM] | Legal counsel |  |  |
| [TO CONFIRM] | Chief Medical Officer |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
