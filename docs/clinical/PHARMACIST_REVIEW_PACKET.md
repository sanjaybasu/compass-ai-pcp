# Pharmacist review packet: medication and refill rules

Reviewer: Jeffrey Tingen, PharmD. Physician sign-off: Sanjay Basu, MD, PhD, 2026-10-28.

## What to review

The 148 rules in `compass_pcp/data/rules/` (refill 93, titration 21, contraception 34). Each rule blocks, holds or routes a medication action when its condition holds. `pharmacist_review_rules.csv` lists every rule with its condition, the message the care team sees, and its source. The exact supporting statements are in `REFILL_RULE_SOURCES.md` and `TITRATION_CONTRACEPTION_SOURCES.md`.

## How to review

1. Open `pharmacist_review_rules.csv`.
2. For each rule, mark `pharmacist_agrees_Y_N` with Y or N.
3. For each N, write the change you want in `pharmacist_comment`.
4. List any rule you think is missing at the end of the sheet.
5. Return the sheet to the Project Lead.

## How sign-off is recorded

When every rule is Y, or every N is resolved, the Project Lead records `pharmacist_approved_by: "Jeffrey Tingen, PharmD"` and the date in the `clinical_review` block of each rule file. The refill, titration and contraception lanes do not deploy until both sign-offs are recorded. The frozen evaluation runs the rules as the physician signed them. A rule that changes after this review needs a new freeze before it enters any evaluation, and the paper reports the pharmacist review status.
