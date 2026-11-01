# Illness-script sources: GI bleeding, adult fever, hyperglycemia, early-pregnancy pain or bleeding

This file lists the source of each number in these four scripts:

- `compass_pcp/data/scripts/gi_bleeding.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/adult_fever.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/hyperglycemia_symptoms.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/pelvic_pain_bleeding_possible_pregnancy.yaml` (version 0.1.0-draft)

All four scripts use lane `undifferentiated_high_risk`. They are drafts for physician sign-off. `clinical_review.approved_by` is null in all four files.

Status labels (same as `SCRIPT_SOURCES.md`):

- **VERIFIED.** We copied the value from a table or results text that we read.
- **DERIVED.** We calculated the value from counts or estimates in a table that we read. The calculation is given.
- **PLACEHOLDER.** The value is a literature value that a Waymark claims rate (DS-5) or a CPD decision-analysis memo must replace.
- **[UNVERIFIED — omitted].** We did not put the value in a script.

We calculated derived 95% CIs for likelihood ratios (LRs) with the log method (Simel DL, Samsa GP, Matchar DB. Likelihood ratios with confidence: sample size estimation for diagnostic test studies. *J Clin Epidemiol*. 1991;44(8):763-770. PMID 1941027): $SE(\ln LR^{+}) = \sqrt{1/a - 1/(a+c) + 1/b - 1/(b+d)}$, where $a$ is true positives, $c$ is false negatives, $b$ is false positives, and $d$ is true negatives. We calculated $LR^{-}$ in the same way. For a binary partition (for example, DKA compared with simple hyperglycemia in the same study), the complement diagnosis takes $LR^{+}_{\text{complement}} = 1/LR^{+}$ and $LR^{-}_{\text{complement}} = 1/LR^{-}$, and the CI limits are the reciprocals of the CI limits.

Every cannot-miss threshold is a decision-analysis input with the YAML source string "PLACEHOLDER: CPD decision-analysis memo; illustrative values". In each threshold table, benefit B is the net benefit of same-day in-person care when the diagnosis is present, and harm R = 1 is the unit harm of one unnecessary same-day in-person visit when it is absent. test_se, test_sp, and test_harm describe the in-person evaluation that would confirm or exclude the diagnosis. The engine calculates T_test and T_treat with `pauker_kassirer` in `compass_pcp/engine/scripts.py`. None of these inputs comes from a published decision analysis. The CPD memo must replace them.

## Sources that we read

| Key | Citation | Access |
|---|---|---|
| Srygley 2012 | Srygley FD, Gerardo CJ, Tran T, Fisher DA. Does this patient have a severe upper gastrointestinal bleed? *JAMA*. 2012;307(10):1072-1079. PMID 22416103. doi:10.1001/jama.2012.253 | PubMed abstract (prevalences, LR+ values with CIs). We could not open the JAMA full text (paywall, HTTP 403). We read the LR table in a verbatim reproduction: Chopra A, et al. Gastroenterology. In: *Approach to Internal Medicine*. Springer; 2015. doi:10.1007/978-3-319-11821-5_5 (PMC7123601), lines 237-257, which cites "JAMA 2012 307:10". The reproduction gives LR+ and LR− with no CIs. |
| Kim 2017 | Kim SS, Kim KU, Kim SJ, et al. Predictors for the need for endoscopic therapy in patients with presumed acute upper gastrointestinal bleeding. *Korean J Intern Med*. 2019;34(2):288-295 (epub 2017). PMID 29232942. doi:10.3904/kjim.2016.406 | PMC6406092, Table 1 and Results text |
| Jones 2009 | Jones R, Charlton J, Latinovic R, Gulliford MC. Alarm symptoms and identification of non-cancer diagnoses in primary care: cohort study. *BMJ*. 2009;339:b3094. PMID 19679615. doi:10.1136/bmj.b3094 | PMC2726930, Table 4 and Results text |
| Komatsu 2025 | Komatsu T, Inoue K, Someya Y, et al. Diagnostic accuracy of self-reported food consumption and shaking chills in predicting bacteremia in outpatients: a prospective, multicenter observational study. *PLoS One*. 2025;20(7):e0327789. PMID 40627656. doi:10.1371/journal.pone.0327789 | PMC12237268, Tables 1, 3, and 4 and Results text |
| Afhami 2017 | Afhami S, Dehghan Manshadi SA, Rezahosseini O. Jolt accentuation of headache: can this maneuver rule out acute meningitis? *BMC Res Notes*. 2017;10(1):540. PMID 29084605. doi:10.1186/s13104-017-2877-1 | PMC5663092, Results text |
| Peamyao 2025 | Peamyao W, Lokeskrawee T, Lawanaskol S, et al. Predictive factors for diagnosing diabetic ketoacidosis or simple hyperglycemia in adults with high blood glucose: the "1-DKA Alert" study. *J Clin Med Res*. 2025;17(3):164-173. PMID 40115837. doi:10.14740/jocmr6180 | PMC11922632, Table 1 and Methods text |
| Arora 2011 | Arora S, Henderson SO, Long T, Menchine M. Diagnostic accuracy of point-of-care testing for diabetic ketoacidosis at emergency-department triage: β-hydroxybutyrate versus the urine dipstick. *Diabetes Care*. 2011;34(4):852-854. PMID 21307381. doi:10.2337/dc10-1844 | PMC3064039, full text (Results) |
| Yan 2025 | Yan JW, Van Aarsen K, Thorne J, et al. A multicenter prospective cohort study evaluating 30-day outcomes after an emergency department visit for hyperglycemia in Canadian adults with type 1 or 2 diabetes. *CJEM*. 2025;27(7):551-558. PMID 40279059. doi:10.1007/s43678-025-00913-6 | PMC12279581, Table 3 and Results text |
| Mimoun 2016 | Mimoun C, Fauconnier A, Varas C, Huchon C. Is a self-assessed questionnaire useful for the diagnosis of ectopic pregnancy in hospitalized patients? *PLoS One*. 2016;11(11):e0155054. PMID 27832075. doi:10.1371/journal.pone.0155054 | PMC5104447, Tables 1 and 3 and Results text |
| Stein 2010 | Stein JC, Wang R, Adler N, et al. Emergency physician ultrasonography for evaluating patients at risk for ectopic pregnancy: a meta-analysis. *Ann Emerg Med*. 2010;56(6):674-683. PMID 20828874. doi:10.1016/j.annemergmed.2010.06.563 | PubMed abstract only |
| Fisher 2024 | Fisher S, Couperthwaite S, Yang EH, Essel NOM, Rowe BH. Utility of pelvic examination in assessing women with bleeding in early pregnancy: a multicenter Canadian emergency department study. *Int J Emerg Med*. 2024;17(1):110. PMID 39227764. doi:10.1186/s12245-024-00686-2 | PMC11370077, Results text |

## GI-bleeding script

Population: adults who report blood in vomit or stool. The location LRs and the upper-GI prior come from adults evaluated in EDs or admitted for acute GI bleeding (Srygley 2012). The severity LRs are conditional on an upper GI bleed. A person who texts about a small amount of red blood on toilet paper is a lower-risk population, so the priors are high for this lane.

### Upper GI bleed (location; not cannot-miss)

| Feature | LR+ (95% CI) | LR− | Remote | Location in source | Status |
|---|---|---|---|---|---|
| `prior_ugib` | 6.2 (no CI) | 0.81 | yes | Srygley table, "Prior history of UGIB" | VERIFIED (reproduction) |
| `age_under_50` | 3.5 (no CI) | 0.80 | yes (also in the record) | Srygley table, "Age <50 years" | VERIFIED (reproduction) |
| `cirrhosis` | 3.1 (no CI) | 0.97 | yes | Srygley table, "Cirrhosis" (UGIB vs LGIB) | VERIFIED (reproduction) |
| `melena_history` | 5.9 (range 5.1-5.9) | 0.27 (range 0.06-0.27) | yes | Srygley abstract (LR+ range) and table (LR− range) | VERIFIED (range; end chosen) |
| `clots_in_stool` | 0.05 (0.01-0.38) | 1.2 | yes | Srygley abstract (LR+, CI) and table (LR−) | VERIFIED |
| `bun_cr_ratio_over_30` | 7.5 (2.8-12.0) | 0.53 | no (lab) | Srygley abstract (LR+, CI) and table (LR−) | VERIFIED |

Srygley reports melena history as a range of single-study LRs, not a summary. We used LR+ 5.9 and LR− 0.27, the ends that move a cannot-miss upper-GI probability up most and down least. This pair is consistent: it implies sensitivity 0.77 and specificity 0.87.

Prior: p = 0.63. Srygley abstract: "The majority of patients (N = 1776) had an acute UGIB (prevalence, 63%; 95% CI, 51%-73%)." Status: PLACEHOLDER (DS-5).

### Upper GI bleed that needs urgent intervention (cannot-miss)

Srygley defines severe bleeding as bleeding that needs urgent intervention. Kim 2017 compares 329 patients who had endoscopic hemostasis with 284 who did not, among 613 adults with presumed acute UGIB in one Korean hospital.

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `syncope` | 3.0 (no CI) | 0.95 | hemodynamic | yes | VERIFIED (Srygley table, reproduction) |
| `pulse_over_100` | 4.9 (3.2-7.6) | 0.34 | hemodynamic | yes, with a home BP cuff or pulse oximeter | VERIFIED (Srygley abstract LR+ and CI; table LR−) |
| `cirrhosis` | 3.2 (no CI) | 0.89 | none | yes | VERIFIED (Srygley table, reproduction) |
| `glasgow_blatchford_above_0` | 1.2 | 0.02 (abstract CI 0-0.05; not entered) | none | no (labs, vitals) | VERIFIED |
| `hematemesis` | 1.27 (1.09-1.48) | 0.76 (0.64-0.90) | bleeding_presentation | yes | DERIVED |
| `melena_history` | 0.94 (0.85-1.04) | 1.15 (0.91-1.46) | bleeding_presentation | yes | DERIVED |

Derivations (Kim 2017 Table 1, endoscopic hemostasis n = 329 vs no hemostasis n = 284): hematemesis TP 197, FN 132, FP 134, TN 150; melena TP 221, FN 108, FP 203, TN 81. Kim also reports syncope or presyncope (14/329 vs 4/284; derived LR+ 3.02, 1.01-9.07; LR− 0.97, 0.95-1.00). This agrees with the Srygley value (3.0), so we used the Srygley meta-analytic value. The Blatchford CI lower limit is 0, which the schema does not accept, so the YAML has no CI for that row. Groups: `hemodynamic` (syncope and tachycardia both show blood loss); `bleeding_presentation` (Kim counts hematemesis and melena in the same patients).

Prior: p = 0.227. DERIVED as 0.63 (UGIB prevalence) × 0.36 (Srygley abstract: "36% (95% CI, 29%-44%) had severe bleeding" among clinically diagnosed UGIB). The severity LRs are conditional on UGIB, but the engine applies them to all GI-bleed reports. The reviewer must decide if this mismatch is acceptable. Status: PLACEHOLDER (DS-5).

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 30 | A missed severe UGIB can cause shock and death. Same-day ED care when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day ED visit. |
| test_se | 0.95 | Illustrative sensitivity of ED evaluation (vitals, hemoglobin, BUN, Blatchford score). Not sourced. |
| test_sp | 0.8 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit and blood tests. |

The engine calculates T_test = 0.0087 and T_treat = 0.326.

### Lower GI bleed (cannot-miss)

Definition: the complement of UGIB among adults with acute GI bleeding in Srygley 2012. All six LRs are DERIVED as reciprocals of the UGIB LRs above: `prior_ugib` 0.16 / 1.23; `age_under_50` 0.29 / 1.25; `cirrhosis` 0.32 / 1.03; `melena_history` 0.17 / 3.70; `clots_in_stool` 20.0 (2.63-100.0) / 0.83; `bun_cr_ratio_over_30` 0.13 (0.083-0.36) / 1.89.

Prior: p = 0.37, the complement of 0.63. Status: PLACEHOLDER (DS-5). Lower GI bleeding and hemorrhoidal bleeding overlap, because hemorrhoids are a lower GI source. The engine treats them as separate diagnoses.

Thresholds (illustrative): B = 5, R = 1, test_se = 0.9, test_sp = 0.8, test_harm = 0.05. We set B lower than for severe UGIB because a lower GI bleed is a location, not a severity. Many lower GI bleeds do not need same-day care; we did not find a source with a rate. The engine calculates T_test = 0.0532 and T_treat = 0.577.

### Hemorrhoidal bleeding

Prior: p = 0.087. Jones 2009 Table 4 ("Diagnoses 90 days and three years after presentation with rectal bleeding in general practice") gives haemorrhoids at 90 days in 596 women (7.8%) and 738 men (10.0%). The total is 1,334 of 15,289 UK primary-care patients with a first recorded rectal bleeding (8.7%). This is the proportion with a recorded diagnosis, so it is a low estimate of the true proportion. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

### Engine behavior (GI bleeding)

With no findings, `step` returns ASK for `melena_history` and `clots_in_stool`. Both cannot-miss diagnoses are in the middle zone (severe UGIB 0.227; lower GI bleed 0.37). Smoke tests: melena and syncope present with no hematemesis gives severe-UGIB p = 0.40 (p95 0.44), and the engine returns ESCALATE. Clots in stool with all other answers reassuring gives lower-GI-bleed p = 0.98, and the engine returns ESCALATE. With the remote features, severe UGIB cannot fall below T_test (the lowest product of LRs gives p of about 0.06), so the script never rules it out remotely.

## Adult-fever script

Population: adults with fever who are not pregnant and not immunosuppressed. The bacteremia LRs come from adult outpatients (ED or general medicine clinic) who had blood cultures drawn in Tokyo (Komatsu 2025). Bacteremia is the sepsis proxy, because we found no paired history LRs for sepsis itself.

### Bloodstream infection (true bacteremia), the sepsis proxy (cannot-miss)

Komatsu 2025 Table 4 ("Diagnostic accuracy") gives the values below for all patients. The published CIs are symmetric on the LR scale, which is unusual. We copied them as published.

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `shaking_chills` | 3.74 (2.75-4.73) | 0.79 (0.29-2.18) | none | yes | VERIFIED |
| `poor_food_intake` | 1.08 (0.09-2.08) | 0.66 (0.23-1.94) | none | yes | VERIFIED |
| `qsofa_2_or_more` | 2.06 (1.07-3.06) | 0.80 (0.29-2.19) | qsofa | no | VERIFIED |
| `new_confusion` | 1.74 (1.28-2.37) | 0.75 (0.60-0.93) | qsofa | yes, patient or family report | DERIVED |
| `sbp_100_or_less` | 1.82 (1.12-2.98) | 0.88 (0.76-1.01) | qsofa | yes, with a home BP cuff | DERIVED |

Derivations (Komatsu 2025 Table 1, bacteremia n = 68, non-bacteremia n = 466): GCS < 15 in 30 (44.1%) vs 118 (25.4%); SBP ≤ 100 mmHg in 16 (23.9%) vs 57 (13.1%). The table does not print the denominators for these rows. We inferred them from the percentages: 465 for GCS (118/465 = 25.4%), and 67 and 435 for SBP. A log-method CI from the shaking-chills counts (18/68 vs 33/466) gives LR+ 3.74 (2.23-6.26) and LR− 0.79 (0.68-0.91); the script uses the published values. The `new_confusion` question asks about new confusion or sleepiness. The source measured GCS < 15 in hospital, which also counts baseline impairment such as dementia. Group `qsofa`: the qSOFA score contains the SBP and mental-status items.

Prior: p = 0.127. Komatsu 2025 Results: "68 (12.7%) in the BG" of 534. These patients had blood cultures drawn, so the prior is high for a text-based fever population. Status: PLACEHOLDER (DS-5).

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 30 | Early antibiotics for bacteremia and sepsis reduce death. |
| harm R | 1 | One unnecessary same-day in-person visit. |
| test_se | 0.9 | Illustrative sensitivity of in-person evaluation (vital signs, exam, blood tests). Not sourced. |
| test_sp | 0.7 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit and blood tests. |

The engine calculates T_test = 0.0128 and T_treat = 0.176.

### Acute meningitis (cannot-miss)

| Feature | LR+ (95% CI) | LR− (95% CI) | Remote | Status |
|---|---|---|---|---|
| `jolt_headache` | 5.36 (3.37-8.52) | 0.42 (0.31-0.59) | yes, guided self-maneuver | VERIFIED point values; CIs DERIVED |

Afhami 2017 Results: "The Jolt maneuver was positive in 40/64 (62.5%) of meningitis and 19/163 (11.7%) of non-meningitis patients." The paper reports LR+ 5.36 and LR− 0.42 with no CI. 2x2: TP 40, FN 24, FP 19, TN 144. Population: 227 adults in an Iranian ED with fever and headache and suspected meningitis; meningitis is CSF WBC > 5 (any cause). A physician did the maneuver. The script asks the patient to do it, which nobody has validated. Other studies of the same maneuver report much lower accuracy (Mofidi 2016 in the same kind of population: LR+ 1.02, LR− 0.91; PMC5357091, read). We used Afhami because it is the largest single study we could read. The reviewer must weigh this conflict.

Prior: p = 0.0094. DERIVED from Komatsu 2025 Table 3 ("Definitive diagnosis of study patients"): bacterial meningitis 2 (bacteremia group) + viral meningitis 3 (non-bacteremia group) = 5 of 534. Status: PLACEHOLDER (DS-5).

Thresholds (illustrative): B = 100 (untreated bacterial meningitis has high death and disability), R = 1, test_se = 0.95, test_sp = 0.9 (illustrative values for ED evaluation with lumbar puncture), test_harm = 0.1 (burden of a lumbar puncture). The engine calculates T_test = 0.0021 and T_treat = 0.136.

### Febrile illness without bacteremia

Definition: the complement of true bacteremia in Komatsu 2025 (466 patients, including 21 contaminated cultures). All five LRs are DERIVED as reciprocals of the bacteremia LRs: `shaking_chills` 0.27 (0.21-0.36) / 1.27 (0.46-3.45); `poor_food_intake` 0.93 (0.48-11.1) / 1.52 (0.52-4.35); `new_confusion` 0.58 (0.42-0.78) / 1.34 (1.07-1.66); `sbp_100_or_less` 0.55 (0.34-0.90) / 1.14 (0.99-1.31); `qsofa_2_or_more` 0.49 (0.33-0.93) / 1.25 (0.46-3.45).

Prior: p = 0.873, the complement of 0.127. Status: PLACEHOLDER (DS-5).

### Engine behavior (adult fever)

With no findings, `step` returns ASK for `jolt_headache` and `poor_food_intake`. Smoke tests:

- Shaking chills present gives bacteremia p = 0.29 (p95 0.34) and ESCALATE.
- Jolt positive with no shaking chills and no confusion gives meningitis p = 0.048 and DEFER (`cannot_miss_middle_zone_no_remote_test`).
- All remote answers reassuring gives bacteremia p = 0.054 but p95 = 0.225, which is above T_treat (0.176), so the engine returns ESCALATE. The wide published CIs for `poor_food_intake` (LR+ 0.09-2.08, LR− 0.23-1.94) cause this. The script cannot close a fever encounter remotely with these sources.

## Hyperglycemia script

Population: adults with known diabetes who report high blood sugar, thirst, or vomiting. Peamyao 2025 studied 274 adults in a Thai ED with capillary glucose > 250 mg/dL (56 DKA, 218 simple hyperglycemia; ADA 2009 criteria). Arora 2011 studied 516 adults in a Los Angeles ED with glucose ≥ 250 mg/dL (54 DKA). Yan 2025 studied 657 adult ED visits for hyperglycemia in Ontario.

### Diabetic ketoacidosis (cannot-miss)

| Feature | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|
| `vomiting_or_belly_pain` | 23 | 33 | 55 | 163 | 1.63 (1.10-2.40) | 0.79 (0.63-0.99) | none | yes | DERIVED |
| `trouble_breathing` | 42 | 14 | 74 | 144 | 2.21 (1.74-2.81) | 0.38 (0.24-0.60) | none | yes | DERIVED |
| `fever` | 18 | 38 | 55 | 163 | 1.27 (0.82-1.99) | 0.91 (0.75-1.10) | none | yes, home thermometer | DERIVED |
| `previous_dka` | 14 | 42 | 9 | 209 | 6.06 (2.76-13.27) | 0.78 (0.67-0.91) | none | yes | DERIVED |
| `uses_insulin` | 39 | 17 | 64 | 154 | 2.37 (1.81-3.10) | 0.43 (0.29-0.64) | insulin_dependence | yes | DERIVED |
| `type_1_diabetes` | 8 | 48 | 3 | 215 | 10.38 (2.85-37.86) | 0.87 (0.78-0.97) | insulin_dependence | yes | DERIVED |
| `missed_diabetes_medicines` | 42 | 14 | 97 | 121 | 1.69 (1.36-2.08) | 0.45 (0.28-0.72) | none | yes | DERIVED |
| `urine_ketones_positive` | 53 | 1 | 300 | 162 | 1.51 (1.40-1.63) | 0.053 (0.0075-0.37) | ketone_test | yes, home urine strips | DERIVED |
| `blood_ketone_over_1_5` | 53 | 1 | 99 | 363 | 4.58 (3.83-5.47) | 0.024 (0.0034-0.16) | ketone_test | yes, home blood ketone meter | DERIVED |

Sources for the counts: the first seven rows are Peamyao 2025 Table 1 ("Baseline Characteristics of Patients With Diabetic Ketoacidosis and Simple Hyperglycemia"): "Gastrointestinal/hepatobiliary" symptoms, "Dyspnea", "Fever", "Previous diabetic ketoacidosis", "Insulin usage", "Type 1 DM", and "Poor compliance". Peamyao assessed compliance from records, history, or HbA1c ≥ 9%, so the script question about missed medicines is a proxy. The last two rows are from Arora 2011 Results: sensitivity 98.1% (53/54) for both tests, specificity 35.1% for the urine dipstick and 78.6% for capillary β-OHB > 1.5 mmol/L, with 462 patients without DKA. We rounded TN to 162 (0.351 × 462 = 162.2) and 363 (0.786 × 462 = 363.1). ED nurses read the urine dipsticks, and the β-OHB meter (Precision Xtra) is also sold for home use. Patient self-testing accuracy was not studied.

Groups: `insulin_dependence` (type 1 diabetes implies insulin use); `ketone_test` (two tests of the same ketosis).

Prior: p = 0.204. Yan 2025 Table 3: final ED diagnosis of DKA in 134 of 657 (20.4%) visits. Status: PLACEHOLDER (DS-5).

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 30 | Untreated DKA can cause death. Same-day ED care when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day ED visit. |
| test_se | 0.99 | Illustrative sensitivity of ED blood tests (venous pH, bicarbonate, anion gap, ketones). Not sourced. |
| test_sp | 0.95 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit and blood tests. |

The engine calculates T_test = 0.0034 and T_treat = 0.720.

### Hyperosmolar hyperglycemic state (cannot-miss)

Prior: p = 0.041. Yan 2025 Table 3: final ED diagnosis of HHS in 27 of 657 (4.1%) visits. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

Thresholds (illustrative): B = 50, R = 1, test_se = 0.95, test_sp = 0.95, test_harm = 0.05. The engine calculates T_test = 0.0021 and T_treat = 0.261. The prior is in the middle zone and there are no remote features, so the engine defers every hyperglycemia encounter.

### Hyperglycemia without DKA or HHS

The Peamyao LRs are DERIVED as reciprocals, because simple hyperglycemia is the exact complement of DKA in that study. The Arora LRs are DERIVED as reciprocals of the no-DKA group, which can include HHS. Values: `vomiting_or_belly_pain` 0.61 / 1.27; `trouble_breathing` 0.45 / 2.64; `fever` 0.78 / 1.10; `previous_dka` 0.17 / 1.28; `uses_insulin` 0.42 / 2.33; `type_1_diabetes` 0.10 / 1.15; `missed_diabetes_medicines` 0.59 / 2.22; `urine_ketones_positive` 0.66 / 18.94; `blood_ketone_over_1_5` 0.22 / 42.43. The YAML carries the reciprocal CIs.

Prior: p = 0.709. Yan 2025 Results: final ED diagnosis "hyperglycemia/diabetes" in 70.9% of 657 visits. Status: PLACEHOLDER (DS-5).

### Engine behavior (hyperglycemia)

With no findings, `step` returns DEFER with `cannot_miss_middle_zone_no_remote_test` (HHS). Smoke tests: vomiting and trouble breathing give DKA p = 0.48; a negative blood ketone test with no vomiting and no trouble breathing gives DKA p = 0.0018 (p95 0.014). Both defer because of HHS. The script cannot close an encounter remotely until sourced HHS LRs are added or the reviewer changes the HHS thresholds.

## Early-pregnancy pain or bleeding script

Population: a person with a positive pregnancy test, or possible pregnancy, in the first trimester, with pelvic pain or vaginal bleeding and no known pregnancy location. The LRs come from Mimoun 2016: women in five French hospitals who filled in a self-assessment questionnaire on arrival at a gynecologic ED and were then hospitalized. The training sample had 97 ectopic and 77 intrauterine pregnancies (ectopic prevalence 56%, a selected population).

### Ectopic pregnancy (cannot-miss)

Mimoun 2016 Table 1 ("Diagnostic performances of items of the SAQ-GE (p<0,1) associated with EP"). The table gives LR+ and LR− to one decimal place with no CIs.

| Feature | Source row | LR+ | LR− | Remote | Status |
|---|---|---|---|---|---|
| `unilateral_pelvic_pain` | Unilateral pelvic pain: Yes (Se 67.0, Sp 61.1) | 1.7 | 0.5 | yes | VERIFIED |
| `pain_with_cough` | Pain during coughing: Yes (Se 49.5, Sp 72.6) | 1.8 | 0.7 | yes | VERIFIED |
| `bleeding_over_24h` | Duration of bleeding > 24 hours (Se 48.9, Sp 76.7) | 2.1 | 0.7 | yes | VERIFIED |
| `brown_discharge` | Brown discharge: Yes (Se 48.9, Sp 81.3) | 2.6 | 0.6 | yes | VERIFIED |
| `anal_pain` | Anal pain: Yes (Se 18.9, Sp 95.9) | 4.6 | 0.8 | yes | VERIFIED |
| `heavy_bleeding` | Frequent need to change sanitary towels: No (LR+ 1.3, LR− 0.4), inverted | 0.4 | 1.3 | yes | DERIVED |

Inversion. The source item is "no frequent need to change sanitary towels". A patient who does need frequent changes has the "No" item absent, so `heavy_bleeding` present takes the source LR− (0.4) and `heavy_bleeding` absent takes the source LR+ (1.3).

Feature selection. `unilateral_pelvic_pain`, `pain_with_cough`, `bleeding_over_24h`, `brown_discharge`, and `heavy_bleeding` are the five items that stayed in the Mimoun multivariable model (adjusted diagnostic odds ratios 2.7 to 6.1). We kept anal pain (univariate LR+ 4.6) as a rule-in red flag. We left out the other univariate items (pain during movement, never experienced such pain before, sudden onset, evacuation of clots, evacuation of membranes, vomiting absent or unique, and others in Table 1), because they did not stay in the model. An earlier draft had all 11 items. In a smoke test with every answer reassuring and tissue passed, the product of the univariate LRs moved ectopic pregnancy to p = 0.0011, below T_test. The validated score does not support that much reduction: Mimoun Table 3 gives score < 25 an LR− of 0.2 (0.1-0.5) in the training sample. With six features, the lowest reachable p is 0.0038, which is above T_test. No group is set, because the model treated the five items as independent. The reviewer can add the SAQ-GE score (score < 25: LR− 0.2 [0.1-0.5]; score > 70: LR+ 12.3 [3.0-49.8], Mimoun Table 3, training sample) as a calculated feature if the extractor can produce it.

Prior: p = 0.075. Stein 2010 abstract: "a total of 2,057 patients, of whom 152 (7.5%) had ectopic pregnancy" in ED patients at risk for ectopic pregnancy (10 studies). Status: PLACEHOLDER (DS-5).

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 100 | A ruptured ectopic pregnancy can cause death. Same-day evaluation when it is present has a very large net benefit. |
| harm R | 1 | One unnecessary same-day visit. |
| test_se | 0.993 | Stein 2010 abstract: pooled sensitivity 99.3% (96.6%-100%) of emergency physician ultrasonography for ectopic pregnancy (no intrauterine pregnancy seen). Sourced, but the choice of this test is illustrative. |
| test_sp | 0.9 | Illustrative. The abstract does not give specificity. |
| test_harm | 0.05 | Burden of the visit, ultrasonography, and hCG test. |

The engine calculates T_test = 0.0015 and T_treat = 0.531.

### Miscarriage (threatened, incomplete, or complete)

Prior: p = 0.56. Fisher 2024 Results: "Pregnancy outcome data were available for 192 pregnancies; 107 (56%) experienced a miscarriage", among 200 women with vaginal bleeding in early pregnancy at three Canadian EDs. Fisher excluded hemodynamically unstable women and women with heavy bleeding. Status: PLACEHOLDER (DS-5).

LRs: none. The Mimoun comparison group is all intrauterine pregnancies, including viable ones, so its LRs do not apply to miscarriage.

### Engine behavior (early pregnancy)

With no findings, `step` returns ASK for `heavy_bleeding` and `brown_discharge`. Smoke tests: unilateral pain, pain on coughing, and anal pain give p = 0.53 and ESCALATE. All remote answers reassuring with heavy bleeding give p = 0.0038 and DEFER (`cannot_miss_middle_zone_no_remote_test`). The script does not rule out ectopic pregnancy remotely, which agrees with the need for ultrasonography and hCG testing in practice. The reviewer must confirm this.

## First-step behavior of all scripts (no findings)

| Script | `step` result |
|---|---|
| `adult_fever` | ASK `jolt_headache`, `poor_food_intake` |
| `gi_bleeding` | ASK `melena_history`, `clots_in_stool` |
| `hyperglycemia_symptoms` | DEFER (`cannot_miss_middle_zone_no_remote_test`, HHS) |
| `pelvic_pain_bleeding_possible_pregnancy` | ASK `heavy_bleeding`, `brown_discharge` |

## Value counts

| Script | LR entries VERIFIED | LR entries DERIVED | Priors (PLACEHOLDER) | Threshold sets (PLACEHOLDER) |
|---|---|---|---|---|
| `gi_bleeding` | 10 | 8 | 4 (1 derived product) | 2 |
| `adult_fever` | 4 (jolt CI derived) | 7 | 3 (1 derived sum) | 2 |
| `hyperglycemia_symptoms` | 0 | 18 | 3 | 2 |
| `pelvic_pain_bleeding_possible_pregnancy` | 5 | 1 | 2 | 1 |
| Total | 19 | 34 | 12 | 7 |

## Unverified and omitted

| Item | Reason |
|---|---|
| Srygley 2012 JAMA tables (direct read) | [UNVERIFIED — check manually]. We could not open the JAMA full text. The LR+ values with CIs for melena range, clots, BUN:Cr, tachycardia, and Blatchford 0 are in the abstract that we read. The other values come from the 2015 Springer reproduction (PMC7123601). The reviewer must check each row against JAMA 2012;307(10):1072-1079. |
| Melenic stool on examination (LR 25), nasogastric lavage findings, hemoglobin < 8 g/dL (LR+ range 4.5-6.2), BUN > 90 mg/dL, history of malignancy or cirrhosis (Srygley) | [UNVERIFIED — omitted]. These are exam, procedure, or lab findings with no remote use, or a range with no single value, or (malignancy or cirrhosis) a feature that duplicates `cirrhosis`. |
| Glasgow-Blatchford history items: cardiac failure, hepatic disease as separate items | [UNVERIFIED — omitted]. We found no paired LR for cardiac failure. Hepatic disease is covered by `cirrhosis`. |
| Hemorrhoidal bleeding LRs (bright red blood on paper, anal pain or itch) | [UNVERIFIED — omitted]. We found no diagnostic-accuracy study that compares hemorrhoidal bleeding with other causes of rectal bleeding by history. |
| Colorectal cancer, inflammatory bowel disease, anal fissure as diagnoses | [UNVERIFIED — omitted]. Olde Bekkink 2010 (PMC2813743) and Jellema 2010 (PMC2848719) concern cancer in rectal bleeding; not read to a table. Not acute cannot-miss for this lane. |
| Sepsis as a diagnosis; qSOFA and NEWS validation (Seymour CW et al. Assessment of clinical criteria for sepsis. *JAMA*. 2016;315(8):762-774. PMID 26903335. doi:10.1001/jama.2016.0288; abstract read) | [UNVERIFIED — omitted]. qSOFA (and NEWS, not read) predicts death or ICU stay among patients with suspected infection. They do not give LRs for the presence of sepsis. Respiratory rate and mental-status exam are not reliable by self-report. Komatsu 2025 gives qSOFA ≥ 2 LRs for bacteremia, which the script uses with `remote_askable: false`. |
| Coburn B et al. Does this adult patient with suspected bacteremia require blood cultures? *JAMA*. 2012;308(5):502-511. PMID 22851117 | [UNVERIFIED — omitted]. We read the abstract only. It gives LR+ for temperature ≥ 38 °C (1.9 [1.4-2.4]) and shaking chills (4.7 [3.0-7.2]) with no LR−. The schema needs both. |
| Measured temperature (home thermometer) as a feature for bacteremia | [UNVERIFIED — omitted]. Komatsu reports body temperature as a continuous value only. Coburn gives no LR−. |
| Respiratory rate ≥ 22 | [UNVERIFIED — omitted]. Not reliably self-measured; no remote-validated source. |
| Attia J et al. The rational clinical examination: does this adult patient have acute meningitis? *JAMA*. 1999;282(2):175-181. PMID 10411200 | [UNVERIFIED — omitted]. Abstract only. It gives jolt accentuation LR+ 2.2 and LR− 0 (LR− 0 fails the schema), and sensitivities with no specificities for headache (50%) and nausea or vomiting (30%). |
| Neck stiffness, Kernig and Brudzinski signs | [UNVERIFIED — omitted]. Exam signs; Akaishi 2019 (PMC6732499) pools them as odds ratios only. Self-reported stiff neck was not studied. Put stiff neck and a purple rash in the lane gate as hard escalation rules. |
| Self-reported normal food consumption, excluding blood cultures drawn 10 pm to 8 am (Komatsu LR− 0.32) | [UNVERIFIED — omitted]. A subgroup value. The script uses the all-patient value. |
| HHS LRs (confusion, very high meter reading, age, type 2 diabetes) | [UNVERIFIED — omitted]. We found no study with paired accuracy data for HHS compared with other hyperglycemia. French 2026 (PMC13331110, a systematic review) and Fujiya 2025 (PMC12532513) describe HHS cases only. |
| Home glucose meter value ("HI" or > 600 mg/dL) for DKA or HHS | [UNVERIFIED — omitted]. Peamyao reports capillary glucose as a continuous value with a risk ratio only. Put a meter reading of "HI" in the lane gate. |
| Capillary β-OHB > 2 mmol/L cutoff (Arora: sensitivity 98.1%, specificity 82.3%) | [UNVERIFIED — omitted]. The script uses the manufacturer cutoff (> 1.5 mmol/L) that the study used as its primary result. |
| Euglycemic DKA (SGLT2 inhibitors) | [UNVERIFIED — omitted]. Not studied in the sources. Put SGLT2-inhibitor use in the lane gate. |
| Crochet JR et al. Does this woman have an ectopic pregnancy? *JAMA*. 2013;309(16):1722-1729. PMID 23613077 | [UNVERIFIED — omitted]. Abstract only. It states that all history components had LR+ < 1.5 and gives exam LR+ values (cervical motion tenderness 4.9 [1.7-14]; adnexal mass 2.4 [1.6-3.7]; adnexal tenderness 1.9 [1.0-3.5]) with no LR−. |
| Mimoun 2016 univariate items not in the multivariable model (pain during movement, new kind of pain, sudden onset, evacuation of clots, evacuation of membranes, vomiting absent or unique, diffuse pain, lumbar pain, fatigue, and others) | [UNVERIFIED — omitted]. Read, but left out because they did not add independent information in the model (see "Feature selection"). "Vomiting absent or unique" (LR− 0.1 for repeated vomiting) would lower ectopic probability strongly on a small sample, which is not safe for a cannot-miss diagnosis. |
| Fainting, shoulder-tip pain, dizziness, soaking ≥ 1 pad per hour, prior ectopic pregnancy, IUD in place, fertility treatment | [UNVERIFIED — omitted]. No paired remote LRs read. Put the hemodynamic items in the lane gate as hard escalation rules. |
| Feature `cost`, `harm`, `leak` | Not set (defaults). No fee-schedule or leak source was given. The engine calculates the leak from the LRs. |
