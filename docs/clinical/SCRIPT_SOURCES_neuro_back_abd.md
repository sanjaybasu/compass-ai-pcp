# Illness-script sources: headache, dizziness, low back pain, abdominal pain

This file lists the source of each number in these four scripts:

- `compass_pcp/data/scripts/headache.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/focal_neuro_dizziness.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/low_back_pain.yaml` (version 0.1.0-draft)
- `compass_pcp/data/scripts/abdominal_pain.yaml` (version 0.1.0-draft)

All four scripts are drafts for physician sign-off. `clinical_review.approved_by` is null in each file. The lane is `undifferentiated_high_risk`. In this lane the AI takes the history and escalates. It does not treat. The main job of each script is cannot-miss coverage.

Status labels:

- **VERIFIED.** We copied the value from a table or results text that we read in the source article.
- **VERIFIED (secondary).** We copied the value from a table or text that we read, but that table reproduces another article that we could not read. The primary article is named. The reviewer must check the primary table.
- **DERIVED.** We calculated the value from counts or from sensitivity and specificity that we read. The calculation is given.
- **PLACEHOLDER.** The value is a literature value that a Waymark claims rate (DS-5) or a CPD decision-analysis memo must replace.
- **[UNVERIFIED — omitted].** We did not put the value in a script.

We calculated derived 95% CIs for likelihood ratios (LRs) with the log method (Simel DL, Samsa GP, Matchar DB. Likelihood ratios with confidence: sample size estimation for diagnostic test studies. *J Clin Epidemiol*. 1991;44(8):763-770. PMID 1941027): $SE(\ln LR^{+}) = \sqrt{1/a - 1/(a+c) + 1/b - 1/(b+d)}$, where $a$ is true positives, $c$ is false negatives, $b$ is false positives, and $d$ is true negatives. We calculated $LR^{-}$ in the same way. When a source gives only sensitivity and specificity, we calculated $LR^{+} = Se/(1-Sp)$ and $LR^{-} = (1-Se)/Sp$ and gave no CI.

## Summary of counts

| Script | LRs | VERIFIED | VERIFIED (secondary) | DERIVED | Priors (PLACEHOLDER) | Threshold sets (PLACEHOLDER) |
|---|---|---|---|---|---|---|
| headache | 12 | 5 | 0 | 7 | 5 | 3 |
| focal_neuro_dizziness | 10 | 3 | 0 | 7 | 2 | 1 |
| low_back_pain | 11 | 8 | 0 | 3 | 4 | 3 |
| abdominal_pain | 9 | 0 | 8 | 1 | 4 | 3 |
| Total | 42 | 16 | 8 | 18 | 15 | 10 |

Five features carry no LR. They are rule-only `must_ask` red flags: `fever` (headache), `bladder_bowel_change` and `saddle_numbness` (low back pain), and `pregnancy_possible` (abdominal pain). A PRESENT rule-only flag acts through `red_flag_action` (default escalate) in `engine/workup.py`. It does not change any posterior.

## Sources that we read

| Key | Citation | Access |
|---|---|---|
| Carpenter 2016 | Carpenter CR, Hussain AM, Ward MJ, et al. Spontaneous subarachnoid hemorrhage: a systematic review and meta-analysis describing the diagnostic accuracy of history, physical examination, imaging, and lumbar puncture with an exploration of test thresholds. *Acad Emerg Med*. 2016;23(9):963-1003. PMID 27306497. doi:10.1111/acem.12984 | PMC5018921, Results text, Table 4 ("Single-Study Predictors of SAH from History and Physical Exam Available") |
| Perry 2010 | Perry JJ, Stiell IG, Sivilotti MLA, et al. High risk clinical characteristics for subarachnoid haemorrhage in patients with acute headache: prospective cohort study. *BMJ*. 2010;341:c5204. PMID 21030443. doi:10.1136/bmj.c5204 | PMC2966872, Tables 1 to 3 |
| Kelly 2021 | Kelly AM, Kuan WS, Chu KH, et al. Epidemiology, investigation, management, and outcome of headache in emergency departments (HEAD study): a multinational observational study. *Headache*. 2021;61(10):1539-1552. PMID 34726783. doi:10.1111/head.14230 | Abstract only |
| Akaishi 2019 | Akaishi T, Kobayashi J, Abe M, et al. Sensitivity and specificity of meningeal signs in patients with meningitis. *J Gen Fam Med*. 2019;20(5):193-198. PMID 31516806. doi:10.1002/jgf2.268 | PMC6732499, Tables 1 and 2 and Results text |
| Lipton 2003 | Lipton RB, Dodick D, Sadovsky R, et al. A self-administered screener for migraine in primary care: the ID Migraine validation study. *Neurology*. 2003;61(3):375-382. PMID 12913201. doi:10.1212/01.wnl.0000078940.53438.83 | Abstract only |
| Navi 2012 | Navi BB, Kamel H, Shah MP, et al. Rate and predictors of serious neurologic causes of dizziness in the emergency department. *Mayo Clin Proc*. 2012;87(11):1080-1088. PMID 23063099. doi:10.1016/j.mayocp.2012.05.023 | PMC3541873, Tables 1 to 4 (read through the PMC web page; two independent reads gave the same counts) |
| Tarnutzer 2011 | Tarnutzer AA, Berkowitz AL, Robinson KA, Hsieh YH, Newman-Toker DE. Does my dizzy patient have a stroke? A systematic review of bedside diagnosis in acute vestibular syndrome. *CMAJ*. 2011;183(9):E571-E592. PMID 21576300. doi:10.1503/cmaj.100174 | PMC3114934, Tables 3 and 4 (read through the PMC web page) |
| Downie 2013 | Downie A, Williams CM, Henschke N, et al. Red flags to screen for malignancy and fracture in patients with low back pain: systematic review. *BMJ*. 2013;347:f7095. PMID 24335669. doi:10.1136/bmj.f7095 | PMC3898572, Results text and web appendix Tables B, C, E, F, G (PDF from Europe PMC supplementary files) |
| Henschke 2009 | Henschke N, Maher CG, Refshauge KM, et al. Prevalence of and screening for serious spinal pathology in patients presenting to primary care settings with acute low back pain. *Arthritis Rheum*. 2009;60(10):3072-3080. PMID 19790051. doi:10.1002/art.24853 | Abstract; counts read in Downie 2013 appendix Table E |
| Hoeritzauer 2020 | Hoeritzauer I, Wood M, Copley PC, Demetriades AK, Woodfield J. What is the incidence of cauda equina syndrome? A systematic review. *J Neurosurg Spine*. 2020;32(6):832-841. PMID 32059184. doi:10.3171/2019.12.SPINE19839 | Abstract only |
| Zusman 2022 | Zusman NL, Radoslovich SS, Smith SJ, Tanski M, Gundle KR, Yoo JU. Physical examination is predictive of cauda equina syndrome: MRI to rule out diagnosis is unnecessary. *Global Spine J*. 2022;12(2):209-214 (epub 2020). PMID 32935582. doi:10.1177/2192568220948804 | PMC8907650, Tables 1 and 2 |
| Viniol 2014 | Viniol A, Keunecke C, Biroga T, et al. Studies of the symptom abdominal pain: a systematic review and meta-analysis. *Fam Pract*. 2014;31(5):517-529. PMID 24987023. doi:10.1093/fampra/cmu036 | Abstract only |
| Laméris 2009 | Laméris W, van Randen A, van Es HW, et al. Imaging strategies for detection of urgent conditions in patients with acute abdominal pain: diagnostic accuracy study. *BMJ*. 2009;338:b2431. PMID 19561056. doi:10.1136/bmj.b2431 | PMC3273785, Table 1 ("Final diagnoses assigned by expert panel") |
| Köksal 2013 | Köksal Ö, Özdemir F, Armağan E, et al. Is routine pregnancy test necessary in women of reproductive age admitted to the emergency department? *World J Emerg Med*. 2013;4(3):175-178. PMID 25215114. doi:10.5847/wjem.j.issn.1920-8642.2013.03.003 | PMC4129843, Results text |
| Chopra 2015 | Chopra A. Gastroenterology. In: *Approach to Internal Medicine*. 4th ed. Springer; 2015. doi:10.1007/978-3-319-11821-5_5 | PMC7123601, "Rational Clinical Examination Series: Does this patient have appendicitis?" table |
| Catena 2019 | Catena F, De Simone B, Coccolini F, Di Saverio S, Sartelli M, Ansaloni L. Bowel obstruction: a narrative review for all physicians. *World J Emerg Surg*. 2019;14:20. PMID 31168315. doi:10.1186/s13017-019-0240-7 | PMC6489175, "Initial patient assessment" text |
| Crochet 2013 | Crochet JR, Bastian LA, Chireau MV. Does this woman have an ectopic pregnancy? The rational clinical examination systematic review. *JAMA*. 2013;309(16):1722-1729. PMID 23613077. doi:10.1001/jama.2013.3914 | Abstract only (used for an omission decision, not for a value) |

Primary articles that the secondary sources reproduce (we did not read their tables): Wagner JM, McKinney WP, Carpenter JL. Does this patient have appendicitis? *JAMA*. 1996;276(19):1589-1594. PMID 8918857. Taylor MR, Lalani N. Adult small bowel obstruction. *Acad Emerg Med*. 2013;20(6):528-544. PMID 23758299. doi:10.1111/acem.12150. Böhner H, Yang Q, Franke C, Verreet PR, Ohmann C. Simple data from history and physical examination help to exclude bowel obstruction and to avoid radiographic studies in patients with acute abdominal pain. *Eur J Surg*. 1998;164(10):777-784. PMID 9840308. doi:10.1080/110241598750005435.

## Headache script

Population for the LRs: adults with acute headache in the ED. The SAH LRs come from alert adults whose non-traumatic headache peaked within 1 hour (Perry 2010) or who had an acute worst headache (Bo 2008, through Carpenter 2016). These populations have a higher SAH prevalence than a primary-care or text-message population, so spectrum effects can change the LRs.

### Subarachnoid hemorrhage (cannot-miss)

Perry 2010 Table 2 ("Interobserver agreement and univariate correlation of variables for subarachnoid haemorrhage") gives counts for 130 patients with SAH and 1,869 without SAH. We made a 2x2 table for each finding: TP = count with SAH, FN = 130 − TP, FP = count without SAH, TN = 1,869 − FP.

| Feature | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|
| `worst_headache` | 121 | 9 | 1,448 | 421 | 1.20 (1.14-1.27) | 0.31 (0.16-0.58) | sah_onset | yes | DERIVED |
| `onset_exertion` | 30 | 100 | 200 | 1,669 | 2.16 (1.53-3.03) | 0.86 (0.78-0.95) | none | yes | DERIVED |
| `loss_of_consciousness` | 22 | 108 | 84 | 1,785 | 3.77 (2.44-5.81) | 0.87 (0.80-0.94) | none | yes | DERIVED |
| `neck_pain_stiffness` ("complaint of neck stiffness or pain") | 92 | 38 | 578 | 1,291 | 2.29 (2.01-2.61) | 0.42 (0.32-0.55) | sah_neck | yes | DERIVED |
| `vomiting` | 76 | 54 | 492 | 1,377 | 2.22 (1.89-2.62) | 0.56 (0.46-0.69) | none | yes | DERIVED |
| `neck_stiffness_exam` ("neck stiffness (flexion/extension)") | 40 | 90 | 97 | 1,772 | 5.93 (4.29-8.19) | 0.73 (0.65-0.82) | sah_neck | no (in-person exam) | DERIVED |

Two cautions apply. First, Table 2 prints 71.1% (92) for neck pain in the SAH column, but 92/130 is 70.8%. The table can have a small number of missing answers. We used 130 as the denominator for every row. Second, Carpenter 2016 Results text gives a pooled LR+ of 4.12 (2.24-7.59) for subjective neck stiffness and 6.59 (3.95-11.00) for neck stiffness on exam, but no pooled LR−. The pooled values are in forest plots that we could not read as text. We used the Perry 2010 single-study counts because they give both LR+ and LR−.

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `onset_peak_within_1h` | 1.13 (1.09-1.19) | 0.06 (CI 0-0.95, not in YAML) | sah_onset | yes | VERIFIED |

Carpenter 2016 Table 4, row "Onset <1 hour" (Bo 2008, one study): sensitivity 100% (95-100), specificity 12% (9-16). Bo 2008 enrolled 433 ED patients aged more than 14 with acute-onset worst headache of life (Carpenter Table 1). The schema needs a CI lower bound more than 0, so the YAML has no `lr_neg_ci`. The 12% specificity means that most callers will answer yes. For this reason `onset_peak_within_1h` is not a `must_ask` red flag. It is the SAH rule-out question, and the engine asks it while SAH stays in the middle zone.

Groups: `sah_onset` (worst headache, peak within 1 hour) because both describe the onset. `sah_neck` (reported neck pain or stiffness, neck stiffness on exam) because both measure the same sign. Perry 2010 Rule 1 kept age 40 or more, neck pain, witnessed loss of consciousness, and onset with exertion as independent predictors, so these have no shared group.

Prior: p = 0.01. The Kelly 2021 abstract reports that SAH, stroke, neoplasm, non-SAH hemorrhage, and meningitis were "about 1% each" of 4,536 adults with nontraumatic headache in 67 EDs in 10 countries. The abstract does not give the exact count for SAH. Status: PLACEHOLDER (DS-5). Perry 2010 has a higher prevalence (130 of 1,999, 6.5%) because it enrolled only headaches that peaked within 1 hour.

### Meningitis (cannot-miss)

Akaishi 2019 Table 2 ("Calculated effect sizes for each of the studied diagnostic examinations"). The reference standard is CSF pleocytosis. Nine studies have 599 patients with pleocytosis and 1,216 without (abstract). The CIs in Table 2 are 99% CIs, and the YAML copies them as reported.

| Feature | LR+ (99% CI) | LR− (99% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `jolt_accentuation` | 1.81 (1.50-2.20) | 0.67 (0.58-0.77) | meningeal_signs | yes, guided self-test | VERIFIED |
| `nuchal_rigidity_exam` | 1.60 (1.35-1.91) | 0.76 (0.67-0.85) | meningeal_signs | no (in-person exam) | VERIFIED |
| `kernig_sign_exam` | 2.61 (1.83-3.71) | 0.84 (0.79-0.91) | meningeal_signs | no (in-person exam) | VERIFIED |
| `brudzinski_sign_exam` | 2.44 (1.74-3.44) | 0.82 (0.75-0.89) | meningeal_signs | no (in-person exam) | VERIFIED |

A clinician did the jolt maneuver in the source studies. The script asks the patient to do it. The reviewer can set `remote_askable: false` for `jolt_accentuation` if the self-test is not accepted. All four signs share group `meningeal_signs` because they come from the same patients and measure meningeal irritation.

`fever` is a rule-only `must_ask` feature with no LR. We found no paired LRs for fever history in a headache population (see "Unverified and omitted"). A PRESENT answer escalates by `red_flag_action` (default).

Prior: p = 0.01, from the Kelly 2021 abstract ("about 1%"). Status: PLACEHOLDER (DS-5).

### Intracranial mass or raised intracranial pressure (cannot-miss)

LRs: none. See "Unverified and omitted". Prior: p = 0.01, from the Kelly 2021 abstract (neoplasm "about 1%"). Status: PLACEHOLDER (DS-5). A primary-care alternative is lower: Kernick D, Stapley S, Goadsby PJ, Hamilton W. What happens to new-onset headache presented to primary care? *Cephalalgia*. 2008;28(11):1188-1195 (PMID 18771496) gives a 1-year risk of 0.15% for a malignant brain tumor and 0.05% for a benign space-occupying lesion after a new undifferentiated headache (abstract).

### Migraine

| Feature | LR+ | LR− | Remote | Status |
|---|---|---|---|---|
| `id_migraine_positive` (2 of 3: nausea, light sensitivity, disability) | 3.24 | 0.25 | yes | DERIVED |

Derivation. The Lipton 2003 abstract gives sensitivity 0.81 (95% CI 0.77-0.85) and specificity 0.75 (0.64-0.84) for the 3-item ID Migraine screener. The reference standard was an IHS diagnosis by a headache expert. The population was 451 primary-care patients who reported headaches in the past 3 months. $LR^{+} = 0.81/0.25 = 3.24$ and $LR^{-} = 0.19/0.75 = 0.25$. The abstract gives no counts, so there is no CI. The population had recurrent headache, which is different from a single new headache.

Prior: p = 0.243. Kelly 2021 abstract: migraine 1,101 of 4,536 (24.3%). Status: PLACEHOLDER (DS-5).

### Tension-type or other benign headache

LRs: none. Prior: p = 0.454. Kelly 2021 abstract: presumed nonmigraine benign headache 2,058 of 4,536 (45.4%). Status: PLACEHOLDER (DS-5).

### Thresholds (illustrative)

Every threshold source string is "PLACEHOLDER: CPD decision-analysis memo; illustrative values". The engine calculates T_test and T_treat with `pauker_kassirer`.

| Diagnosis | B | R | test_se | test_sp | test_harm | T_test | T_treat | Reason |
|---|---|---|---|---|---|---|---|---|
| SAH | 40 | 1 | 0.94 | 0.99 | 0.05 | 0.0016 | 0.2773 | B/R = 40 matches the Carpenter 2016 test-threshold inputs (benefit 0.8, angiography risk 0.02). test_se 0.94 is the Carpenter 2016 pooled CT sensitivity (Results text). test_sp is not sourced. |
| Meningitis | 50 | 1 | 0.95 | 0.95 | 0.05 | 0.0021 | 0.2609 | A missed bacterial meningitis can cause death or brain damage. Test = in-person evaluation and lumbar puncture. Not sourced. |
| Mass or raised ICP | 10 | 1 | 0.95 | 0.95 | 0.05 | 0.0105 | 0.6207 | Harm from a short delay is lower than for SAH or meningitis. Test = in-person exam and imaging. Not sourced. |

## Dizziness and focal neurologic symptom script

Population for the history LRs: 907 adults with a primary ED triage complaint of dizziness, vertigo, or imbalance at one academic ED in San Francisco, 2007 to 2009 (Navi 2012).

### Stroke or TIA, including posterior circulation (cannot-miss)

Navi 2012 Tables 1 to 3 give counts for 49 patients with a serious neurologic diagnosis and 858 with other diagnoses. The serious composite was 24 ischemic strokes, 8 TIAs, 5 intracerebral hemorrhages, 6 brain neoplasms, 4 seizures, and 2 demyelinating diseases (Table 4). Thus 37 of 49 were cerebrovascular. The LRs are for the composite, not for stroke or TIA only. The Results text gives 9 TIAs and 8 hemorrhages, which differs from Table 4. We used Table 4 because its counts sum to 49.

| Feature | Table | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| `unilateral_weakness` | 2 | 9 | 40 | 8 | 850 | 19.70 (7.95-48.83) | 0.82 (0.72-0.94) | focal_symptoms | yes | DERIVED |
| `speech_disturbance` | 2 | 10 | 39 | 15 | 843 | 11.67 (5.53-24.63) | 0.81 (0.70-0.93) | focal_symptoms | yes | DERIVED |
| `diplopia` | 2 | 7 | 42 | 16 | 842 | 7.66 (3.31-17.75) | 0.87 (0.78-0.98) | focal_symptoms | yes | DERIVED |
| `gait_disturbance` | 2 | 23 | 26 | 130 | 728 | 3.10 (2.21-4.34) | 0.63 (0.48-0.82) | none | yes | DERIVED |
| `previous_stroke` | 1 | 8 | 41 | 46 | 812 | 3.05 (1.52-6.09) | 0.88 (0.78-1.00) | none | yes | DERIVED |
| `any_focal_exam_finding` | 3 | 31 | 18 | 145 | 713 | 3.74 (2.89-4.85) | 0.44 (0.31-0.64) | neuro_exam | no (in-person exam) | DERIVED |
| `limb_ataxia_exam` | 3 | 10 | 39 | 19 | 839 | 9.22 (4.53-18.74) | 0.81 (0.71-0.94) | neuro_exam | no (in-person exam) | DERIVED |

Navi 2012 is retrospective. The neurologists who assigned the final diagnosis also read the chart that recorded the symptoms, so incorporation bias can make the LRs too high.

Tarnutzer 2011 Table 4 ("Pooled analysis of key bedside diagnostic predictors of stroke in AVS"). The population is acute vestibular syndrome, which is continuous vertigo with nystagmus, nausea, and gait unsteadiness for hours to days. The reference standard is stroke or another central cause on neuroimaging.

| Feature | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|
| `head_impulse_test_normal` (all central causes) | 18.39 (6.08-55.64) | 0.16 (0.11-0.23) | hints | no (in-person exam) | VERIFIED |
| `direction_changing_nystagmus` | 4.51 (2.18-9.34) | 0.68 (0.60-0.76) | hints | no (in-person exam) | VERIFIED |
| `skew_deviation` | 19.66 (2.76-140.15) | 0.71 (0.63-0.80) | hints | no (in-person exam) | VERIFIED |

Groups: `focal_symptoms` (weakness, speech trouble, double vision) because they are correlated symptoms of one brain lesion. `neuro_exam` because "any focal finding" includes limb ataxia. `hints` because the three HINTS components come from the same exam. The text of Tarnutzer 2011 gives a combined HINTS LR− of 0.02 (0.01-0.09), which is stronger than any single component. The group keeps the conservative single-component value.

Prior: p = 0.041. Navi 2012 abstract: 37 cerebrovascular events among 907 patients (4.1%). Status: PLACEHOLDER (DS-5). The prior is the cerebrovascular share, and the LRs are for the full serious composite (49 of 907, 5.4%). The reviewer can use 0.054 to match the LR reference standard.

### Peripheral vestibular disorder

LRs: none. Prior: p = 0.324. Navi 2012 Table 4: peripheral neurologic diseases 294 of 907 (32%): peripheral vertigo not otherwise specified 185, BPPV 78, vestibular neuronitis 27, Ménière disease 4. Status: PLACEHOLDER (DS-5).

### Thresholds (illustrative)

| Diagnosis | B | R | test_se | test_sp | test_harm | T_test | T_treat | Reason |
|---|---|---|---|---|---|---|---|---|
| Stroke or TIA | 30 | 1 | 0.9 | 0.9 | 0.05 | 0.0055 | 0.2179 | Thrombolysis and early secondary prevention depend on time. Test = in-person evaluation with imaging. Not sourced. |

## Low back pain script

Population: adults with low back pain in primary care or walk-in clinics (Henschke 2009, Deyo 1988, through Downie 2013), with exceptions noted for cauda equina syndrome.

### Vertebral fracture (cannot-miss)

Downie 2013 appendix Table E ("Results of included studies for detection of spinal fracture in primary care"), rows for Henschke 2009: 1,172 consecutive primary-care patients (general practice, physiotherapy, chiropractic) with acute LBP in Sydney, 8 fractures, 12-month follow-up as reference standard (appendix Table B).

| Feature | TP | FP | FN | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|
| `age_over_70` | 4 | 52 | 4 | 1,112 | 11.19 (5.33-23.51) | 0.52 (0.26-1.05) | fracture_flags | yes (or enrollment data) | VERIFIED |
| `significant_trauma` | 2 | 29 | 6 | 1,135 | 10.03 (2.87-35.13) | 0.77 (0.52-1.15) | fracture_flags | yes | VERIFIED |
| `prolonged_steroids` | 2 | 6 | 6 | 1,158 | 48.5 (11.48-204.99) | 0.75 (0.51-1.12) | fracture_flags | yes | VERIFIED |

Henschke 2009 defines significant trauma as "trauma which is major in young patients and minor in elderly patients" (Table E footnote). Downie does not define "prolonged". With 8 fractures, every CI is wide. Table E gives LR+ 15.48 (8.45-28.36) for 2 positive Henschke flags, which is less than the product of the single-flag LR+ values. Thus the flags are not independent, and they share group `fracture_flags`.

Prior: p = 0.0068 (8 of 1,172). Status: PLACEHOLDER (DS-5). Downie 2013 Results text gives a median fracture prevalence of 3.6% (IQR 1.8-4.3%) in primary care, which is higher.

### Spinal malignancy (cannot-miss)

Downie 2013 appendix Table G ("Results of included studies for detection of spinal malignancy (all care settings)"), rows for Deyo 1988: 1,975 walk-in clinic patients in the USA with back pain as the primary complaint, 13 cancers, tumor registry at 6 months or more as reference standard (appendix Table C).

| Feature | TP | FP | FN | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|
| `previous_cancer` | 4 | 39 | 9 | 1,897 | 15.27 (6.38-36.55) | 0.71 (0.49-1.02) | none | yes | VERIFIED |
| `age_50_or_older` (">50 years") | 10 | 562 | 3 | 1,377 | 2.65 (1.95-3.6) | 0.32 (0.12-0.88) | cancer_minor | yes (or enrollment data) | VERIFIED |
| `unexplained_weight_loss` | 2 | 115 | 11 | 1,822 | 2.59 (0.72-9.39) | 0.90 (0.71-1.13) | cancer_minor | yes | VERIFIED |
| `not_improved_1_month` | 4 | 196 | 9 | 1,766 | 3.08 (1.35-7.04) | 0.77 (0.54-1.11) | cancer_minor | yes | VERIFIED |
| `bed_rest_no_relief` | 4 | 507 | 0 | 432 | 1.67 (1.24-2.25) | 0.22 (0.02-3.02) | cancer_minor | yes | VERIFIED |

The bed-rest row has 943 patients, not 1,975, so the question was asked only of patients who tried bed rest. The four minor flags come from one cohort and share group `cancer_minor`. Downie 2013 Results text: "history of cancer" gives a post-test probability of 7% (3% to 16%) in primary care.

Prior: p = 0.0066 (13 of 1,975). Status: PLACEHOLDER (DS-5).

### Cauda equina syndrome (cannot-miss)

| Feature | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|
| `rectal_tone_abnormal` | 8 | 2 | 18 | 107 | 5.56 (3.28-9.42) | 0.23 (0.07-0.81) | sacral_exam | no (in-person exam) | DERIVED |
| `perianal_sensation_abnormal` | 6 | 4 | 41 | 87 | 1.87 (1.06-3.30) | 0.59 (0.27-1.27) | sacral_exam | no (in-person exam) | DERIVED |
| `post_void_residual_abnormal` | 8 | 2 | 31 | 45 | 1.96 (1.30-2.96) | 0.34 (0.10-1.18) | sacral_exam | no (bladder scan) | DERIVED |

Derivation. Zusman 2022 Table 1 ("Characteristics of Subjects With and Without CES") gives normal, abnormal, and missing counts for 10 patients with CES and 132 without. We excluded missing values. The sensitivities and specificities agree with Table 2 (rectal tone 80%/86%, perianal sensation 60%/68%, PVR 80%/59%). The population is 142 ED patients with back pain who reported bowel or bladder dysfunction and had lumbar MRI and a spine consult. These LRs apply after a positive bladder or bowel history, not to all back pain. Bulbocavernosus reflex (3 of 10 vs 0 of 132 tested) is not a feature because 109 of 142 values are missing and a zero cell gives an infinite LR+.

`bladder_bowel_change` and `saddle_numbness` are rule-only `must_ask` features with no LR. A PRESENT answer escalates by `red_flag_action` (default).

Prior: p = 0.0008. The Hoeritzauer 2020 abstract: CES "occurred in 0.08% of those with low-back pain presenting to primary care in 1 study". Status: PLACEHOLDER (DS-5).

### Non-specific (mechanical) low back pain

LRs: none. Prior: p = 0.99. The Henschke 2009 abstract gives 11 of 1,172 (0.9%) with serious pathology. The complement is 99.1%, which we rounded to 0.99. Status: PLACEHOLDER (DS-5).

### Thresholds (illustrative)

| Diagnosis | B | R | test_se | test_sp | test_harm | T_test | T_treat | Reason |
|---|---|---|---|---|---|---|---|---|
| Vertebral fracture | 5 | 1 | 0.9 | 0.95 | 0.02 | 0.0154 | 0.6414 | Most fractures need imaging and pain care, not emergency care. Test = in-person exam and radiograph. Not sourced. |
| Spinal malignancy | 10 | 1 | 0.95 | 0.9 | 0.05 | 0.0156 | 0.6071 | Earlier diagnosis can prevent cord compression. Test = MRI. Not sourced. |
| Cauda equina syndrome | 100 | 1 | 0.95 | 0.95 | 0.05 | 0.0011 | 0.1513 | A delay can cause permanent bladder, bowel, and sexual dysfunction. Test = emergency MRI. Not sourced. |

## Abdominal pain script

Population: adults with acute abdominal pain. The appendicitis and gastroenteritis priors are from primary care (Viniol 2014). The bowel obstruction prior is from EDs (Laméris 2009). The ectopic pregnancy prior is from women of reproductive age in one ED (Köksal 2013).

### Acute appendicitis (cannot-miss)

All LRs are VERIFIED (secondary). Chopra 2015 reproduces the Wagner 1996 JAMA Rational Clinical Examination table under "Rational Clinical Examination Series: Does this patient have appendicitis?". The secondary table gives no CIs.

| Feature | Sens | Spec | LR+ | LR− | Group | Remote | Status |
|---|---|---|---|---|---|---|---|
| `migration_to_rlq` | 64% | 82% | 3.18 | 0.50 | rlq | yes | VERIFIED (secondary) |
| `rlq_pain` | 81% | 53% | 8.0 | 0.15 | rlq | yes | VERIFIED (secondary) |
| `no_similar_pain_before` | 81% | 41% | 1.5 | 0.32 | none | yes | VERIFIED (secondary) |
| `fever` | 67% | 79% | 1.94 | 0.58 | none | yes, home thermometer | VERIFIED (secondary) |
| `rigidity_exam` | 27% | 83% | 3.76 | 0.82 | peritoneal | no (in-person exam) | VERIFIED (secondary) |
| `rebound_tenderness_exam` | 63% | 69% | 3.7 | 0.4 | peritoneal | no (in-person exam) | VERIFIED (secondary) |
| `psoas_sign_exam` | 16% | 95% | 2.38 | 0.90 | peritoneal | no (in-person exam) | VERIFIED (secondary) |

Three cautions apply. First, the secondary table does not agree with itself for `rlq_pain`: sensitivity 81% and specificity 53% give LR+ 1.7, not 8.0. The table also does not agree for `rebound_tenderness_exam` (63%/69% gives LR+ 2.0). Wagner 1996 pooled several studies and reported ranges, so the single values can come from different studies. The reviewer must check the primary table before sign-off, and can delete `rlq_pain` if the primary value is not confirmed. Second, the source populations were patients with suspected appendicitis in hospital settings, not primary care. Third, "pain before vomiting" (LR+ 2.76, no LR−) is not a feature because the schema needs both LRs.

Prior: p = 0.019. Viniol 2014 abstract: appendicitis in 1.9% of primary-care patients who consult for abdominal pain. Status: PLACEHOLDER (DS-5). Laméris 2009 Table 1 gives 284 of 1,021 (28%) in Dutch EDs, which is not representative of a text-message population.

### Ectopic pregnancy (cannot-miss)

LRs: none. The Crochet 2013 abstract reports that all components of the patient history had LR+ less than 1.5, and gives LR+ only for the exam findings (cervical motion tenderness 4.9, adnexal mass 2.4, adnexal tenderness 1.9). See "Unverified and omitted".

`pregnancy_possible` is a rule-only `must_ask` feature with no LR. A PRESENT answer escalates by `red_flag_action` (default) to same-day hCG and ultrasound.

Prior: p = 0.0429. Köksal 2013 Results text: 68 ectopic pregnancies among 1,586 women of reproductive age who had a pregnancy test in a Turkish university ED, 2006 to 2010 (4.29%). Of these women, 954 (60.15%) had abdominal pain. The script applies the prior to every caller, including men and women past menopause. This is the conservative direction, but it puts ectopic pregnancy in the middle zone for every encounter (see "Engine behavior"). Status: PLACEHOLDER (DS-5).

### Bowel obstruction (cannot-miss)

| Feature | LR+ | LR− | Remote | Status |
|---|---|---|---|---|
| `prior_abdominal_surgery` | 3.86 | 0.19 | yes | DERIVED |
| `abdominal_distension_exam` | 16.8 | 0.27 | no (in-person exam) | VERIFIED (secondary) |

Derivation for `prior_abdominal_surgery`. Catena 2019 ("Initial patient assessment") states that a history of previous abdominal surgery has 85% sensitivity and 78% specificity to predict adhesive small bowel obstruction, and cites Taylor 2013. $LR^{+} = 0.85/0.22 = 3.86$ and $LR^{-} = 0.15/0.78 = 0.19$. No counts, so no CI.

`abdominal_distension_exam`. Catena 2019 states that abdominal distension has LR+ 16.8 and LR− 0.27, and cites Böhner 1998. The Böhner 1998 abstract states that the cohort (1,254 patients, 48 with bowel obstruction) excluded patients with a history of abdominal injury including surgery. Thus this LR applies to patients without prior surgery, and it is in a different population from the `prior_abdominal_surgery` LR.

The two features have no group. They come from different studies and populations.

Prior: p = 0.067. Laméris 2009 Table 1: bowel obstruction 68 of 1,021 (7%) adults with non-traumatic abdominal pain of 2 hours to 5 days in 6 Dutch EDs. The study excluded pregnancy and patients discharged with no imaging. Status: PLACEHOLDER (DS-5). This is an ED value, so it is high for a primary-care or text-message population.

### Gastroenteritis

LRs: none. Prior: p = 0.187. Viniol 2014 abstract: gastroenteritis in 7.2% to 18.7% of primary-care abdominal pain. We used the upper value. Status: PLACEHOLDER (DS-5).

### Thresholds (illustrative)

| Diagnosis | B | R | test_se | test_sp | test_harm | T_test | T_treat | Reason |
|---|---|---|---|---|---|---|---|---|
| Appendicitis | 30 | 1 | 0.95 | 0.95 | 0.05 | 0.0035 | 0.3673 | Delay increases perforation. Test = in-person exam and CT or ultrasound. Not sourced. |
| Ectopic pregnancy | 100 | 1 | 0.9 | 0.9 | 0.02 | 0.0013 | 0.0807 | Rupture can cause death from bleeding. Test = hCG and transvaginal ultrasound. Not sourced. |
| Bowel obstruction | 30 | 1 | 0.9 | 0.9 | 0.05 | 0.0055 | 0.2179 | Strangulation can cause bowel ischemia. Test = in-person exam and CT. Not sourced. |

## Red-flag rules (`must_ask` and `red_flag_action`)

The engine asks every `must_ask` feature before it can complete an encounter. A PRESENT `must_ask` finding acts by rule: escalate (default) or defer, as `red_flag_action` sets. These choices are drafts for the CPD.

| Script | must_ask feature | Action if present | Reason |
|---|---|---|---|
| headache | `loss_of_consciousness` | escalate | SAH red flag (Perry 2010 Rule 1) |
| headache | `fever` | escalate | Meningitis red flag; no sourced LR |
| headache | `neck_pain_stiffness` | defer | 30.9% of patients without SAH report it (Perry 2010 Table 2) |
| focal_neuro_dizziness | `unilateral_weakness`, `speech_disturbance`, `diplopia` | escalate | Focal symptoms; LR+ 7.7 to 19.7 |
| focal_neuro_dizziness | `gait_disturbance` | defer | 15% of patients without a serious cause report it (Navi 2012 Table 2) |
| low_back_pain | `significant_trauma`, `prolonged_steroids`, `previous_cancer` | defer | Need clinician review and imaging, not emergency care |
| low_back_pain | `bladder_bowel_change`, `saddle_numbness` | escalate | CES red flags; no sourced LR |
| abdominal_pain | `pregnancy_possible` | escalate | Ectopic pregnancy; no sourced LR |
| abdominal_pain | `rlq_pain`, `prior_abdominal_surgery` | defer | Common without disease |

## Engine behavior with these numbers

We ran `step(script, WorkupState(findings=[]))` for each script and some smoke cases with confirmed findings.

- **headache.** First step ASK (`neck_pain_stiffness`, `vomiting`). SAH and meningitis are in the middle zone; mass is just below T_test (prior 0.01, T_test 0.0105), so the engine marks it ruled out. A small change to the mass prior or thresholds will move it into the middle zone, and then every headache defers because mass has no remote features. With all red flags negative, SAH falls below T_test, but meningitis stays in the middle zone after `jolt_accentuation`, and the engine returns DEFER (`cannot_miss_middle_zone_no_remote_test`). Neck pain with loss of consciousness returns ESCALATE.
- **focal_neuro_dizziness.** First step ASK (`unilateral_weakness`, `speech_disturbance`). One-sided weakness returns ESCALATE (p = 0.46, p95 = 0.66). With all five history features negative, the stroke posterior is 0.019 (p95 0.025), which is above T_test (0.0055), so the engine returns DEFER. No remote history answer can rule out stroke at these thresholds.
- **low_back_pain.** First step ASK (`significant_trauma`, `prolonged_steroids`). All three cannot-miss priors are below T_test. With all red flags negative, the engine returns COMPLETE. A prior cancer or steroid use returns DEFER by rule; a bladder or bowel change returns ESCALATE by rule.
- **abdominal_pain.** First step DEFER (`cannot_miss_middle_zone_no_remote_test`). Ectopic pregnancy has no remote features and its prior (0.0429) is between T_test (0.0013) and T_treat (0.0807). The abdominal-pain lane cannot close or even ask questions until the reviewer chooses one of these options: (1) gate the script on sex and age so that ectopic pregnancy applies only to people who can be pregnant, and route `pregnancy_possible` to the pelvic pain and possible pregnancy script; (2) remove ectopic pregnancy from this script and make `pregnancy_possible` a lane-gate exclusion; or (3) add sourced remote LRs.

## Unverified and omitted

| Item | Reason |
|---|---|
| Detsky 2006 neuroimaging predictors for intracranial abnormality (cluster-type headache LR 10.7, abnormal neuro exam 5.3, undefined headache 3.8, aura 3.2, exertion or Valsalva 2.3, vomiting 1.8) and POUND migraine criteria | [UNVERIFIED — omitted]. Detsky ME, McDonald DR, Baerlocher MO, et al. Does this patient with headache have a migraine or need neuroimaging? *JAMA*. 2006;296(10):1274-1283 (PMID 16968852, doi:10.1001/jama.296.10.1274). The abstract gives LR+ only and states that "no clinical features were useful in ruling out significant pathologic conditions". We could not get the full-text table with LR−. This leaves the mass diagnosis with no LRs. |
| Ottawa SAH rule (sensitivity 100%) | [UNVERIFIED — omitted]. A rule is not a single patient question, and an LR− of 0 does not pass the schema. Carpenter 2016 Results text gives LR− 0.02 (0.00-0.39) for the Ottawa SAH Rule; the lower CI bound is 0. |
| Carpenter 2016 pooled history LRs (neck pain LR+ 4.12, neck stiffness on exam LR+ 6.59) | [UNVERIFIED — omitted]. The pooled values are in forest plots that we could not read as text, and the text gives no pooled LR−. We used Perry 2010 counts instead. |
| Fever, nausea or vomiting, altered mental status for meningitis (Attia 1999) | [UNVERIFIED — omitted]. Attia J, Hatala R, Cook DJ, Wong JG. The rational clinical examination. Does this adult patient have acute meningitis? *JAMA*. 1999;282(2):175-181 (PMID 10411200, doi:10.1001/jama.282.2.175). The abstract gives sensitivities only (headache 50%, nausea or vomiting 30%) and jolt accentuation LR− 0. `fever` is a rule-only red flag. |
| Head trauma, age over 50, history of neoplasm for serious secondary headache (Chu 2024, SNNOOP10) | [UNVERIFIED — omitted]. Chu K, Kelly AM, Kuan WS, et al. *Emerg Med J*. 2024;41(6):368-375 (PMID 38658053, doi:10.1136/emermed-2023-213461). The target is any serious secondary headache, and the full text was not available (HTTP 403). |
| Face, arm, speech composite for stroke (Goldstein 2005: LR 5.5 [3.3-9.1] for 1 or more findings, 0.39 [0.25-0.61] for none) | [UNVERIFIED — omitted]. Goldstein LB, Simel DL. Is this patient having a stroke? *JAMA*. 2005;293(19):2391-2402 (PMID 15900010, doi:10.1001/jama.293.19.2391). The values are in the abstract, but they are clinician-exam findings in patients with neurologic symptoms, and they overlap with the Navi 2012 focal-symptom features. The reviewer can add them in group `focal_symptoms`. |
| Craniocervical pain for stroke in AVS (Tarnutzer 2011 Table 3: PLR 3.2) and other Table 3 items | [UNVERIFIED — omitted]. Table 3 gives LR+ or LR− alone, with no CI. |
| Combined HINTS (LR− 0.02) and INFARCT | [UNVERIFIED — omitted] as features. A combined exam is not one finding. The single components are in group `hints`. |
| Peripheral vertigo history LRs (positional trigger, hearing loss) | [UNVERIFIED — omitted]. No paired LRs found in a table that we read. |
| Cauda equina history red flags (urinary retention, incontinence, saddle anesthesia) | [UNVERIFIED — omitted] as LRs. Dionne N, Adefolarin A, Kunzelman D, et al. What is the diagnostic accuracy of red flags related to cauda equina syndrome (CES), when compared to Magnetic Resonance Imaging (MRI)? A systematic review. *Musculoskelet Sci Pract*. 2019;42:125-133 (PMID 31132655, doi:10.1016/j.msksp.2019.05.004). The abstract gives only ranges (pooled sensitivity 0.19 to 0.43, specificity 0.62 to 0.88). The full text was not available (HTTP 403). The features are rule-only red flags. |
| Spinal infection (epidural abscess, vertebral osteomyelitis) | [UNVERIFIED — omitted] as a diagnosis. No sourced prior or paired LRs in a primary-care back-pain population. Galliker G, et al. *Am J Med*. 2020;133(1):60-72 (PMID 31278933) reports ED prevalence ranges and names intravenous drug use and indwelling catheter as red flags in its abstract, without values. The lane gate can add fever plus injection drug use as a hard rule. |
| Abdominal aortic aneurysm (back pain and abdominal pain) | [UNVERIFIED — omitted] as a diagnosis. We found no sourced prior in a back-pain or abdominal-pain population. Lederle FA, Simel DL. The rational clinical examination. Does this patient have abdominal aortic aneurysm? *JAMA*. 1999;281(1):77-82 (PMID 9892455) gives abdominal palpation LRs (LR+ 12.0, LR− 0.72 for AAA 3.0 cm or more, as quoted in a secondary PMC source, PMC11126164), but these come from screening populations, and palpation is an in-person exam. The lane gate can add age 60 or more with sudden severe abdominal or back pain and fainting as a hard escalation rule. |
| Ectopic pregnancy history and exam LRs | [UNVERIFIED — omitted]. Crochet 2013 abstract: all history items LR+ less than 1.5; exam LRs given as LR+ only. Tans A, et al. *BJGP Open*. 2024;8(3):BJGPO.2023.0245 (PMC11523522) reports flank pain LR− 0.12 and cervical motion tenderness LR+ 5.62 and 8.60 from Buckley 1999 and Birkhahn 2002, but each without the paired LR. Its supplementary tables did not download. |
| Pain before vomiting for appendicitis (Wagner 1996: LR+ 2.76, no LR−) | [UNVERIFIED — omitted]. No LR−. |
| Visible peristalsis (LR+ 18.8) and abnormal bowel sounds (LR+ 5.0) for obstruction | [UNVERIFIED — omitted]. LR+ only (Chopra 2015). |
| Adult Appendicitis Score, Alvarado score, AIR score (Sammalkorpi 2014, PMC4087125, Table 4) | [UNVERIFIED — omitted] as features. They need laboratory values. |
| Feature `cost`, `harm`, `leak` | Not set (defaults). No fee-schedule or leak source was given. The engine calculates the leak from the LRs. |
