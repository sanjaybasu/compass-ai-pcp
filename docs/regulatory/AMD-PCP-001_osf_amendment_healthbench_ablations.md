# AMD-PCP-001: Amendment to OSF registration aypqk — additional HealthBench analyses

Status: DRAFT, not filed. File on OSF (10.17605/OSF.IO/AYPQK) before any run in Section 4 starts.

## 1. Reason for the amendment

The registered HealthBench test run did not record which path produced each reply. A later re-run of the frozen router
estimated that 524 of 2,928 test conversations (17.9%) reached the decision engine. The registered analyses therefore
cannot show the effect of the engine on reply quality. The registered ablations A1–A5 apply to Cohort C, which is not
yet complete.

During the preparation of this amendment we also found a defect in the evaluation harness. `AiPcpV2` stores the
router's `user_type` on the arm instance between `build_ledger` and `next_message`. The registered test run shared one
arm across 8 threads, so a reply can use the `user_type` of a different conversation. The effect on the registered
result is unknown. Analysis 1 measures it.

## 2. What does not change

1. The frozen system (commit 32b907d), its configuration, the models, the test split and both graders do not change.
2. The registered primary and secondary analyses stay as registered and are reported first.
3. The new analyses are reported as analyses added by this amendment, after the test split was first scored.

## 3. Analyses added

*Analysis 1. Re-run of the frozen system with recorded paths.* We run the frozen `ai_pcp_v3` once more on all 2,928
Consensus test conversations, 3 repeats each. Each worker builds its own arm, so the defect in Section 1 cannot occur.
For each reply we record the user type, the complaints, the decision and the hazard tier. We report the overall score
under both graders next to the registered score. We report the difference from the registered `raw_llm` run with the
registered method.

*Analysis 2. Engine ablation.* For each reply in Analysis 1, we keep the router result, the hazard screens and the
extracted findings. We then write the reply again with no engine decision (`engine_off`): the composer uses its general
path. Replies that the engine did not decide are the same in both arms by construction. The primary contrast is the
mean score difference, `ai_pcp_v3` minus `engine_off`, on the replies where the engine made the decision. We also
report the difference on all replies.

*Analysis 3. Component ablations.* With the same method as Analysis 2, we change one engine setting at a time:
`minus_stopping_rule` (`enforce_stopping_rule = False`), `fixed_question_order` (`fixed_question_order = True`),
`rule_out_authority` (`bayes_rule_out_authority = True`), `eig_questions` (`question_policy = "eig"`), and
`single_extractor` (findings from extractor A only). The rule-gate ablations in the protocol are not part of
`ai_pcp_v3` and are not run. A reply is written again only when the changed setting changes the decision.

## 4. Statistical analysis

1. Scores are HealthBench overall scores from simple-evals, unchanged, under the reference grader (GPT-4.1) and the
   second grader (Gemini 3.1 Pro).
2. Differences are paired by conversation and repeat. 95% confidence intervals come from a bootstrap over
   conversations, 10,000 resamples, as in the registered analysis.
3. There is no hypothesis test and no margin. We report estimates with 95% confidence intervals.
4. We interpret a difference as inconclusive when its 95% confidence interval includes zero under either grader, or
   when the two graders give opposite signs.
5. For Analysis 1, we report the difference between the re-run and the registered score under each grader. If the
   difference is larger than the registered non-inferiority margin (0.02), we report it as a deviation.

## 5. Conduct

1. Model calls use the vendors' batch interfaces (Anthropic Message Batches, OpenAI Batch, Gemini Batch) with the same
   model identifiers, prompts, token limits and temperatures as the registered run.
2. Code: `paper/ablation_staged.py` and `paper/batch_stage.py` in waymark-care/compass-pcp. The frozen package
   `compass_pcp/` is not edited.
3. Only public HealthBench data are used. No patient data are sent to any model in these analyses.
