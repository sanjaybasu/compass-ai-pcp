# Illness-script sources

This file lists the source of each number in these two scripts:

- `compass_pcp/data/scripts/dysuria.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/sore_throat.yaml` (version 0.1.0-draft)

Both scripts are drafts for physician sign-off. `clinical_review.approved_by` is null in both files.

Status labels:

- **VERIFIED.** The value is copied from a table that we read in the source article.
- **DERIVED.** We calculated the value from counts or estimates in a table that we read. The calculation is given.
- **PLACEHOLDER.** The value is a literature value that a Waymark claims rate (DS-5) or a CPD decision-analysis memo must replace.
- **[UNVERIFIED — omitted].** We did not put the value in a script.

We calculated derived 95% CIs for likelihood ratios (LRs) with the log method (Simel DL, Samsa GP, Matchar DB. Likelihood ratios with confidence: sample size estimation for diagnostic test studies. *J Clin Epidemiol*. 1991;44(8):763-770. PMID 1941027): $SE(\ln LR^{+}) = \sqrt{1/a - 1/(a+c) + 1/b - 1/(b+d)}$, where $a$ is true positives, $c$ is false negatives, $b$ is false positives, and $d$ is true negatives. We calculated $LR^{-}$ in the same way.

## Sources that we read

| Key | Citation | Access |
|---|---|---|
| Bent 2002 | Bent S, Nallamothu BK, Simel DL, Fihn SD, Saint S. Does this woman have an acute uncomplicated urinary tract infection? *JAMA*. 2002;287(20):2701-2710. PMID 12020306. doi:10.1001/jama.287.20.2701 | Full-text PDF reprint, Tables 2 and 3 and Results text |
| Tomas 2015 | Tomas ME, Getman D, Donskey CJ, Hecker MT. Overdiagnosis of urinary tract infection and underdiagnosis of sexually transmitted infection in adult women presenting to an emergency department. *J Clin Microbiol*. 2015;53(8):2686-2692. PMID 26063863. doi:10.1128/JCM.00670-15 | PMC4508438, Tables 1 to 4 |
| Fernández-García 2025 | Fernández-García S, Moragas A, Giner-Soriano M, Morros R, Ouchi D, García-Sangenís A, Llor C. Urinary tract infections in women in Catalonia, Spain: a population-based observational cohort study in primary care. *Front Pharmacol*. 2025;16:1593910. PMID 40994650. doi:10.3389/fphar.2025.1593910 | PMC12455073, Table 1 |
| Aalbers 2011 | Aalbers J, O'Brien KK, Chan WS, Falk GA, Teljeur C, Dimitrov BD, Fahey T. Predicting streptococcal pharyngitis in adults in primary care: a systematic review of the diagnostic accuracy of symptoms and signs and validation of the Centor score. *BMC Med*. 2011;9:67. PMID 21631919. doi:10.1186/1741-7015-9-67 | PMC3127779, Tables 2 and 3 and Background text |
| Voruz 2025 | Voruz F, Revol R, Combescure C, Monnier Y, Becker M, Dulguerov N. Diagnosis of peritonsillar abscess: a prospective study comparing clinical with CT findings in 133 consecutive patients. *Diagnostics (Basel)*. 2025;15(2):228. PMID 39857112. doi:10.3390/diagnostics15020228 | PMC11765337, Tables 1 to 3 (the LR supplement did not download) |
| Little 2013 | Little P, Stuart B, Hobbs FDR, et al. Predictors of suppurative complications for acute sore throat in primary care: prospective clinical cohort study. *BMJ*. 2013;347:f6867. PMID 24277339. doi:10.1136/bmj.f6867 | PMC3898431, Table 1 |

## Dysuria script

Population: non-pregnant women aged 18 to 64 with dysuria. The lane gate handles pregnancy, including possible ectopic pregnancy, as an eligibility exclusion. We found no LRs for ectopic pregnancy in a dysuria population, so ectopic pregnancy is not a candidate diagnosis.

### Uncomplicated cystitis (UTI)

Bent 2002 defines UTI as a culture of at least 10^2 to 10^5 CFU/mL of one uropathogen. The script uses UTI for the cystitis diagnosis. All LRs below are the "Summary" rows of Bent 2002 Table 2 ("Clinical Signs and Symptoms in the Prediction of Urinary Tract Infection"), pages 2705-2706.

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `dysuria` | 1.5 (1.2-2.0) | 0.5 (0.3-0.7) | irritative_voiding | yes | VERIFIED |
| `urinary_frequency` | 1.8 (1.1-3.0) | 0.6 (0.4-1.0) | irritative_voiding | yes | VERIFIED |
| `hematuria` | 2.0 (1.3-2.9) | 0.9 (0.9-1.0) | none | yes | VERIFIED |
| `back_pain` | 1.6 (1.2-2.1) | 0.8 (0.7-0.9) | back_flank | yes | VERIFIED |
| `flank_pain` | 1.1 (0.9-1.4) | 0.9 (0.8-1.1) | back_flank | yes | VERIFIED |
| `lower_abdominal_pain` | 1.1 (0.9-1.4) | 0.9 (0.8-1.1) | none | yes | VERIFIED |
| `fever` | 1.6 (1.0-2.6) | 0.9 (0.9-1.0) | none | yes | VERIFIED |
| `vaginal_discharge` (history) | 0.3 (0.1-0.9) | 3.1 (1.0-9.3) | vaginal_sx | yes | VERIFIED |
| `vaginal_irritation` (history) | 0.2 (0.1-0.9) | 2.7 (0.9-8.5) | vaginal_sx | yes | VERIFIED |
| `cva_tenderness_exam` | 1.7 (1.1-2.5) | 0.9 (0.8-1.0) | none | no (in-person exam) | VERIFIED |
| `vaginal_discharge_exam` | 0.7 (0.5-0.9) | 1.1 (1.0-1.2) | none | no (in-person exam) | VERIFIED |
| `dipstick_le_or_nitrite` | 4.2 (no CI) | 0.3 (no CI) | none | no (office test) | VERIFIED (Bent cites Hurlbut and Littenberg; no CI) |

Prior: p = 0.48. Bent 2002 Results text gives the summary prevalence of UTI in 5 studies of symptomatic women as 48% (95% CI, 41%-55%). Status: PLACEHOLDER (DS-5).

Groups:

- `irritative_voiding` (dysuria, frequency). The task brief asks for these to share a group. Bent 2002 Table 3 multiplies the dysuria and frequency LRs as if independent. With the group, only the stronger finding counts, which is the conservative choice. The reviewer can remove the group to follow Bent Table 3.
- `vaginal_sx` (vaginal discharge, vaginal irritation). Bent 2002 Table 3 uses "0.3 or 0.2" for these, which treats them as one finding.
- `back_flank` (back pain, flank pain). These overlap in patient report.

Fever and hematuria have no group. Their overlap with other findings is not reported.

### Pyelonephritis (cannot-miss)

Prior: p = 0.035. Fernández-García 2025 Table 1 ("Sociodemographic characteristics of patients diagnosed with UTI") gives 29,586 of 852,116 women with a primary-care UTI diagnosis (3.5%) as pyelonephritis and 822,530 (96.5%) as cystitis. The denominator is women with a recorded UTI. It is not all women with dysuria, so the value is high for this population. A high prior is the conservative direction for a cannot-miss diagnosis. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

Thresholds (illustrative, source string "PLACEHOLDER: CPD decision-analysis memo; illustrative values"):

| Input | Value | Reason |
|---|---|---|
| benefit B | 30 | An untreated pyelonephritis can cause sepsis and hospital admission. Same-day in-person care when it is present has a large net benefit. |
| harm R | 1 | The unit of harm is one unnecessary same-day in-person visit when pyelonephritis is absent. |
| test_se | 0.9 | Illustrative sensitivity of an in-person evaluation (exam, urinalysis, urine culture). Not sourced. |
| test_sp | 0.8 | Illustrative specificity of the same evaluation. Not sourced. |
| test_harm | 0.05 | Burden of the visit and the urine tests. |

The engine calculates T_test = 0.0092 and T_treat = 0.197. The prior (0.035) is between the two thresholds. Because the diagnosis has no remote features, the engine returns DEFER with `cannot_miss_middle_zone_no_remote_test` for every dysuria encounter. The dysuria lane cannot close an encounter remotely until sourced LRs for pyelonephritis are added or the reviewer changes the thresholds.

### Sexually transmitted infection, including cervicitis or PID (cannot-miss)

Tomas 2015 counts chlamydia, gonorrhea, and trichomoniasis (urine NAAT) as STI. The script uses the same definition.

Prior: p = 0.26. Tomas 2015 Table 3 ("Urine culture and STI test results stratified by symptoms") gives a positive STI test in 42 of 161 (26%) women with at least one UTI-related symptom in an urban academic ED. UTI-related symptoms are dysuria, frequency, urgency, hematuria, other urinary symptoms, suprapubic pain, and flank pain. The cohort included 24 of 264 (9%) pregnant women (Table 1). Status: PLACEHOLDER (DS-5).

| Feature | LR+ (95% CI) | LR− (95% CI) | Remote | Status |
|---|---|---|---|---|
| `any_vaginal_symptom` | 1.95 (1.46-2.61) | 0.42 (0.25-0.71) | yes | DERIVED |

Derivation. Tomas 2015 Table 3 gives an STI in 42 of 161 women with at least one UTI-related symptom and in 11 of 85 women with UTI-related symptoms but no vaginal symptoms. Thus 31 of 76 women with vaginal symptoms had an STI. The 2x2 table is: TP = 31, FN = 11, FP = 45, TN = 74. Sensitivity is 0.738 and specificity is 0.622. Tomas defines vaginal symptoms as vaginal discharge, abnormal vaginal bleeding, vaginal itching, and vaginal lesions. Two cautions apply. First, the paper counts women with no documented vaginal symptoms (77 of 264) as having none. Second, the same cell (11/85) appears in two rows of Table 3, which can be a typesetting error. The reviewer should check the published PDF.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 10 | Treatment of a present STI prevents PID, infertility, and transmission to partners. |
| harm R | 1 | One unnecessary antibiotic course and the related visit. |
| test_se | 0.95 | Illustrative sensitivity of a NAAT on a self-collected vaginal swab. Not sourced. |
| test_sp | 0.99 | Illustrative specificity of the NAAT. Not sourced. |
| test_harm | 0.02 | Burden of a self-collected swab. |

The engine calculates T_test = 0.0032 and T_treat = 0.651. One remote feature is available, and its absence (LR− 0.42) cannot move the prior below T_test. The engine therefore defers to NAAT testing for this diagnosis. We think that this agrees with screening practice for sexually active women with dysuria. The reviewer must confirm this.

### Vaginitis, non-STI (bacterial vaginosis or candidiasis)

Prior: p = 0.23. Tomas 2015 Table 2 ("Laboratory test results") gives clue cells (at least 20%) in 25 of 110 tested women (23%) and yeast in 13 of 111 tested women (12%). Only the women that clinicians tested are in these counts. Thus the numbers have selection bias, and the overlap between the two conditions is not reported. Trichomoniasis is in the STI diagnosis, not here. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted". Because the posterior stays at 0.23, its entropy (0.54 nats) is more than the default limit (eta = 0.5). This also stops the engine from closing a dysuria encounter.

## Sore-throat script

Population: adults with acute sore throat (URI lane).

### Group A streptococcal pharyngitis

All LRs are from Aalbers 2011 Table 2 ("Summary estimates of sensitivity, specificity, positive likelihood ratio (LR) and negative LR calculated for signs and symptoms using a bivariate random effects model"). The reference standard is throat culture, and the population is primary-care and ED adults older than 14 years.

| Feature | LR+ (95% CI) | LR− (95% CI) | Studies, patients | Group | Remote | Status |
|---|---|---|---|---|---|---|
| `no_cough` | 1.46 (1.28-1.66) | 0.53 (0.46-0.61) | 19, 4,653 | centor | yes | VERIFIED |
| `fever_history` | 1.65 (1.40-1.95) | 0.71 (0.64-0.80) | 21, 4,635 | centor | yes | VERIFIED |
| `tender_anterior_cervical_nodes` | 1.65 (1.41-1.92) | 0.56 (0.41-0.76) | 16, 4,144 | centor | yes, guided self-exam | VERIFIED |
| `tonsillar_exudate` ("any exudates") | 2.20 (1.76-2.74) | 0.58 (0.47-0.72) | 21, 4,839 | centor | yes, guided self-exam | VERIFIED |

The source studies measured fever and exudate on clinician exam, and they used fever cut-offs of 37.5 °C to 38.5 °C (Table 2 footnote a). The script asks for a fever history and uses guided self-exams for exudate and lymph nodes. The accuracy of patient self-inspection was not measured in these studies. The reviewer can set `remote_askable: false` for `tonsillar_exudate` and `tender_anterior_cervical_nodes` if the self-exams are not accepted.

Group `centor`. Aalbers 2011 Table 3 gives these Centor score LRs: score of 1 or more, LR+ 1.16 (1.08-1.25), LR− 0.27 (0.16-0.46); score of 2 or more, LR+ 1.76 (1.51-2.07), LR− 0.37 (0.29-0.48); score of 3 or more, LR+ 2.68 (1.92-3.75), LR− 0.62 (0.52-0.74); score of 4, LR+ 3.85 (2.05-7.24), LR− 0.86 (0.78-0.93). The product of the four single LR+ values is about 8.7, which is more than the score-4 LR+ of 3.85. Thus the signs are not independent. With the group, only the strongest sign counts, so the maximum LR+ is 2.20. The Centor-score LRs are not features, because a score is not a patient question. The reviewer can add a calculated score feature if the extractor can produce one.

Prior: p = 0.10. The Aalbers 2011 Background text gives a GABHS prevalence of 5% to 10% in adults (it cites another source). We used the upper value. Status: PLACEHOLDER (DS-5).

### Non-group-A-strep sore throat (viral pharyngitis or URI, or other)

Definition: the complement of GABHS in the Aalbers 2011 studies (throat culture negative for GABHS). For a binary partition, $LR^{+}_{\text{non-GAS}} = 1/LR^{+}_{\text{GAS}}$ and $LR^{-}_{\text{non-GAS}} = 1/LR^{-}_{\text{GAS}}$. The CI limits are the reciprocals of the CI limits.

| Feature | LR+ (95% CI) | LR− (95% CI) | Status |
|---|---|---|---|
| `no_cough` | 0.68 (0.60-0.78) | 1.89 (1.64-2.17) | DERIVED |
| `fever_history` | 0.61 (0.51-0.71) | 1.41 (1.25-1.56) | DERIVED |
| `tender_anterior_cervical_nodes` | 0.61 (0.52-0.71) | 1.79 (1.32-2.44) | DERIVED |
| `tonsillar_exudate` | 0.45 (0.36-0.57) | 1.72 (1.39-2.13) | DERIVED |

Prior: p = 0.90, the complement of the GABHS prior. Status: PLACEHOLDER (DS-5).

### Peritonsillar abscess (cannot-miss)

Prior: p = 0.0035. Little 2013 Table 1 gives quinsy within 1 month of the index visit in 11 of 4,974 (no antibiotics), 30 of 5,932 (immediate antibiotics), and 6 of 2,382 (delayed antibiotics) adults with acute sore throat in UK primary care. The total is 47 of 13,288 (0.4%). The script uses the unrounded proportion, 0.0035. This value is the incidence after a primary-care visit. It is not the prevalence at the visit, so it can be low for a population that writes in by text. Status: PLACEHOLDER (DS-5).

LRs: all DERIVED from Voruz 2025 Table 2 ("Test data and odds ratios for the association with peritonsillar abscess (PTA)"). The sensitivities and specificities agree with Table 3. The population is 133 adults with suspected PTA in a tertiary ED (117 with PTA, 16 without). An otolaryngologist did the exam. The reference standard was pus at surgery or a favorable course at 48 hours. Voruz reports the LRs in a supplement that did not download, so we calculated them from the counts.

| Feature | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Remote |
|---|---|---|---|---|---|---|---|
| `trismus` (mouth opening less than 2 cm) | 23 | 94 | 1 | 15 | 3.15 (0.46-21.73) | 0.86 (0.73-1.00) | yes, guided two-finger self-test |
| `muffled_voice` (hot potato voice) | 47 | 70 | 5 | 11 | 1.29 (0.60-2.75) | 0.87 (0.61-1.25) | yes, patient or family report |
| `uvula_deviation` | 69 | 48 | 5 | 11 | 1.89 (0.90-3.96) | 0.60 (0.40-0.89) | no, in-person exam |
| `pharynx_immobility` | 77 | 40 | 7 | 9 | 1.50 (0.85-2.66) | 0.61 (0.37-1.00) | no, in-person exam |

Three cautions apply. First, these LRs come from a population with suspected PTA and a prevalence of 88%. Spectrum effects make them weak for a general sore-throat population. Second, no sign had a statistically significant association with PTA in Voruz 2025. Third, the sample had only 16 patients without PTA, so the CIs are wide. All four signs share group `pta_signs`, because each sign comes from the same peritonsillar mass.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 100 | A missed PTA can cause airway obstruction or spread to the deep neck spaces. Same-day in-person care when it is present has a very large net benefit. |
| harm R | 1 | One unnecessary same-day in-person visit. |
| test_se | 0.974 | Voruz 2025 Table 3, "overall clinical impression" sensitivity 114/117 (97.4%), used as the in-person exam. |
| test_sp | 0.125 | Voruz 2025 Table 3, "overall clinical impression" specificity 2/16 (12.5%). |
| test_harm | 0.02 | Burden of the visit. |

The test_se and test_sp values are from a source, but the YAML source string is the required placeholder, because the choice of the in-person exam as the reference test is an illustrative decision. The engine calculates T_test = 0.0091 and T_treat = 0.0385. The prior (0.0035) is below T_test, so with no findings the engine marks PTA as ruled out and does not ask about it. In a smoke run, `trismus` present (confirmed) gave p = 0.011 and p95 = 0.058, and the engine returned ESCALATE. A `muffled_voice` finding alone did not change the outcome (p95 = 0.008).

### Engine behavior with these numbers

With no findings, the sore-throat script returns COMPLETE. The GABHS prior (0.10) has an entropy of 0.33 nats, which is less than the default limit (eta = 0.5), and PTA is below T_test. The reviewer must decide if this is acceptable or if the lane must ask a minimum set of red-flag questions first.

## Unverified and omitted

| Item | Reason |
|---|---|
| Pyelonephritis LRs for fever, flank pain, chills, nausea or vomiting, CVA tenderness, compared with other causes of dysuria | [UNVERIFIED — omitted]. A PubMed search found no diagnostic-accuracy study of these findings for pyelonephritis in women with urinary symptoms. The Bent 2002 fever and back-pain LRs are for UTI compared with no UTI, so they do not apply to pyelonephritis. Soler JK, Corrigan D, Kazienko P, et al. Evidence-based rules from family practice to inform family practice; the learning healthcare system case study on urinary tract infections. *BMC Fam Pract*. 2015;16:63 (PMID 25980623, doi:10.1186/s12875-015-0271-4), Additional file 3 (Table 2), gives LR+ for the "pyelonephritis" episode against all primary-care episodes (combined data: flank/axilla complaint 59.60, fever 9.00). It has the wrong comparison group and gives no LR−, so we did not use it. |
| Vaginitis LRs (itching, odor, discharge) | [UNVERIFIED — omitted]. Anderson MR, Klink K, Cohrssen A. Evaluation of vaginal complaints. *JAMA*. 2004;291(11):1368-1379 (PMID 15026404, doi:10.1001/jama.291.11.1368) has the relevant tables. We could not get the full text. The abstract gives only the LR for absent findings (for example, no itching for candidiasis, LR range 0.18 to 0.79; no perceived odor for bacterial vaginosis, LR 0.07 [0.01-0.51]). The schema needs LR+ and LR− for each feature. |
| Self-diagnosis of UTI (Bent 2002 Table 2, Gupta et al: LR+ 4.0 [2.9-5.5], LR− 0.0) | [UNVERIFIED — omitted]. The LR− of 0.0 does not pass the schema (LR must be more than 0). The source population had recurrent UTI only. |
| Urgency for UTI | [UNVERIFIED — omitted]. Bent 2002 does not report urgency. |
| Ectopic pregnancy or pregnancy-related causes | [UNVERIFIED — omitted]. We found no LRs in a dysuria population. The lane gate handles pregnancy as an eligibility exclusion (YAML comment). |
| New or multiple sex partners, partner with STI symptoms, for STI | [UNVERIFIED — omitted]. Not searched to a table with paired LRs. |
| Exposure to strep throat in the past 2 weeks (Ebell 2000) | [UNVERIFIED — omitted]. Ebell MH et al. The rational clinical examination: does this patient have strep throat? *JAMA*. 2000;284(22):2912-2918 (PMID 11147989, doi:10.1001/jama.284.22.2912). The abstract gives LR+ 1.9 but no LR−, and we could not get the full-text table. Ebell 2000 abstract values for tonsillar exudate (LR+ 3.4), pharyngeal exudate (LR+ 2.1), and absence of tender nodes (LR− 0.60) were not used, because Aalbers 2011 gives paired values with CIs from a larger meta-analysis. |
| McIsaac score (age modifier) | [UNVERIFIED — omitted]. No validation table read. |
| Epiglottitis / supraglottitis | [UNVERIFIED — omitted]. No diagnostic-accuracy study with a comparison group found. Put red flags (drooling, stridor, cannot swallow saliva, trouble breathing) in the lane gate as hard escalation rules. |
| Deep neck space infection (parapharyngeal, retropharyngeal) | [UNVERIFIED — omitted]. Voruz 2025 excluded these patients. |
| Unilateral throat pain, Liverpool Peritonsillar abscess Score items (Lau AS et al. *Clin Otolaryngol*. 2019;44(3):293-298, PMID 30663235) | [UNVERIFIED — omitted]. The abstract gives odds ratios for the score only. We did not read the full text. |
| Feature `cost`, `harm`, `leak` | Not set (defaults). No fee-schedule or leak source was given. The engine calculates the leak from the LRs. |
