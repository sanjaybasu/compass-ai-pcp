# Illness-script sources: cardiopulmonary high-risk complaints

This file lists the source of each number in these four scripts:

- `compass_pcp/data/scripts/chest_pain.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/dyspnea.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/leg_swelling.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/syncope.yaml` (version 0.1.0-draft)

All four scripts use lane `undifferentiated_high_risk`. They are drafts for physician sign-off. `clinical_review.approved_by` is null in all four files. In this lane the AI takes the history and escalates. The main job of each script is to cover the cannot-miss diagnoses. Features that need an exam, an ECG, a blood test, or imaging have `remote_askable: false`, so the engine defers when a cannot-miss diagnosis stays in the middle zone.

Status labels:

- **VERIFIED.** We copied the value from a table or the abstract text of the source article, and we read that table or text.
- **VERIFIED (secondary).** We copied the value from a table in a review that we read. The review attributes the value to a primary article that we did not read. The primary article is named.
- **DERIVED.** We calculated the value from counts or estimates in a table that we read. The calculation is given.
- **PLACEHOLDER.** The value is a literature value that a Waymark claims rate (DS-5) or a CPD decision-analysis memo must replace.
- **[UNVERIFIED — omitted].** We did not put the value in a script.

We calculated derived 95% CIs for likelihood ratios (LRs) with the log method (Simel DL, Samsa GP, Matchar DB. Likelihood ratios with confidence: sample size estimation for diagnostic test studies. *J Clin Epidemiol*. 1991;44(8):763-770. PMID 1941027): $SE(\ln LR^{+}) = \sqrt{1/a - 1/(a+c) + 1/b - 1/(b+d)}$, where $a$ is true positives, $c$ is false negatives, $b$ is false positives, and $d$ is true negatives. We calculated $LR^{-}$ in the same way. For a binary partition (one diagnosis and its complement in the same data), $LR^{+}_{\text{complement}} = 1/LR^{+}$ and $LR^{-}_{\text{complement}} = 1/LR^{-}$; we took reciprocals of the unrounded values and their CI limits.

Every cannot-miss threshold is a decision-analysis input with the YAML source string "PLACEHOLDER: CPD decision-analysis memo; illustrative values". Benefit B is the net benefit of same-day in-person or ED care when the diagnosis is present. Harm R = 1 is the unit harm of one unnecessary same-day visit when the diagnosis is absent. test_se, test_sp, and test_harm describe the in-person evaluation that would confirm or exclude the diagnosis. The engine calculates T_test and T_treat with `pauker_kassirer` in `compass_pcp/engine/scripts.py`. No published decision analysis supplied these inputs. The CPD memo must replace them.

Feature `cost`, `harm`, and `leak` are not set in any of the four scripts (defaults). No fee-schedule or leak source was given. The engine calculates the leak from the LRs.

## Sources that we read

| Key | Citation | Access |
|---|---|---|
| Raat 2024 | Raat W, Nees L, Vaes B. Diagnostic accuracy of signs and symptoms in acute coronary syndrome and acute myocardial infarction. *Scand J Prim Health Care*. 2024;43(1):111-119. PMID 39308022. doi:10.1080/02813432.2024.2406266 | PMC11834805, Tables 1 and 2 |
| Bösner 2010 | Bösner S, Becker A, Abu Hani M, et al. Accuracy of symptoms and signs for coronary heart disease assessed in primary care. *Br J Gen Pract*. 2010;60(575):e246-e257. PMID 20529488. doi:10.3399/bjgp10X502137 | Full-text PDF from bjgp.org, Tables 2 and 3, Appendix 1, Results text |
| Haasenritter 2015 | Haasenritter J, Biroga T, Keunecke C, et al. Causes of chest pain in primary care: a systematic review and meta-analysis. *Croat Med J*. 2015;56(5):422-430. PMID 26526879. doi:10.3325/cmj.2015.56.422 | PMC4655927, Tables 1 to 3 |
| Bösner 2009 | Bösner S, Haasenritter J, Becker A, et al. Heartburn or angina? Differentiating gastrointestinal disease in primary care patients presenting with chest pain: a cross sectional diagnostic study. *Int Arch Med*. 2009;2:40. PMID 20003376. doi:10.1186/1755-7682-2-40 | PMC2799444, Tables 1 to 3, Results text |
| Courtney 2010 | Courtney DM, Kline JA, Kabrhel C, et al. Clinical features from the history and physical examination that predict the presence or absence of pulmonary embolism in symptomatic emergency department patients: results of a prospective, multicenter study. *Ann Emerg Med*. 2010;55(4):307-315.e1. PMID 20045580. doi:10.1016/j.annemergmed.2009.11.010 | PMC2847003 (author manuscript, NCBI efetch XML), Tables 1 to 3 and the unnumbered web-appendix table "Univariate association of predictor variable stratified by VTE positive and negative groups" |
| Morello 2020 | Morello F, Bartalucci A, Bironzo M, et al. Prospective diagnostic accuracy study of plasma soluble ST2 for diagnosis of acute aortic syndromes. *Sci Rep*. 2020;10(1):3103. PMID 32080259. doi:10.1038/s41598-020-59884-6 | PMC7033105, Tables 1 and 2, Results text |
| Alter 2015 | Alter SM, Eskin B, Allegra JR. Diagnosis of aortic dissection in emergency department patients is rare. *West J Emerg Med*. 2015;16(5):629-631. PMID 26587083. doi:10.5811/westjem.2015.6.25752 | PMC4644027, Abstract and Results text |
| Wang 2005 | Wang CS, FitzGerald JM, Schulzer M, Mak E, Ayas NT. Does this dyspneic patient in the emergency department have congestive heart failure? *JAMA*. 2005;294(15):1944-1956. PMID 16234501. doi:10.1001/jama.294.15.1944 | Abstract only (full text not available to us) |
| Devroey 2011 | Devroey D, Van Casteren V. Signs for early diagnosis of heart failure in primary health care. *Vasc Health Risk Manag*. 2011;7:591-596. PMID 21966224. doi:10.2147/VHRM.S24476 | PMC3180513, Tables 1 and 2, Methods and Results text |
| Long 2019 | Long B, Koyfman A, Gottlieb M. Diagnosis of acute heart failure in the emergency department: an evidence-based review. *West J Emerg Med*. 2019;20(6):875-884. PMID 31738714. doi:10.5811/westjem.2019.9.43732 | PMC6860389, Table 2 ("History and examination findings in acute heart failure", cites Martindale 2016) |
| Martindale 2016 (not read) | Martindale JL, Wakai A, Collins SP, et al. Diagnosing acute heart failure in the emergency department: a systematic review and meta-analysis. *Acad Emerg Med*. 2016;23(3):223-242. PMID 26910112. doi:10.1111/acem.12878 (metadata checked in Europe PMC) | Not read; values taken from Long 2019 Table 2 |
| Htun 2019 | Htun TP, Sun Y, Chua HL, Pang J. Clinical features for diagnosis of pneumonia among adults in primary care setting: a systematic and meta-review. *Sci Rep*. 2019;9(1):7600. PMID 31110214. doi:10.1038/s41598-019-44145-y | PMC6527561, Tables 1 and 2 with footnotes |
| Frese 2011 | Frese T, Sobeck C, Herrmann K, Sandholzer H. Dyspnea as the reason for encounter in general practice. *J Clin Med Res*. 2011;3(5):239-246. PMID 22383911. doi:10.4021/jocmr642w | PMC3279485, Tables 1, 4, and 5 |
| Heller 2021 | Heller T, Becher M, Kröger JC, et al. Isolated calf deep venous thrombosis: frequency on venous ultrasound and clinical characteristics. *BMC Emerg Med*. 2021;21(1):126. PMID 34717549. doi:10.1186/s12873-021-00516-1 | PMC8557054, Table 1, Methods text |
| Beller 2020 | Beller E, Becher M, Meinel FG, et al. Prevalence and predictors of alternative diagnoses on whole-leg ultrasound negative for acute deep venous thrombosis. *BMC Med Imaging*. 2020;20(1):127. PMID 33267839. doi:10.1186/s12880-020-00527-7 | PMC7709303, Abstract, Tables 1 and 2 |
| Biesheuvel 2008 | Biesheuvel CJ, Vergouwe Y, Oudega R, Hoes AW, Grobbee DE, Moons KG. Advantages of the nested case-control design in diagnostic research. *BMC Med Res Methodol*. 2008;8:48. PMID 18644127. doi:10.1186/1471-2288-8-48 | PMC2500041, Table 1, Methods and Results text |
| Dybowska 2015 | Dybowska M, Tomkowski WZ, Kuca P, Ubysz R, Jóźwik A, Chmielewski D. Analysis of the accuracy of the Wells scale in assessing the probability of lower limb deep vein thrombosis in primary care patients practice. *Thromb J*. 2015;13:18. PMID 26045696. doi:10.1186/s12959-015-0050-4 | PMC4455328, Tables 1 to 4 (Table 4 is the 2x2 table at Wells threshold 2) |
| Berecki-Gisolf 2013 | Berecki-Gisolf J, Sheldon A, Wieling W, et al. Identifying cardiac syncope based on clinical history: a literature-based model tested in four independent datasets. *PLoS One*. 2013;8(9):e75255. PMID 24223233. doi:10.1371/journal.pone.0075255 | PMC3815402, Tables 1 to 3, dataset descriptions |
| Albassam 2019 | Albassam OT, Redelmeier RJ, Shadowitz S, Husain AM, Simel D, Etchells EE. Did this patient have cardiac syncope? The Rational Clinical Examination systematic review. *JAMA*. 2019;321(24):2448-2457. PMID 31237649. doi:10.1001/jama.2019.8001 | Abstract only (full text not available to us) |

We verified each citation (authors, title, journal, year, volume, pages, PMID, DOI) against PubMed or Europe PMC metadata on 2026-10-27.

## Chest-pain script

Population: adults with chest pain. Priors come from primary-care cohorts (Haasenritter 2015, Bösner 2009 and 2010), except aortic dissection (ED, Alter 2015). The LR sources use different reference conditions, which the YAML header lists.

### Acute coronary syndrome (cannot-miss)

Prior: p = 0.036. Haasenritter 2015 Table 3 ("Relative frequencies ... considering only studies with a low overall risk of bias"), ACS/MI block, Bösner 2009 row: 3.6% (95% CI 2.7%-4.9%) of 1,212 primary-care adults aged 35 or older with chest pain. Status: PLACEHOLDER (DS-5).

LRs from Raat 2024 Table 2 ("Summary table of mean estimates"), ACS rows. The table footnote says that the brackets are 95% CIs. Raat 2024 pooled 24 studies, mostly ED, ambulance, and call-centre populations (Table 1).

| Feature | LR+ (95% CI) | LR− (95% CI) | Studies | Group | Remote | Status |
|---|---|---|---|---|---|---|
| `oppressive_pain` | 1.28 (1.06-1.61) | 0.71 (0.60-0.87) | 7 | none | yes | VERIFIED |
| `radiation_left_arm` | 1.33 (1.22-1.44) | 0.87 (0.78-0.94) | 4 | radiation | yes | VERIFIED |
| `radiation_right_arm` | 2.93 (0.72-7.38) | 0.84 (0.55-1.04) | 1 | radiation | yes | VERIFIED |
| `radiation_neck` | 1.38 (1.05-1.75) | 0.94 (0.85-0.99) | 4 | radiation | yes | VERIFIED |
| `radiation_back` | 1.18 (0.66-1.85) | 0.96 (0.77-1.07) | 4 | radiation | yes | VERIFIED |
| `sweating` | 1.46 (1.28-1.67) | 0.85 (0.79-0.90) | 7 | autonomic | yes | VERIFIED |
| `nausea_vomiting` ("nausea and/or vomiting") | 1.20 (1.00-1.46) | 0.94 (0.90-1.00) | 7 | autonomic | yes | VERIFIED |
| `chest_wall_tenderness_absent` | 1.45 (1.10-2.12) | 0.24 (0.10-0.51) | 3 | none | no (exam) | VERIFIED |

`known_vascular_disease`: LR+ 3.94 (2.78-5.90), LR− 0.50 (0.33-0.70). Bösner 2010 Table 3 ("Clinical recommendation"), section "Useful for considering urgent hospital admission", "Known clinical vascular disease". The reference condition is "indication for urgent hospital admission" in 349 acute cases (pain under 48 hours). Of the 70 patients with this indication, 42 (60.0%) had ACS (Results text). We use it as a proxy for ACS. Status: VERIFIED (proxy reference condition).

Groups. `radiation` holds the four radiation sites, because one pain can spread to more than one site and the source gives no joint data. `autonomic` holds sweating and nausea or vomiting, for the same reason.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 100 | A missed ACS can cause death or heart failure. ED care when it is present has a very large net benefit. |
| harm R | 1 | One unnecessary ED visit. |
| test_se | 0.95 | Illustrative sensitivity of ED evaluation (ECG and serial troponin). Not sourced. |
| test_sp | 0.90 | Illustrative specificity of the same evaluation. Not sourced. |
| test_harm | 0.05 | Burden of the ED visit and tests. |

The engine calculates T_test = 0.00158 and T_treat = 0.144. The prior (0.036) is in the middle zone.

### Coronary heart disease, stable or acute (not cannot-miss)

This diagnosis carries the Bösner 2010 primary-care LRs, whose reference condition is any CHD (stable angina or ACS), as decided by an expert panel after 6 months of follow-up. It is not cannot-miss, because ACS has its own entry.

Prior: p = 0.149. Bösner 2010 Results text: 180 of the non-trauma patients (14.9%) had the reference diagnosis CHD (analysis sample n = 1,199). Status: PLACEHOLDER (DS-5).

All LRs from Bösner 2010 Table 3, section "Useful for including or excluding any CHD".

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `pain_worse_exercise` | 2.53 (2.04-3.14) | 0.68 (0.60-0.78) | none | yes | VERIFIED |
| `known_vascular_disease` | 4.51 (3.63-5.62) | 0.54 (0.46-0.63) | none | yes | VERIFIED |
| `known_heart_failure` | 3.95 (2.60-6.13) | 0.86 (0.81-0.93) | none | yes | VERIFIED |
| `known_diabetes` | 2.55 (1.90-3.44) | 0.81 (0.74-0.89) | none | yes | VERIFIED |
| `age_risk` (female 65+, male 55+) | 1.85 (1.69-2.05) | 0.32 (0.23-0.44) | none | yes (record) | VERIFIED |
| `patient_thinks_heart` | 1.43 (1.31-1.56) | 0.39 (0.27-0.57) | none | yes | VERIFIED |
| `stinging_pain` | 0.45 (0.33-0.62) | 1.41 (1.29-1.54) | none | yes | VERIFIED |
| `cough` | 0.27 (0.13-0.57) | 1.12 (1.08-1.17) | none | yes | VERIFIED |
| `localised_muscle_tension` | 0.38 (0.29-0.58) | 1.68 (1.38-1.70) | chest_wall | no (exam) | VERIFIED |
| `pain_reproducible_palpation` | 0.25 (0.15-0.41) | 1.71 (1.56-1.89) | chest_wall | no (exam) | VERIFIED |

The `localised_muscle_tension` LR− point value (1.68) is close to the upper CI limit (1.70). We copied the values as printed. Group `chest_wall` holds the two chest-wall exam findings, because both come from the same palpation. Bösner 2010 Table 2 (multivariable model) shows that the remaining findings each kept an independent association with CHD.

### Pulmonary embolism (cannot-miss)

Prior: p = 0.0017. Bösner 2010 Results text: among the 70 patients with an indication for urgent hospital admission, 2 (2.9%) had PE. The denominator is the 1,199 primary-care patients in the analysis sample, so 2 of 1,199. This counts only PE that the reference panel found among urgent cases. Status: PLACEHOLDER (DS-5).

All LRs are DERIVED from the Courtney 2010 web-appendix table ("Univariate association of predictor variable stratified by VTE positive and negative groups"). The population is 7,940 adults in 12 US EDs whose physician ordered a test for PE (D-dimer, CT angiography, or V/Q scan). The outcome is VTE (PE or DVT) within 45 days, in 568 of 7,940 (7.2%). The outcome includes DVT, so these LRs are for VTE, not for PE alone.

| Feature | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote |
|---|---|---|---|---|---|---|---|---|
| `history_vte` | 155 | 413 | 703 | 6669 | 2.86 (2.46-3.33) | 0.80 (0.76-0.85) | none | yes |
| `unilateral_leg_swelling` | 135 | 433 | 575 | 6797 | 3.05 (2.58-3.60) | 0.83 (0.79-0.87) | none | yes (patient report) |
| `recent_surgery` (general anaesthesia, 4 weeks) | 86 | 482 | 434 | 6938 | 2.57 (2.07-3.19) | 0.90 (0.87-0.93) | vte_provoked | yes |
| `immobilization` | 125 | 443 | 638 | 6734 | 2.54 (2.14-3.02) | 0.85 (0.82-0.89) | vte_provoked | yes |
| `active_cancer` | 85 | 483 | 404 | 6968 | 2.73 (2.20-3.40) | 0.90 (0.87-0.93) | none | yes |
| `pleuritic_pain` | 274 | 294 | 3386 | 3986 | 1.05 (0.96-1.15) | 0.96 (0.88-1.04) | none | yes |
| `substernal_pain` | 121 | 447 | 2788 | 4584 | 0.56 (0.48-0.66) | 1.27 (1.21-1.33) | none | yes |
| `hypoxemia` (SpO2 < 95%; n = 567 VTE+, 7,349 VTE−) | 240 | 327 | 1304 | 6045 | 2.39 (2.14-2.66) | 0.70 (0.65-0.75) | none | no (measured) |

Courtney 2010 Table 3 (multivariable model) shows independent associations for history of VTE, leg swelling, surgery, cancer, immobilization, and hypoxemia. Group `vte_provoked` holds surgery and immobilization, because post-operative immobility makes them overlap.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 50 | A missed PE can cause death. Same-day evaluation when it is present has a large net benefit. |
| harm R | 1 | One unnecessary ED visit. |
| test_se | 0.97 | Illustrative sensitivity of a D-dimer as the first in-person test. Not sourced. |
| test_sp | 0.40 | Illustrative specificity of the D-dimer. Not sourced. |
| test_harm | 0.05 | Burden of the visit and the blood test. |

The engine calculates T_test = 0.0132 and T_treat = 0.184. The prior (0.0017) is below T_test, so with no findings the engine marks PE as ruled out. `history_vte` and `unilateral_leg_swelling` are in `must_ask`, so the engine still asks them. Two positive VTE risk factors move PE into the middle zone, and the engine then defers.

### Aortic dissection (cannot-miss)

Prior: p = 0.00102. Alter 2015 Abstract and Results: 782 aortic dissections in 9,533,827 ED visits in 33 New York and New Jersey EDs, 1996-2010, which is 1 dissection per 980 (95% CI 910-1,050) patients with atraumatic chest pain. 1/980 = 0.00102. The authors note that a narrower chest-pain definition gives 1 in 600 to 700. Status: PLACEHOLDER (DS-5).

All LRs are DERIVED from Morello 2020 Tables 1 and 2. The population is 297 adults in one Italian ED with a red-flag symptom and clinical suspicion of acute aortic syndrome (AAS); 88 (29.6%) had AAS (Results text). The high prevalence means that spectrum effects can make these LRs too strong for an unselected chest-pain population.

| Feature | Table | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote |
|---|---|---|---|---|---|---|---|---|---|
| `sudden_onset` ("sudden pain") | 2 | 55 | 33 | 91 | 118 | 1.44 (1.15-1.80) | 0.66 (0.49-0.89) | aas_pain | yes |
| `severe_pain` | 2 | 28 | 60 | 45 | 164 | 1.48 (0.99-2.21) | 0.87 (0.74-1.02) | aas_pain | yes |
| `ripping_tearing_pain` | 2 | 20 | 68 | 12 | 197 | 3.96 (2.02-7.74) | 0.82 (0.73-0.92) | aas_pain | yes |
| `known_thoracic_aneurysm` | 2 | 21 | 67 | 19 | 190 | 2.62 (1.49-4.63) | 0.84 (0.74-0.95) | none | yes |
| `hypertension` | 1 | 62 | 26 | 114 | 95 | 1.29 (1.08-1.55) | 0.65 (0.46-0.93) | none | yes |
| `pulse_deficit` | 2 | 16 | 72 | 7 | 202 | 5.43 (2.31-12.73) | 0.85 (0.76-0.94) | none | no (exam) |

Group `aas_pain` holds the three pain features. They form one category ("high-risk pain features") in the aortic dissection detection risk score, and one pain can have all three.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 200 | Mortality of untreated type A dissection is very high. ED care when it is present has a very large net benefit. |
| harm R | 1 | One unnecessary ED visit. |
| test_se | 0.98 | Illustrative sensitivity of CT angiography. Not sourced. |
| test_sp | 0.95 | Illustrative specificity of CT angiography. Not sourced. |
| test_harm | 0.10 | Burden of the visit, contrast, and radiation. |

The engine calculates T_test = 0.00077 and T_treat = 0.172. The prior (0.00102) is in the middle zone.

### Chest wall syndrome (not cannot-miss)

Prior: p = 0.498. Haasenritter 2015 Table 3, chest wall syndrome block, Bösner 2009 row: 49.8% (95% CI 47.0%-52.7%) of 1,212. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

### Gastro-oesophageal reflux disease (not cannot-miss)

Prior: p = 0.035. Bösner 2009 Results text: of 1,212 patients analysed for the cause of their chest pain, 71 had GI disease, including 42 with GERD (42/1,212 = 3.5%). Haasenritter 2015 Table 3 gives oesophageal disorders as 6.0% to 7.1% in two other cohorts (Buntinx 1991, Verdon 2008). Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

## Dyspnea script

Population: adults with shortness of breath. Priors come from the Dutch Transition Project (primary care) as reported in Frese 2011 Table 5. This population includes children, and the highest consultation rate was at age 0 to 4 years (Table 1).

### Heart failure (cannot-miss)

Prior: p = 0.041. Frese 2011 Table 5 ("Incidence (%) of the most frequent diagnoses for primary care patients with complaints of dyspnea"), column "Transition Project initial consultation for new occurred dyspnea (n = 3743)": heart failure 4.09%. Status: PLACEHOLDER (DS-5).

| Feature | LR+ (95% CI) | LR− (95% CI) | Source | Group | Remote | Status |
|---|---|---|---|---|---|---|
| `history_heart_failure` | 5.8 (4.1-8.0) | 0.45 (0.38-0.53) | Wang 2005 Abstract, "past history of heart failure"; ED | none | yes | VERIFIED |
| `history_mi` | 2.1 (1.8-2.5) | 0.82 (0.76-0.89) | Long 2019 Table 2, "History of MI", attributed to Martindale 2016; ED | none | yes | VERIFIED (secondary) |
| `orthopnea` | 2.12 (1.61-2.80) | 0.69 (0.62-0.76) | Devroey 2011 Table 1, TP 258, FN 299, FP 43, TN 154 | hf_nocturnal | yes | DERIVED |
| `pnd` ("nocturnal dyspnea") | 2.30 (1.51-3.49) | 0.84 (0.78-0.90) | Devroey 2011 Table 1, TP 143, FN 414, FP 22, TN 175 | hf_nocturnal | yes | DERIVED |
| `dyspnea_on_exertion` ("breathlessness on exercise") | 1.78 (1.47-2.15) | 0.53 (0.45-0.62) | Devroey 2011 Table 1, TP 372, FN 185, FP 74, TN 123 | none | yes | DERIVED |
| `ankle_swelling` ("peripheral edema") | 1.93 (1.58-2.34) | 0.49 (0.42-0.58) | Devroey 2011 Table 1, TP 381, FN 176, FP 70, TN 127 | none | yes (patient report; source used clinician exam) | DERIVED |

Devroey 2011 population: 754 adults without known HF in whom 178 Belgian sentinel GPs first suspected HF; the GP confirmed HF in 557 (74%) at 1 month (Methods and Results text). The reference standard was the GP's diagnosis at 1 month; only 63% had an echocardiogram. The Devroey sensitivities and specificities in Table 1 agree with the counts. Wang 2005 and Martindale 2016 studied ED patients with dyspnea; Wang 2005 gives paired LRs in the abstract for history of heart failure only. Martindale 2016 also gives orthopnea and PND LRs (Long 2019 Table 2: orthopnea 1.9 [1.4-2.5] and 0.74 [0.64-0.85]; PND 1.6 [1.2-2.1] and 0.79 [0.71-0.88]). We used the primary-care Devroey values for these, because the Waymark population is closer to primary care. Group `hf_nocturnal` holds orthopnea and PND, which overlap in patient report.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 20 | Decompensated HF can need admission; same-day care when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day visit. |
| test_se | 0.93 | Illustrative sensitivity of an in-person evaluation with a natriuretic peptide. Not sourced. |
| test_sp | 0.60 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit and blood test. |

The engine calculates T_test = 0.0237 and T_treat = 0.275. The prior (0.041) is in the middle zone.

### Pulmonary embolism (cannot-miss)

Prior: p = 0.0035. Frese 2011 Table 5, same column: pulmonary embolism 0.35%. Status: PLACEHOLDER (DS-5).

LRs: DERIVED from Courtney 2010, as in the chest-pain script (`history_vte`, `unilateral_leg_swelling`, `recent_surgery`, `immobilization`, `active_cancer`, `hypoxemia`), plus:

| Feature | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Remote |
|---|---|---|---|---|---|---|---|
| `hemoptysis` | 20 | 548 | 207 | 7165 | 1.25 (0.80-1.97) | 0.99 (0.98-1.01) | yes |

Thresholds: same illustrative inputs as PE in the chest-pain script (B 50, R 1, test_se 0.97, test_sp 0.40, test_harm 0.05). T_test = 0.0132, T_treat = 0.184. The prior is below T_test; `history_vte`, `unilateral_leg_swelling`, and `recent_surgery` are in `must_ask`.

### Pneumonia (cannot-miss)

Prior: p = 0.026. Frese 2011 Table 5, same column: pneumonia 2.64%. Status: PLACEHOLDER (DS-5).

All LRs from Htun 2019 Table 2 ("Summary estimates of diagnostic performance measures of each index test assessed in four studies or more"). The reference standard is a chest radiograph. The population is adults in primary care or outpatient and emergency clinics with acute cough or lower respiratory tract infection (Table 1).

| Feature | LR+ (95% CI) | LR− (95% CI) | Studies | Group | Remote | Status |
|---|---|---|---|---|---|---|
| `fever_history` ("Fever", symptom) | 1.41 (1.15-1.78) | 0.70 (0.59-0.82) | 4 | none | yes | VERIFIED |
| `cough` | 1.36 (1.03-2.10) | 0.36 (0.15-0.78) | 6 | pna_cough | yes | VERIFIED |
| `sputum` | 1.27 (0.90-1.72) | 0.72 (0.39-1.13) | 5 | pna_cough | yes | VERIFIED |
| `chest_pain` | 1.37 (1.14-1.60) | 0.79 (0.62-0.93) | 7 | none | yes | VERIFIED |
| `temperature_38` (sign) | 3.21 (2.36-4.23) | 0.68 (0.53-0.82) | 7 | none | no (measured) | VERIFIED |

Table 2 footnotes: cough includes dry cough in one study; sputum includes yellow purulent sputum in three studies; temperature includes 37.8 °C cut-offs in two studies. Most of the Htun studies enrolled patients with cough, so the `cough` LR− is from a population in which few patients had no cough. Group `pna_cough` holds cough and sputum. The reviewer can set `temperature_38` to remote if a home thermometer reading is accepted.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 20 | Untreated pneumonia can progress to sepsis. Same-day care when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day visit. |
| test_se | 0.90 | Illustrative sensitivity of exam plus chest X-ray. Not sourced. |
| test_sp | 0.80 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit and X-ray. |

The engine calculates T_test = 0.0137 and T_treat = 0.268. The prior (0.026) is in the middle zone.

### Asthma or COPD exacerbation (not cannot-miss)

Prior: p = 0.13. Frese 2011 Table 5, same column: bronchial asthma 10.96% plus COPD 2.19% = 13.15%. Asthma and COPD are separate codes in the source, so we added them. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

## Leg-swelling script

Population: adults with a swollen, painful, or red leg.

### Deep vein thrombosis (cannot-miss)

Prior: p = 0.223. Biesheuvel 2008 Methods and Results text and Table 1: 289 of 1,295 (22%) consecutive Dutch primary-care adults with a painful and swollen or red leg for 30 days or less had DVT on repeated compression ultrasound. Dybowska 2015 gives a lower value in Polish primary care (60 of 1,048, 5.7%). We used the higher value, which is the conservative direction for a cannot-miss diagnosis. Status: PLACEHOLDER (DS-5).

| Feature | Source and table | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `previous_dvt` | Heller 2021 Table 1 | 46 | 111 | 52 | 387 | 2.47 (1.74-3.52) | 0.80 (0.72-0.89) | none | yes | DERIVED |
| `active_cancer` | Heller 2021 Table 1 | 24 | 133 | 53 | 386 | 1.27 (0.81-1.98) | 0.96 (0.89-1.04) | none | yes | DERIVED |
| `recent_surgery` | Courtney 2010 web appendix | 86 | 482 | 434 | 6938 | 2.57 (2.07-3.19) | 0.90 (0.87-0.93) | vte_provoked | yes | DERIVED |
| `immobilization` | Courtney 2010 web appendix | 125 | 443 | 638 | 6734 | 2.54 (2.14-3.02) | 0.85 (0.82-0.89) | vte_provoked | yes | DERIVED |
| `male_sex` | Biesheuvel 2008 Table 1 | 137 | 152 | 330 | 676 | 1.45 (1.24-1.68) | 0.78 (0.70-0.88) | none | yes (record) | DERIVED |
| `ddimer_abnormal` (≥ 500 ng/mL) | Biesheuvel 2008 Table 1 | 271 | 18 | 621 | 385 | 1.52 (1.43-1.61) | 0.16 (0.10-0.26) | none | no (blood test) | DERIVED |
| `wells_score_3plus` (score > 2) | Dybowska 2015 Table 4 (threshold 2) | 40 | 20 | 60 | 928 | 10.98 (8.10-14.87) | 0.35 (0.25-0.51) | none | no (exam) | DERIVED |

Heller 2021 population: 596 patients who had whole-leg ultrasound for suspected acute DVT at one German university radiology department in 2014; 157 had DVT. Biesheuvel 2008 reports sensitivity 0.94 (0.91-0.97) and specificity 0.38 (0.35-0.41) for the D-dimer, which agree with the counts. Dybowska 2015 reports sensitivity 66.66% and specificity 93.93% at threshold 2, which agree with the counts.

Two cautions apply. First, `recent_surgery` and `immobilization` come from Courtney 2010 (ED patients tested for PE, VTE outcome). We did not find these Wells history items for DVT in a leg-symptom population in an open full text (see "Unverified and omitted"). The reviewer must accept this population or remove the features. Second, the Heller `active_cancer` LR is weak (CI crosses 1). The Wells rule gives cancer one point, and Courtney 2010 gives LR+ 2.73 for VTE. We used the DVT-specific value.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 30 | A missed DVT can cause PE. Same-day evaluation when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day visit. |
| test_se | 0.97 | Illustrative sensitivity of D-dimer plus compression ultrasound. Not sourced. |
| test_sp | 0.95 | Illustrative specificity of the same strategy. Not sourced. |
| test_harm | 0.05 | Burden of the visit and tests. |

The engine calculates T_test = 0.0034 and T_treat = 0.487. The prior (0.223) is in the middle zone.

### Cellulitis or erysipelas (cannot-miss)

Prior: p = 0.019. Beller 2020 Table 2 ("soft tissue inflammation/erysipelas/cellulitis"): 15 of 531 DVT-negative patients (2.8%). The full scanned cohort was 789 (Abstract), so 15/789 = 0.019. Ultrasound in a suspected-DVT cohort detects only some cellulitis, so this value is probably low for a general leg-swelling population. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 20 | Untreated cellulitis can spread and cause sepsis. Same-day care when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day visit. |
| test_se | 0.90 | Illustrative sensitivity of an in-person skin exam. Not sourced. |
| test_sp | 0.80 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit. |

The engine calculates T_test = 0.0137 and T_treat = 0.268. The prior (0.019) is in the middle zone. Because cellulitis has no features, the engine returns DEFER with `cannot_miss_middle_zone_no_remote_test` at the first step, before it asks any DVT question. We chose B = 20 for this reason. With B = 10, T_test is 0.0272, the prior is below it, and the engine marks cellulitis as ruled out with no question. That is a cannot-miss gap, so we did not use it. The reviewer must choose between these two behaviours or add sourced cellulitis features.

### Chronic venous insufficiency (not cannot-miss)

Prior: p = 0.186. Beller 2020 Abstract: chronic venous insufficiency in 147 of 531 DVT-negative patients (27.7%); 147/789 = 0.186 of the scanned cohort. Status: PLACEHOLDER (DS-5).

LRs: none.

## Syncope script

Population: adults with a transient loss of consciousness.

### Cardiac syncope (cannot-miss)

Prior: p = 0.095. Berecki-Gisolf 2013 Table 3 ("Distribution of age, gender and symptoms in relation to final diagnosis, for each patient population"), Amsterdam data (FAST, ED patients with transient loss of consciousness, Amsterdam, 2000-2002): 44 cardiac and 419 non-cardiac, so 44/463 = 0.095. The text gives 44 of 503 enrolled (9%). Status: PLACEHOLDER (DS-5).

LRs DERIVED from Berecki-Gisolf 2013 Table 3 counts. The Amsterdam denominators differ by row, because some answers were missing; we used the row totals.

| Feature | Dataset | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote |
|---|---|---|---|---|---|---|---|---|---|
| `age_60_plus` | Amsterdam | 32 | 12 | 128 | 291 | 2.38 (1.89-3.00) | 0.39 (0.24-0.64) | age | yes (record) |
| `known_heart_disease` (structural heart disease) | Amsterdam | 18 | 26 | 29 | 390 | 5.91 (3.59-9.74) | 0.63 (0.50-0.81) | none | yes |
| `syncope_during_effort` | Amsterdam | 10 | 33 | 42 | 365 | 2.25 (1.22-4.16) | 0.86 (0.72-1.01) | none | yes |
| `syncope_supine` | Milan (STePS ED, 37 cardiac vs 652) | 14 | 23 | 149 | 503 | 1.66 (1.07-2.56) | 0.81 (0.62-1.04) | none | yes |
| `few_episodes` (two spells or less) | Amsterdam | 26 | 16 | 151 | 218 | 1.51 (1.16-1.98) | 0.64 (0.43-0.96) | none | yes |
| `nausea_before` | Amsterdam | 6 | 37 | 129 | 287 | 0.45 (0.21-0.96) | 1.25 (1.09-1.43) | reflex_prodrome | yes |
| `sweating_before` (diaphoresis) | Amsterdam | 12 | 29 | 200 | 216 | 0.61 (0.37-0.99) | 1.36 (1.10-1.69) | reflex_prodrome | yes |
| `long_warning` ((long) prodrome) | Amsterdam | 9 | 35 | 148 | 271 | 0.58 (0.32-1.05) | 1.23 (1.04-1.45) | reflex_prodrome | yes |

Two LRs come from the Albassam 2019 abstract (n = 323 in each case):

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Status |
|---|---|---|---|---|
| `first_syncope_age_35_plus` | 3.3 (2.6-4.1) | 0.13 (0.06-0.25) | age | VERIFIED (abstract: age at first syncope ≥ 35 years LR 3.3; < 35 years LR 0.13) |
| `history_af_flutter` | 7.3 (2.4-22) | 0.89 (no CI) | none | LR+ VERIFIED (abstract); LR− DERIVED from abstract sensitivity 13% and specificity 98%: (1 − 0.13)/0.98 = 0.888 |

The Amsterdam data had no supine item, so we used the Milan data for `syncope_supine`. The Rochester data in the same table gives a weaker supine LR+ (1.12, 0.84-1.50, DERIVED from 47/424 vs 341/3,453). The reviewer can choose. Group `age` holds the two age features, which overlap. Group `reflex_prodrome` holds nausea, sweating, and a long warning, which are parts of one reflex prodrome.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 50 | Cardiac syncope can come before sudden death. Same-day evaluation when it is present has a large net benefit. |
| harm R | 1 | One unnecessary same-day visit. |
| test_se | 0.90 | Illustrative sensitivity of ECG plus rhythm monitoring and echocardiogram. Not sourced. |
| test_sp | 0.70 | Illustrative specificity. Not sourced. |
| test_harm | 0.05 | Burden of the visit and tests. |

The engine calculates T_test = 0.0077 and T_treat = 0.114. The prior (0.095) is in the middle zone.

### Non-cardiac syncope: reflex (vasovagal), orthostatic, or other (not cannot-miss)

Definition: the complement of cardiac syncope in the same Berecki-Gisolf data. Prior: p = 0.905 (419/463). Status: PLACEHOLDER (DS-5). The source does not split reflex from orthostatic syncope, so the script has one non-cardiac diagnosis.

| Feature | LR+ (95% CI) | LR− (95% CI) | Status |
|---|---|---|---|
| `age_60_plus` | 0.42 (0.33-0.53) | 2.55 (1.57-4.14) | DERIVED (reciprocal) |
| `known_heart_disease` | 0.17 (0.10-0.28) | 1.58 (1.23-2.02) | DERIVED (reciprocal) |
| `syncope_during_effort` | 0.44 (0.24-0.82) | 1.17 (0.99-1.38) | DERIVED (reciprocal) |
| `syncope_supine` | 0.60 (0.39-0.93) | 1.24 (0.96-1.60) | DERIVED (reciprocal, Milan) |
| `few_episodes` | 0.66 (0.51-0.86) | 1.55 (1.04-2.30) | DERIVED (reciprocal) |
| `nausea_before` | 2.22 (1.04-4.73) | 0.80 (0.70-0.92) | DERIVED (reciprocal) |
| `sweating_before` | 1.64 (1.01-2.67) | 0.73 (0.59-0.91) | DERIVED (reciprocal) |
| `long_warning` | 1.73 (0.95-3.14) | 0.81 (0.69-0.96) | DERIVED (reciprocal) |

The Albassam features have no reciprocal here, because the abstract does not define the complement population.

## Engine behaviour with these numbers

We ran `step` with no findings and with test findings (patient-reported, confirmed) on 2026-10-27.

| Script | First step (no findings) | Cannot-miss status at start | Notes from test findings |
|---|---|---|---|
| chest_pain | ASK `known_vascular_disease`, `radiation_right_arm` | ACS and aortic dissection in the middle zone; PE below T_test | `known_vascular_disease` + `sweating` present gave ACS p = 0.177 (p95 0.231) and ESCALATE. `ripping_tearing_pain` alone moved dissection to p = 0.004 and the engine kept asking. With 11 ACS, PE, and dissection features absent, the engine still asked (ACS p95 0.015 is above T_test 0.0016). |
| dyspnea | ASK `history_heart_failure`, `ankle_swelling` | HF and pneumonia in the middle zone; PE below T_test | `orthopnea` + `history_heart_failure` gave HF p = 0.20 and the engine kept asking. With 13 HF, PE, and pneumonia features absent, the engine returned COMPLETE (HF p95 0.004, pneumonia p95 0.010, PE p95 0.002). |
| leg_swelling | DEFER (`cannot_miss_middle_zone_no_remote_test`) | DVT and cellulitis in the middle zone | Cellulitis has no remote features, so the engine defers at once. `previous_dvt` present gave DVT p = 0.41 and ESCALATE. |
| syncope | ASK `first_syncope_age_35_plus`, `nausea_before` | Cardiac syncope in the middle zone | `syncope_during_effort`, `known_heart_disease`, or `history_af_flutter` present each gave ESCALATE (p = 0.19, 0.38, 0.43). |

The reviewer must decide on one result. In the dyspnea script, a patient who denies all 13 history items reaches COMPLETE, because the history LRs together move HF and pneumonia below the illustrative T_test values. The lane permits DISPOSITION (`compass_pcp/lanes.py`). If the CPD wants this lane never to close an encounter remotely, that rule belongs in the lane gate, not in the threshold numbers.

## Unverified and omitted

| Item | Reason |
|---|---|
| Fanaroff AC et al. Does this patient with chest pain have acute coronary syndrome? *JAMA*. 2015;314(18):1955-1965. PMID 26547467 | [UNVERIFIED — omitted]. Full text not available to us (JAMA paywall). The abstract gives LR+ only (pain radiation to both arms 2.6 [1.8-3.7], peripheral arterial disease 2.7 [1.5-4.8], prior abnormal stress test 3.1 [2.0-4.7]) and no LR−. We used Raat 2024 instead. |
| Swap CJ, Nagurney JT. Value and limitations of chest pain history in the evaluation of patients with suspected acute coronary syndromes. *JAMA*. 2005;294(20):2623-2629. PMID 16304077. doi:10.1001/jama.294.20.2623 | [UNVERIFIED — omitted]. Full text not read. |
| Klompas M. Does this patient have an acute thoracic aortic dissection? *JAMA*. 2002;287(17):2262-2272. PMID 11980527 | [UNVERIFIED — omitted]. Full text not available to us. The abstract gives absence of sudden onset LR− 0.3 (0.2-0.5) and pulse deficit LR+ 5.7, without paired values. We used Morello 2020 counts instead. |
| Ohle R et al. Clinical examination for acute aortic dissection: a systematic review and meta-analysis. *Acad Emerg Med*. 2018 [UNVERIFIED — check manually] | [UNVERIFIED — omitted]. Not read. A Europe PMC search did not return this record, so the citation details are not confirmed. |
| West J, Goodacre S, Sampson F. The value of clinical features in the diagnosis of acute pulmonary embolism: systematic review and meta-analysis. *QJM*. 2007;100(12):763-769. PMID 18089542. doi:10.1093/qjmed/hcm113 | [UNVERIFIED — omitted]. Full text not read. We used Courtney 2010 counts instead. |
| Chest wall syndrome LRs (Ronga A et al. *BMC Fam Pract*. 2012;13:74, PMID 22866824) | [UNVERIFIED — omitted]. Ronga 2012 Table 3 gives odds ratios, not LRs, for single findings (pain reproducible by palpation OR 6.47; stabbing pain OR 2.11). The clinical prediction rule (validation sensitivity 22.0%, specificity 93.4%) includes "absence of GP concern" and palpation, which are not patient questions. |
| GERD LRs (Bösner 2009 Table 3: pain worse with food intake LR+ 10.5; retrosternal pain radiation LR+ 6.39; localised muscle tension 0.38) | [UNVERIFIED — omitted]. The table gives LR+ only, with no LR− and no CI. The schema needs both. |
| Pericarditis, pneumothorax, oesophageal rupture (chest pain) | [UNVERIFIED — omitted]. No LR source searched to a table. |
| Wang 2005 orthopnea (LR+ 2.2), PND (LR+ 2.6 [1.5-4.5]), dyspnea on exertion (LR− 0.48 [0.35-0.67]), S3 gallop, chest X-ray, BNP | [UNVERIFIED — omitted] as Wang values. The abstract gives only one of each pair. We used the paired Devroey 2011 counts for orthopnea, PND, and exertional dyspnea. |
| Mant J et al. Systematic review and individual patient data meta-analysis of diagnosis of heart failure. *Health Technol Assess*. 2009;13(32). PMID 19586584 | [UNVERIFIED — omitted]. Full report blocked (HTTP 403 and CAPTCHA). The abstract gives sensitivity or specificity for single features, not pairs. |
| Ebell MH et al. Accuracy of signs and symptoms for the diagnosis of community-acquired pneumonia: a meta-analysis. *Acad Emerg Med*. 2020. PMID 32329557 | [UNVERIFIED — omitted]. PDF blocked (HTTP 403). We used Htun 2019 instead. |
| Asthma or COPD exacerbation LRs (wheeze, known asthma or COPD, inhaler use) | [UNVERIFIED — omitted]. No diagnostic-accuracy table with paired LRs found. Long 2019 Table 2 gives wheeze LRs for HF only (0.6 [0.5-0.8], 1.19 [1.10-1.30]); we did not use them for asthma or COPD. |
| ACS, pneumothorax, anaphylaxis, upper airway obstruction as causes of dyspnea | [UNVERIFIED — omitted]. Not searched to a table. Put red flags in the lane gate. |
| Goodacre S, Sutton AJ, Sampson FC. Meta-analysis: the value of clinical assessment in the diagnosis of deep venous thrombosis. *Ann Intern Med*. 2005;143(2):129-139. PMID 16027455 | [UNVERIFIED — omitted]. Full text not available to us. The abstract gives single LRs without pairs (malignancy 2.71, previous DVT 2.25, recent immobilization 1.98, recent surgery 1.76; absence of calf swelling 0.67). |
| Wells PS, Owen C, Doucette S, Fergusson D, Tran H. Does this patient have deep vein thrombosis? *JAMA*. 2006;295(2):199-207. PMID 16403932. doi:10.1001/jama.295.2.199 | [UNVERIFIED — omitted]. Full text not read. |
| Wells score > 0 for DVT (Dybowska 2015 Table 3: TP 59, FN 1, FP 343, TN 645) | [UNVERIFIED — omitted]. The derived LR− is 0.03 with a lower CI limit that rounds to 0.00, which does not pass the schema (LR must be more than 0). With only 1 false negative, the estimate is unstable. |
| Cellulitis LRs (redness, warmth, fever, unilateral vs bilateral swelling) | [UNVERIFIED — omitted]. No diagnostic-accuracy study with a comparison group found in an open full text. Beller 2020 Table 1 gives redness for "any alternative finding", not cellulitis. |
| Courtney 2010 estrogen use (LR+ 1.08), family history of VTE (1.33), non-cancer thrombophilia (2.74), age > 50 (1.41) | Not added. The values are available as DERIVED counts in the web-appendix table. We left them out to keep the PE feature set to the Wells and PERC history items. The reviewer can add them. |
| Del Rosso A et al. Clinical predictors of cardiac syncope at initial evaluation in patients referred urgently to a general hospital: the EGSYS score. *Heart*. 2008;94(12):1620-1626. PMID 18519550 | [UNVERIFIED — omitted]. PDF blocked (HTTP 403). The EGSYS items (palpitations before syncope, abnormal ECG or heart disease, effort, supine, autonomic prodrome, precipitating factors) are partly covered by the Berecki-Gisolf features. |
| Palpitations before syncope | [UNVERIFIED — omitted]. Berecki-Gisolf 2013 Table 2 (pooled published studies) gives palpitations in 39 of 468 cardiac and 200 of 1,768 non-cardiac patients (their LR 1.03). The same table has inconsistent totals in the diaphoresis rows (for example 86 [18%] "yes" for cardiac when the study counts sum to 382), so we did not use Table 2. The test datasets in Table 3 do not record palpitations. Palpitations before a faint belong in the lane gate as a hard escalation rule. |
| Albassam 2019 other abstract values (cyanosis witnessed LR 6.2; mood change or prodromal preoccupation LR 0.09; feeling cold 0.16; headache 0.17; EGSYS < 3 LR 0.12-0.17) | [UNVERIFIED — omitted]. The abstract gives sensitivity and specificity, so LR− can be derived, but witness reports and these prodrome items are hard to ask by text and were not needed for cannot-miss coverage. |
| Seizure, PE, aortic dissection, GI bleeding as causes of syncope; family history of sudden death | [UNVERIFIED — omitted]. Not searched to a table. Put these in the lane gate as hard escalation rules. |
| Reflex vs orthostatic syncope split | [UNVERIFIED — omitted]. Berecki-Gisolf 2013 Table 1 lists Iglesias (ambulatory syncope clinic) categories (VV/Psy 387, hypotension 58, arrhythmia 148 of 939), but the Amsterdam data do not split non-cardiac syncope, and we found no paired LRs for orthostatic syncope. |
