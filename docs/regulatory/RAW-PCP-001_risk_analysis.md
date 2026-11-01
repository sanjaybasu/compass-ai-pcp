**Risk Analysis Worksheet (Seed): COMPASS Decision Layer**

|  |  |
| :-: | :-: |
| **Document ID** | RAW-PCP-001 (form basis: FORM-RM-002 Risk Analysis Worksheet) |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | ISO 14971:2019; SOP-RM-001; AI-enabled device software functions draft guidance (January 2025) Section VII |
| **Parent File** | DHF-001; Risk Management File per SOP-RM-001 §9 |
| **Code Baseline** | `waymark-care/compass-pcp` `0d604b1` |
| **Data File** | `RAW-PCP-001_risk_analysis.csv` |

# 1. PURPOSE

This worksheet seeds the ISO 14971 risk analysis for the decision layer. It lists hazards, hazardous situations, harms, and the risk controls in the code. It also shows how each control is verified for implementation and effectiveness.

# 2. METHOD

1. Each row is one hazard and one risk control.
2. Severity and probability use the 5-point scales in SOP-RM-001 §6.3.1. The score is severity × probability. Acceptability uses the bands in SOP-RM-001 §6.3.1 and Appendix A.
3. Initial severity is a proposal from this seed. The Medical Lead must confirm it.
4. No probability data exist before validation. Per SOP-RM-001 §6.3.2, initial probability is set to the highest credible level (5).
5. Control types follow the priority order in SOP-RM-001 §6.6.1: inherently safe design, protective measure, information for safety.
6. "Verification of Implementation" cites the RTM requirement and its pytest status. "Verification of Effectiveness" cites the validation endpoint in VVP-PCP-001.
7. Residual columns stay empty until VVR-PCP-001 is approved.
8. Status uses the eQMS values: Identified, Mitigated, Accepted, Closed.

# 3. HAZARDS

| ID | Hazard | Proposed initial severity |
| :-: | :-: | :-: |
| HAZ-01 | Missed cannot-miss diagnosis | 5 |
| HAZ-02 | Unsafe order or prescription | 4 |
| HAZ-03 | Parser polarity error | 5 |
| HAZ-04 | Record staleness | 4 |
| HAZ-05 | LLM veto of the deterministic triage floor | 5 |
| HAZ-06 | Fail-open on error or unknown | 5 |
| HAZ-07 | Third-party LLM drift or silent version change | 5 |
| HAZ-08 | Automation bias in physician review | 5 |
| HAZ-09 | Lower performance in a subgroup | 5 |
| HAZ-10 | Wrong clinical number in a script or rule | 5 |
| HAZ-11 | PHI written to application logs | 2 [TO CONFIRM scale] |
| HAZ-12 | Action outside lane scope | 4 |
| HAZ-13 | Missed post-order monitoring | 4 |
| HAZ-14 | Validation leakage overstates performance | 5 |
| HAZ-15 | Router sends the conversation to the wrong complaint script | 5 |
| HAZ-16 | Ablation switch left on in production | 5 |
| HAZ-17 | Patient acts on individualized advice before physician review | 4 |

# 4. FINDINGS FROM THE SEED

1. Five controls are not built. RC-28 is the production fail-safe. RC-29 is vendor-model drift monitoring. RC-30 is usability engineering of the review interface. RC-31 is the recency check in `findings.py::merge_with_record`. RC-33 is a guard that keeps the ablation switches in `WorkupConfig` at their defaults in production. RC-29, RC-30, and RC-31 have no requirement in RTM-PCP-001 yet.
2. RC-16 (record outranks report) is a risk control for HAZ-02. It also creates HAZ-04, because `merge_with_record` does not use `Finding.observed_on`. SOP-RM-001 §6.6.5 requires analysis of risks that come from risk controls.
3. RC-17 (conversation-wide ANCHOR floor) is a proposed patch to `waymark-care/compass`. It is not applied.
4. RC-19 (vendor separation) is enforced in the validation runner only. The production vendor assignment is a Compass configuration [TO CONFIRM].
5. RC-36 (no individualized advice before sign-off) is a prompt instruction to an LLM. It has no deterministic check.
6. The gate now treats a missing or stale lab as unknown (`gate.py::lab_bounds`), which holds the dependent rule. This reduces HAZ-04 for labs. It does not cover other record items.

# 5. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial seed from `0d604b1` |

# 6. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Risk Management Lead |  |  |
| [TO CONFIRM] | Medical Lead |  |  |
| [TO CONFIRM] | Data Science / ML Engineering |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
