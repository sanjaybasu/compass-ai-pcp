**Regulatory File Index: COMPASS Retrospective Validation**

|  |  |
| :-: | :-: |
| **Document ID** | IDX-PCP-001 [TO CONFIRM ID scheme, see Section 3] |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | 21 CFR Part 820 (QMSR); ISO 13485:2016 Clause 7.3; IEC 62304:2006/Amd 1:2015; ISO 14971:2019 |
| **Parent File** | DHF-001 COMPASS Design History File (eQMS register) |
| **Code Baseline** | `waymark-care/compass-pcp` commit `0d604b1` |

# 1. PURPOSE

This index lists the regulatory documents for the retrospective validation of the COMPASS decision layer (`compass-pcp`). It also maps each harness artifact to the section of a marketing submission where FDA recommends that the information goes. The protocol VVP-PCP-001 keeps its registered title and wording ("Compass AI PCP decision layer"), because the OSF registration holds that text; it names the same system as COMPASS and the frozen configuration `ai_pcp_v3`.

# 2. SCOPE AND REGULATORY POSTURE

The design document sets the regulatory posture. This file follows it and does not change it.

1. With a physician who signs every item (rung 0 and rung 1 in `compass_pcp/lanes.py`), the product aims to be non-device CDS under the Clinical Decision Support Software final guidance (January 2026). CDS-PCP-001 holds the criterion-by-criterion memo.
2. Batch review (rung 2), audit-sample review (rung 3), and autonomous refills or prescribing are device functions.
3. The pathway for deterministic refill or titration logic is 510(k). The design document names UpDoc K253281 as the closest precedent. FDA's 510(k) database lists K253281 as "UpDoc", Updoc, Inc., product code NDC, regulation 21 CFR 868.1890, decision date 12/23/2025. [TO CONFIRM predicate suitability with regulatory counsel.]
4. The pathway for autonomous diagnosis plus prescribing is De Novo.

This file covers the retrospective validation only. It does not cover prospective clinical validation, human factors validation (IEC 62366-1), or production deployment.

# 3. DOCUMENT REGISTER

| Document ID | Title | File | Governing SOP | Status |
| :-: | :-: | :-: | :-: | :-: |
| IDX-PCP-001 | Regulatory File Index | `README.md` | SOP-DD-001 | Draft |
| VVP-PCP-001 | Verification and Validation Protocol, Retrospective Validation | `VVP-PCP-001_retrospective_validation_protocol.md` | SOP-DD-001 §6.6–6.7 | Draft |
| DMP-PCP-001 | Data Management Plan | `DMP-PCP-001_data_management_plan.md` | SOP-DD-001 §6.3.2; SOP-DATA-001 | Draft |
| RTM-PCP-001 | Requirements Traceability Matrix | `RTM-PCP-001_traceability_matrix.md` + `.csv` | SOP-DD-001 App. A; SOP-SDLC-001 §12 | Draft |
| RAW-PCP-001 | Risk Analysis Worksheet (seed) | `RAW-PCP-001_risk_analysis.md` + `.csv` | SOP-RM-001; FORM-RM-002 | Draft |
| SOUP-PCP-001 | SOUP and OTS Inventory (template) | `SOUP-PCP-001_soup_ots_inventory.md` | SOP-SDLC-001 §8 | Draft |
| MDC-PCP-001 | Model Card and Algorithm Description (template) | `MDC-PCP-001_model_card.md` | SOP-DD-001 §6.4.3 | Draft |
| PCCP-PCP-001 | Predetermined Change Control Plan (outline) | `PCCP-PCP-001_pccp_outline.md` | SOP-RM-001 §7.2; SOP-DD-001 §6.9.5 | Draft |
| CDS-PCP-001 | Non-Device CDS Criteria Memo (template) | `CDS-PCP-001_cds_criteria_memo.md` | SOP-DD-001 §6.1.1 | Draft |
| VVR-PCP-001 | Validation Report (template) | `VVR-PCP-001_validation_report.md` | SOP-DD-001 §6.7.6 | Draft |

## 3.1 Document ID scheme [TO CONFIRM]

The Waymark QMS uses two ID sets that do not agree.

| Source | IDs for the same SOPs |
| :-: | :-: |
| eQMS register (`waymark-care/waymark-qms`, `server/seed.ts`) | SOP-PDR-001 Design and Development Controls; SOP-PDR-002 Risk Management; SOP-PDR-003 SDLC; DHF-001 COMPASS DHF |
| Controlled SOP text (Google Drive, Subfolder A) | SOP-DD-001; SOP-RM-001; SOP-SDLC-001; cross-references to SOP-QA-00x, SOP-ENG-00x, SOP-SW-00x, FORM-RM-00x, WI-ENG-00x |

Both sets use the pattern `TYPE-AREA-NNN`. These records use the same pattern, with the area code `PCP` and the record-type prefixes in the register above. Each record is filed under DHF-001. This file cites SOPs by their Drive IDs, because those IDs appear in the SOP text. The document control owner must choose one scheme and re-number these records before approval.

## 3.2 Conventions matched from the Waymark QMS

1. The header table has the fields of the controlled SOPs: Document ID, Version, Effective Date, Author or Approver, Classification, and Regulatory Basis. Status uses the eQMS values: Draft, In Review, Approved, Obsolete.
2. The Revision History table has the columns Version, Date, Author, and Description.
3. The approval table has the columns Name, Function, Signature, and Date (SOP-DD-001 Appendix B).
4. Traceability columns follow SOP-DD-001 Appendix A: Req ID, Design Input, Design Output, Verification, Validation, Risk Control.
5. Risk scoring follows SOP-RM-001 §6.3: 5×5 severity × probability matrix and the four acceptability bands.
6. The footer is the controlled-document statement.

# 4. MAP FROM HARNESS ARTIFACTS TO SUBMISSION SECTIONS

The columns name the documentation element from *Content of Premarket Submissions for Device Software Functions* (June 14, 2023) and the section from the draft guidance *Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations* (January 7, 2025). The eSTAR column uses the draft guidance's Appendix A table. Where a placement is Waymark's proposal and not stated in a guidance, the cell says [PROPOSED].

| Artifact (repo path or record) | Premarket software guidance element | AI draft guidance section | Submission section (AI draft App. A) |
| :-: | :-: | :-: | :-: |
| Lanes, rungs, permitted actions (`compass_pcp/lanes.py`); intended use in MDC-PCP-001 | Software Description | V Device Description | Device Description |
| Architecture layers (`README.md` layout table; `compass_pcp/engine/*`, `gate.py`, `findings.py`) | System and Software Architecture Diagram; Software Design Specification | IX Model Description and Development | Software Description |
| Illness scripts and gate rules as sourced data (`compass_pcp/data/`, `engine/scripts.py`, `gate.py::RuleSet`) | Software Design Specification | IX Model Description and Development | Software Description |
| Replayable certificate (`engine/workup.py::Certificate`) shown to the signing physician | Software Description | VI.A User Interface | Software Description |
| ANCHOR rule corpus bridge (`anchor_bridge.py`); Cohort A floor runner (`scripts/run_cohort_a_floor.py`) | Software Design Specification; Software Testing as part of Verification and Validation | IX; X.A | Software Description; Performance Testing |
| RAW-PCP-001 risk analysis | Risk Management File | VII Risk Assessment | Risk Management File of Software Documentation |
| RTM-PCP-001 requirements and traceability | Software Requirements Specification [PROPOSED: traceability also in Software Testing as part of V&V] | VII, X | Software Documentation |
| Unit and integration tests (`tests/`, 49 tests at `0d604b1`) | Software Testing as part of Verification and Validation | X Validation | Software testing as part of verification and validation of Software Documentation |
| DMP-PCP-001; split, hashing, freeze (`harness/episode.py`, `harness/prereg.py`) | — | VIII Data Management | Development data: Software Description; test data: Performance Testing |
| VVP-PCP-001 and VVR-PCP-001; runner, metrics, adjudication, gatekeeper (`harness/runner.py`, `metrics.py`, `adjudication.py`, `gatekeeper.py`) | Software Testing as part of Verification and Validation | X.A Performance Validation | Performance Testing |
| COMPASS arm and comparator arms (`arms/ai_pcp.py`, `arms/baselines.py`, `arms/llm.py`); ablation switches (`engine/workup.py::WorkupConfig`); `harness/configurations.py` | — | X.A Performance Validation | Performance Testing |
| HealthBench public layer (`harness/healthbench.py`, `scripts/run_healthbench.py`) | — | X.A Performance Validation [PROPOSED: supplementary] | Performance Testing |
| Device performance monitoring plan [NOT BUILT; `monitoring.py` holds clinical lab contracts, not device monitoring] | Risk Management File | XI Device Performance Monitoring | Risk Management File of Software Documentation |
| SOUP-PCP-001; SBOM | [PROPOSED: Software Description] | XII Cybersecurity | Cybersecurity |
| MDC-PCP-001 model card | — | VI.B Labeling; XIII Public Submission Summary | Labeling; Administration Information |
| PCCP-PCP-001 | — | — | [UNVERIFIED: eSTAR location for a PCCP] |
| Commit history, freeze file | Software Version History | — | Software Documentation |
| Software Problem Reports (SOP-SDLC-001 App. C) | Unresolved Software Anomalies | — | Software Documentation |
| Repo conventions (`AGENTS.md`), SOP-SDLC-001 | Software Development, Configuration Management, and Maintenance Practices | IV.A Quality System Documentation | Software Documentation |
| Documentation Level evaluation [TO CONFIRM Basic or Enhanced] | Documentation Level Evaluation | — | Software Documentation |
| CDS-PCP-001 memo | Not a submission section. It supports the device or non-device decision. | — | — |

# 5. REFERENCES

| Reference | Date | How verified |
| :-: | :-: | :-: |
| 21 CFR Part 820, Quality Management System Regulation (incorporates ISO 13485:2016) | Effective February 2, 2026 | Stated in the June 2023 software guidance text (fda.gov) |
| Content of Premarket Submissions for Device Software Functions | June 14, 2023 | fda.gov PDF |
| Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations (draft) | January 7, 2025 | fda.gov PDF |
| Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions (final) | December 2024 | Design document; secondary sources. SOP-RM-001 cites an August 2025 update [UNVERIFIED]. |
| Cybersecurity in Medical Devices: Quality Management System Considerations and Content of Premarket Submissions (FD&C Act section 524B) | February 3, 2026 (supersedes June 27, 2025 version) | fda.gov PDF |
| Clinical Decision Support Software (final) | Issued January 6, 2026; re-issued January 29, 2026 | FDA CDRH town hall transcript, March 11, 2026 |
| Good Machine Learning Practice for Medical Device Development: Guiding Principles (FDA, Health Canada, MHRA) | October 2021 | Health Canada and gov.uk pages |
| IEC 62304:2006/Amd 1:2015; ISO 14971:2019; ISO 13485:2016 | — | As cited in SOP-SDLC-001, SOP-RM-001 |
| IEC 62366-1 | [TO CONFIRM edition] | Not cited in the Waymark SOPs |

# 6. OPEN ITEMS [TO CONFIRM]

1. Document ID scheme (Section 3.1) and document owners, authors, and approvers for all ten records.
2. Part 11 e-signature system for the approval tables.
3. Predicate suitability of K253281 and the Documentation Level (Basic or Enhanced).
4. The code at `0d604b1` has no fields for state, race, ethnicity, language, age, or sex on `harness/episode.py::Episode`. The subgroup analyses in VVP-PCP-001 §12 need them.
5. Third-party LLM ids, version pins, vendors, and BAA status (SOUP-PCP-001).
6. The open items listed at the end of each record.

# 7. HOW TO REGENERATE THE TRACEABILITY BASELINE

The traceability matrix cites pytest node ids at commit `0d604b1` (2026-10-27 11:06 -0700). On 2026-10-27, all 49 tests passed on a clean export of that commit, with `ANCHOR_REPO` available (the two ANCHOR bridge tests skip without it). The repository changed twice while these records were drafted (`33e0629`, `0d604b1`), and the working tree had an untracked `compass_pcp/data/scripts/dysuria.yaml`. Regenerate the matrix at the architecture freeze.

1. Check out the frozen commit in a clean tree.
2. Run `.venv/bin/pytest --collect-only -q` and compare node ids to RTM-PCP-001.
3. Run `.venv/bin/pytest -q` and record the result and commit in RTM-PCP-001.
4. Update the Verification Status column for each requirement.

# 8. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial draft |

# 9. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Project Lead |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |
| [TO CONFIRM] | Regulatory Affairs |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
