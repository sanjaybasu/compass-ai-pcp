# FID-PCP-001 Comparator fidelity memo

Version 1.0, 2026-10-28. Code: `compass_pcp/arms/baselines.py`. Protocol: VVP-PCP-001 Sections 7.2 and 10. System: COMPASS (Clinically-Optimized Medical Patient Assistance & Support System); code arm `ai_pcp`, frozen configuration `ai_pcp_v3`.

## 1. Purpose

The protocol compares COMPASS with four external comparators. Three of them reconstruct published systems from their descriptions, because the original systems are not available to run. This memo states what each reconstruction keeps from its source, what it changes, and why. A reader can then judge whether a difference in results comes from structure or from our implementation.

## 2. Rules shared by every arm

1. Every arm uses the same language model for its main reasoning and reply. On the test split, this model is Claude Opus 5.5 (`anthropic:claude-opus-5-5`).
2. Every arm uses the same output policy. A patient or caregiver gets an SMS reply: plain text, no markdown, at most 600 characters, a 6th-grade reading level, at most two questions, in the patient's language. A health professional gets the task asked, in the length and format asked for, brief by default.
3. Every arm has the same output-token budget for its final reply (1,200 tokens).
4. Every arm sees the same conversation and nothing else. No arm sees a patient record on HealthBench.
5. No arm sees HealthBench rubrics, ideal completions or grader output.

## 3. Raw model (`raw_llm`)

*Source.* None; this is the unstructured baseline.

*Implementation.* One call with a short persona: the model answers messages sent to a primary care team that serves Medicaid patients, takes a history when needed and gives a plan, under the shared output policy.

*What it tests.* The contribution of structure over the same model with no scaffold.

## 4. Conventional guardrail stack (`llm_standard_guardrails`)

*Source.* The Coalition for Health AI (CHAI) publishes assurance standards, not a guardrail implementation. This arm therefore puts into practice the controls that deployed health chatbots commonly use and that CHAI-style assurance asks for: an input screen for emergencies and self-harm, a scope limit, a persona that forbids prescribing and doses, an output safety classifier, a disclaimer and a handoff to a clinician.

*Implementation.* Four steps. (1) An LLM classifies the latest message for emergency, self-harm and out-of-scope. An emergency or self-harm result returns a fixed 911/988 message. (2) An out-of-scope result returns a fixed redirect. (3) The model drafts a reply under the persona, the shared output policy, and "do not prescribe or name doses". (4) An LLM reviews the draft for false diagnostic certainty, dangerous instructions, prescribing and discouraging care; an unsafe draft becomes a fixed handoff message. A safe draft gets a short disclaimer.

*Differences from practice.* Production stacks often use dedicated moderation models. We use the same language model for every check, so the arm differs from the raw model only in structure.

## 5. AMIE-style chain (`amie_style`)

*Sources.* Tu et al., Nature 2025 (AMIE), which uses an inference-time chain of reasoning before each dialogue turn; Vedadi et al. 2025 (guardrailed AMIE), which withholds individualized medical advice and defers a plan to an overseeing physician.

*Implementation.* Three calls per turn. (1) Analysis: summarize the history, list a differential with likelihoods, and list the most useful missing information. (2) Draft: write the next message from the analysis, asking for missing information or explaining likely causes and next steps, without individualized treatment advice before physician review. (3) Self-critique and refinement: critique the draft against accuracy, context seeking, safety and escalation, empathy, the advice guardrail and the output policy, and return only the improved message. The refinement step sees the conversation and the draft.

*Differences from the source.* AMIE is a fine-tuned model trained with simulated self-play; we cannot reproduce its weights or training. We reproduce its published inference-time chain and its guardrail on our shared model. The original guardrailed system hands a structured note to a physician; our arm has no physician in the loop, as in every arm on HealthBench.

## 6. MAI-DxO-style panel (`mai_dxo_style`)

*Source.* Nori et al., arXiv 2506.22405 (MAI Diagnostic Orchestrator), which orchestrates one model as a virtual panel of physician roles that debate before each action, with a cost-aware steward.

*Implementation.* Six calls per turn. Five role calls run in sequence, and each sees the notes of the roles before it: hypothesis (probability-ranked differential), test chooser (up to two questions or tests that best separate the leading diagnoses), challenger (argue against the leading diagnosis and name cannot-miss risks), stewardship (prefer cheaper, safer steps), and checklist (check for errors and safety gaps). A final call decides to ask, escalate or explain likely causes and next steps, then writes the message.

*Differences from the source.* The source works on sequential diagnosis cases with a gatekeeper that reveals test results at a cost. HealthBench conversations have no test results to order, so the cost budget acts only through the stewardship role. We use one pass of the panel per turn; the source can run several debate rounds before it acts.

## 7. Known limits of the comparison

1. The reconstructions follow the published descriptions. They are not the original systems, and the paper names them "AMIE-style" and "MAI-DxO-style".
2. COMPASS uses more structure (scripts, rules, two hazard screens) than any comparator. The ablation family in the protocol tests which parts of that structure matter.
3. All arms are graded by the same reference grader; a second grader from another vendor and a physician-scored sample test how much the result depends on the grader (VVP-PCP-001 Section 8.6).

## 8. Approval

| Name | Function | Date |
| :-- | :-- | :-- |
| Sanjay Basu, MD, PhD | Project Lead | 2026-10-28 |
| Named in the validation report | Fidelity reviewer outside the build team | |
