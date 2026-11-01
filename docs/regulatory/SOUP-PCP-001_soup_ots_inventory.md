**SOUP and OTS Inventory (Template): COMPASS**

|  |  |
| :-: | :-: |
| **Document ID** | SOUP-PCP-001 |
| **System Name** | COMPASS (Clinically-Optimized Medical Patient Assistance & Support System). In the code COMPASS is the `ai_pcp` arm (`compass_pcp/arms/ai_pcp.py`, class `AiPcpArm`); the frozen configuration is `ai_pcp_v3`. |
| **Version** | 1.0 |
| **Status** | Draft |
| **Effective Date** | [TO CONFIRM, on approval] |
| **Author** | [TO CONFIRM] |
| **Approver** | [TO CONFIRM] |
| **Classification** | Confidential |
| **Regulatory Basis** | IEC 62304 §5.3.3, §5.3.4, §7.1.2, §8.1.2; SOP-SDLC-001 §8 and Appendix B; cybersecurity guidance (February 3, 2026), SBOM |
| **Parent File** | DHF-001 |
| **Code Baseline** | `waymark-care/compass-pcp` `0d604b1` |

# 1. PURPOSE

This inventory lists the software of unknown provenance (SOUP), off-the-shelf (OTS) components, and third-party models that the decision layer and the validation use. Complete one SOUP evaluation checklist (SOP-SDLC-001 Appendix B) per item.

# 2. RULES

1. Record the exact version of each item. A version range is not a pin.
2. Record a hash or checksum where the source provides one.
3. For an LLM, record the exact model id string sent to the API and the vendor's snapshot or version identifier. Do not use an alias that the vendor can repoint.
4. Do not send PHI to a vendor until the BAA status is "signed" and the BAA covers the use.
5. A change to any pinned item follows PCCP-PCP-001 or design change control (SOP-DD-001 §6.9).

# 3. SECTION A: SOFTWARE LIBRARIES (RUNTIME)

"Observed" is the version installed in the development virtual environment on 2026-10-27. It is not a release pin. `pyproject.toml` declares lower bounds only.

| Item | Manufacturer / source | Declared constraint | Observed | Pinned version | Hash | License | Function | Safety class contribution | Known anomalies reviewed | CVE check date |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Python | Python Software Foundation | `>=3.12` | 3.12.14 | [TO FILL] | [TO FILL] | [TO FILL] | Runtime | [TO FILL] | [TO FILL] | [TO FILL] |
| pydantic | Pydantic (PyPI) | `>=2.6` | 2.14.1 | [TO FILL] | [TO FILL] | [TO FILL] | Schema validation of findings, scripts, rules | [TO FILL] | [TO FILL] | [TO FILL] |
| pydantic_core | Pydantic (PyPI) | via pydantic | 2.50.1 | [TO FILL] | [TO FILL] | [TO FILL] | Validation core | [TO FILL] | [TO FILL] | [TO FILL] |
| PyYAML | PyYAML (PyPI) | `>=6.0` | 6.0.3 | [TO FILL] | [TO FILL] | [TO FILL] | Loads scripts and rules (`yaml.safe_load`) | [TO FILL] | [TO FILL] | [TO FILL] |
| annotated-types | PyPI | via pydantic | 0.8.0 | [TO FILL] | [TO FILL] | [TO FILL] | Dependency | [TO FILL] | [TO FILL] | [TO FILL] |
| typing_extensions | PyPI | via pydantic | 4.16.0 | [TO FILL] | [TO FILL] | [TO FILL] | Dependency | [TO FILL] | [TO FILL] | [TO FILL] |
| typing-inspection | PyPI | via pydantic | 0.4.4 | [TO FILL] | [TO FILL] | [TO FILL] | Dependency | [TO FILL] | [TO FILL] | [TO FILL] |

| anthropic SDK | Anthropic (PyPI) | `>=0.40` (extra `arms`) | 2.3.0 | [TO FILL] | [TO FILL] | [TO FILL] | LLM client (`arms/llm.py::AnthropicLLM`) | [TO FILL] | [TO FILL] | [TO FILL] |
| google-genai SDK | Google (PyPI) | `>=1.0` (extra `arms`) | 2.33.0 | [TO FILL] | [TO FILL] | [TO FILL] | LLM client (`arms/llm.py::GeminiLLM`) | [TO FILL] | [TO FILL] | [TO FILL] |
| openai SDK | OpenAI (PyPI) | `>=1.50` (extra `arms`) | 3.40.0 | [TO FILL] | [TO FILL] | [TO FILL] | LLM client (`arms/llm.py::OpenAILLM`) | [TO FILL] | [TO FILL] | [TO FILL] |

Compass (`waymark-care/compass`) has its own dependencies. They go in the Compass SOUP list [TO CONFIRM owner].

# 4. SECTION B: THIRD-PARTY LLMs

One row per role. Roles come from `harness/runner.py::VendorPolicy`, `arms/ai_pcp.py::AiPcpArm`, and `harness/healthbench.py`. `arms/llm.py` records the vendor and model id of every call; the model id is whatever string the caller passes, so the pin must be enforced where the arm is configured. The separation rule requires different vendors for generator and verifier, for extractor A and extractor B, and for generator and gatekeeper paraphraser.

| Role | Used in | Exact model id | Version / snapshot pin | Vendor | API endpoint and region | BAA status | Data retention terms | PHI sent (Y/N) | Deprecation date | Change-notice method | Evaluation evidence |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Backbone / generator | Compass production; all harness configurations | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | VVR-PCP-001 |
| Router (picks the complaint script) | `arms/ai_pcp.py`; Compass production [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | VE-C1 |
| Dialogue (words the reply) | `arms/ai_pcp.py` (`dialogue`); Compass production | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | VE-D1 |
| Extractor A | Compass production | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | VE-A1–A3 |
| Extractor B (different vendor from A) | Compass production | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | VE-A1–A3 |
| Verifier (different vendor from generator) | Compass production [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | VE-B1 |
| Gatekeeper paraphraser (different vendor from generator) | Validation only | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | Y (one answered fact) | [TO CONFIRM] | [TO CONFIRM] | VE-I1 |
| HealthBench reference grader | Validation only, public data | `gpt-4.1-2025-04-14` (`healthbench.py::REFERENCE_GRADER`) | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | Not required if no PHI | [TO CONFIRM] | N | [TO CONFIRM] | [TO CONFIRM] | VE-HB1 |
| HealthBench second-vendor grader | Validation only, public data | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | [TO CONFIRM] | Not required if no PHI | [TO CONFIRM] | N | [TO CONFIRM] | [TO CONFIRM] | VE-HB1 sensitivity |

# 5. SECTION C: EXTERNAL DATA AND INTERFACING SYSTEMS

| Item | Source | Version or pin | Use |
| :-: | :-: | :-: | :-: |
| HealthBench full, hard, consensus files | URLs in `healthbench.py::DATA_URLS` | File names carry dates (2025-05-07, 2025-05-08, 2025-05-09) | Public layer |
| HealthBench grading code | `openai/simple-evals` `healthbench_eval.py` | [TO CONFIRM commit] | Public layer |
| Compass | `waymark-care/compass` | Frozen commit in the freeze file | System under test |
| ANCHOR rule corpus (Light ANCHOR, about 3,128 rules) | `waymark-care/anchor`, `light/` via `ANCHOR_REPO` | Commit recorded by `anchor_bridge.py::anchor_commit` (`+dirty` if modified); local checkout was `28fbdb2` on 2026-10-27 [TO CONFIRM release commit] | Plan concordance findings and red-flag floor |
| lighthouse, coredb, messenger | Waymark infrastructure | Extract log per DMP-PCP-001 §3 | Episode data |

# 6. SECTION D: SUPPORTING TOOLS (NOT IN THE PRODUCT)

| Tool | Declared constraint | Observed | Use |
| :-: | :-: | :-: | :-: |
| pytest | `>=8` | 9.1.1 | Verification |
| ruff | `>=0.4` | 0.17.3 | Static analysis |
| black | `>=24` | 26.10.1 | Formatting |
| mypy | `>=1.10` | 2.4.0 | Type checking |

# 7. OPEN ITEMS

1. Pin runtime versions with hashes for the release build (for example, a lock file) [TO CONFIRM method].
2. Fill every LLM row. Confirm BAA status with the contract owner, not from memory or email.
3. Add the Compass SOUP list or reference it.
4. Produce the SBOM in the format the cybersecurity guidance expects [TO CONFIRM format].

# 8. REVISION HISTORY

| Version | Date | Author | Description |
| :-: | :-: | :-: | :-: |
| 1.0 | 2026-10-27 | [TO CONFIRM] | Initial template |

# 9. APPROVALS

| Name | Function | Signature | Date |
| :-: | :-: | :-: | :-: |
| [TO CONFIRM] | Software Development Lead |  |  |
| [TO CONFIRM] | Cybersecurity Lead |  |  |
| [TO CONFIRM] | Quality Assurance |  |  |

*This document is controlled. © 2026 Waymark Care. All rights reserved.*
