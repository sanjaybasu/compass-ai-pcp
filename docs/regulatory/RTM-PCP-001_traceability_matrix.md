**Requirements Traceability Matrix: COMPASS Decision Layer**

|  |  |
| :-: | :-: |
| **Document ID** | RTM-PCP-001 |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | IEC 62304 §5.1, §5.2, §5.7; ISO 13485:2016 Clause 7.3; ISO 14971:2019 §7; SOP-SDLC-001 §12 |
| **Parent File** | DHF-001 |
| **Code Baseline** | `waymark-care/compass-pcp` `0d604b1` (49 tests collected, 49 passed on a clean export with `ANCHOR_REPO` available, 2026-10-27) |
| **Data File** | `RTM-PCP-001_traceability_matrix.csv` |

# 1. PURPOSE

The matrix links each requirement to its design output, its risk control, its verification test, and its validation endpoint. It follows the columns of SOP-DD-001 Appendix A.

# 2. COLUMNS

| Column | Content |
| :-: | :-: |
| Req ID | REQ-PCP-NNN |
| Design Input | The requirement, from the design rules and the code docstrings |
| Design Output | Repository path and function or class |
| Risk Control | RC id in RAW-PCP-001 |
| Verification | pytest node id, separated by ` ; `. A `compass:` prefix means a test in `waymark-care/compass` from the proposed patch. `NONE` means no test exists. |
| Verification Status | Result at `0d604b1`, or `NOT VERIFIED` with the reason |
| Validation | VE id in VVP-PCP-001, an ablation id, or a process record |
| Notes | Gaps and dependencies |

# 3. SUMMARY AT 0d604b1

| Item | Count |
| :-: | :-: |
| Requirements | 56 |
| Requirements with a passing unit test | 42 (4 partial: REQ-PCP-015, -022, -024, -042) |
| Requirements not verified | 14 |
| pytest node ids collected | 49; every one maps to at least one requirement |

The 14 requirements without verification fall into four groups.

1. Not built: production extractors (REQ-PCP-003), production fail-safe (REQ-PCP-035), subgroup fields (REQ-PCP-048).
2. Proposed but not applied: the Compass ANCHOR floor patch (REQ-PCP-033, REQ-PCP-034).
3. Built without a test: REQ-PCP-009, -021, -028, -030, -038, -053, -055.
4. Not built and no test: the guard that keeps ablation switches off in production (REQ-PCP-054). Process control: REQ-PCP-031.

REQ-PCP-052 passes only when `ANCHOR_REPO` points at a checkout of `waymark-care/anchor`; without it the two tests skip. The Notes column names each gap.

# 4. BASELINE CAUTION

The repository changed twice while this matrix was drafted (`33e0629`, `0d604b1`). The matrix cites `0d604b1`. Regenerate it at the freeze with the steps in IDX-PCP-001 §7.

# 5. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial draft from `0d604b1` |

# 6. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Software Development Lead |  |  |
| [TO CONFIRM] | Risk Management Lead |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
