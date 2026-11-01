# Illness-script sources: sinus, cough, red eye, ear pain

This file lists the source of each number in these four scripts:

- `compass_pcp/data/scripts/acute_sinusitis.yaml` (version 0.1.0-draft, lane `uri`)
- `compass_pcp/data/scripts/cough_acute.yaml` (version 0.1.0-draft, lane `uri`)
- `compass_pcp/data/scripts/red_eye.yaml` (version 0.1.0-draft, lane `conjunctivitis`)
- `compass_pcp/data/scripts/ear_pain.yaml` (version 0.1.0-draft, lane `uri`)

All four scripts are drafts for physician sign-off. `clinical_review.approved_by` is null in all four files.

Status labels (the same as `SCRIPT_SOURCES.md`):

- **VERIFIED.** The value is copied from a table that we read in the source article.
- **DERIVED.** We calculated the value from counts or estimates in a table or text that we read. The calculation is given.
- **PLACEHOLDER.** The value is a literature value that a Waymark claims rate (DS-5) or a CPD decision-analysis memo must replace.
- **[UNVERIFIED — omitted].** We did not put the value in a script.

We calculated derived 95% CIs for likelihood ratios (LRs) with the log method (Simel DL, Samsa GP, Matchar DB. Likelihood ratios with confidence: sample size estimation for diagnostic test studies. *J Clin Epidemiol*. 1991;44(8):763-770. PMID 1941027): $SE(\ln LR^{+}) = \sqrt{1/a - 1/(a+c) + 1/b - 1/(b+d)}$, where $a$ is true positives, $c$ is false negatives, $b$ is false positives, and $d$ is true negatives. We calculated $LR^{-}$ in the same way.

For a complement diagnosis (for example, "not bacterial" when the source compares bacterial with not bacterial), $LR^{+}_{\text{complement}} = 1/LR^{+}$ and $LR^{-}_{\text{complement}} = 1/LR^{-}$. The CI limits are the reciprocals of the CI limits. This is the method that `sore_throat.yaml` uses.

## Summary of value status

| Script | VERIFIED LRs | DERIVED LRs | PLACEHOLDER priors | PLACEHOLDER thresholds | LRs omitted |
|---|---|---|---|---|---|
| acute_sinusitis | 6 | 6 | 3 | 1 | see below |
| cough_acute | 4 | 19 | 3 | 1 | see below |
| red_eye | 0 | 11 | 3 | 1 | see below |
| ear_pain | 0 | 0 | 3 | 1 | all (none found) |
| Total | 10 | 36 | 12 | 4 | |

## Sources that we read

| Key | Citation | Access |
|---|---|---|
| Ebell 2019 | Ebell MH, McKay B, Dale A, Guilbault R, Ermias Y. Accuracy of signs and symptoms for the diagnosis of acute rhinosinusitis and acute bacterial rhinosinusitis. *Ann Fam Med*. 2019;17(2):164-172. PMID 30858261. doi:10.1370/afm.2354 | PMC6411403, Tables 1 to 5 (read from the HTML table markup) |
| Hansen 2012 | Hansen FS, Hoffmans R, Georgalas C, Fokkens WJ. Complications of acute rhinosinusitis in The Netherlands. *Fam Pract*. 2012;29(2):147-153 (epub 2011). PMID 21896505. doi:10.1093/fampra/cmr062 | Abstract only |
| van Vugt 2013 | van Vugt SF, Broekhuizen BDL, Lammens C, et al. Use of serum C reactive protein and procalcitonin concentrations in addition to symptoms and signs to predict pneumonia in patients presenting to primary care with acute cough: diagnostic study. *BMJ*. 2013;346:f2450. PMID 23633005. doi:10.1136/bmj.f2450 | PMC3639712, Tables 1 to 4 (NCBI efetch JATS XML) |
| Teepe 2015 | Teepe J, Broekhuizen BDL, Ieven M, et al. Prevalence, diagnosis, and disease course of pertussis in adults with acute cough: a prospective, observational study in primary care. *Br J Gen Pract*. 2015;65(639):e662-e667. PMID 26412843. doi:10.3399/bjgp15X686917 | PMC4582879, Tables 1 to 3 and Results text |
| Ebell 2017 | Ebell MH, Marchello C, Callahan M. Clinical diagnosis of *Bordetella pertussis* infection: a systematic review. *J Am Board Fam Med*. 2017;30(3):308-319. PMID 28484063. doi:10.3122/jabfm.2017.03.160330 | Full-text PDF from jabfm.org, Table 3 |
| Marchello 2019 | Marchello CS, Ebell MH, Dale AP, Harvill ET, Shen Y, Whalen CC. Signs and symptoms that rule out community-acquired pneumonia in outpatient adults: a systematic review and meta-analysis. *J Am Board Fam Med*. 2019;32(2):234-247. PMID 30850460. doi:10.3122/jabfm.2019.02.180219 | PMC7422644, Tables 1 to 4. Read for the reviewer; no value is in a script |
| Rietveld 2004 | Rietveld RP, ter Riet G, Bindels PJE, Sloos JH, van Weert HCPM. Predicting bacterial cause in infectious conjunctivitis: cohort study on informativeness of combinations of signs and symptoms. *BMJ*. 2004;329(7459):206-210. PMID 15201195. doi:10.1136/bmj.38128.631319.AE | PMC487734, Tables 1 to 4 (read twice through the PMC page) |
| Narayana 2015 | Narayana S, McGee S. Bedside diagnosis of the "red eye": a systematic review. *Am J Med*. 2015;128(11):1220-1224.e1. PMID 26169885. doi:10.1016/j.amjmed.2015.06.026 | Abstract only (publisher page returned HTTP 403). Used only as a cross-check |
| Yaphe 2003 | Yaphe J, Pandher KS. The predictive value of the penlight test for photophobia for serious eye pathology in general practice. *Fam Pract*. 2003;20(4):425-427. PMID 12876115. doi:10.1093/fampra/cmg416 | Abstract only (counts are in the abstract) |
| Petersen 2007 | Petersen I, Johnson AM, Islam A, Duckworth G, Livermore DM, Hayward AC. Protective effect of antibiotics against serious complications of common respiratory tract infections: retrospective cohort study with the UK General Practice Research Database. *BMJ*. 2007;335(7627):982. PMID 17947744. doi:10.1136/bmj.39345.405243.BE | PMC2072032, Table 3 and Methods text |
| Rijk 2021 | Rijk MH, Hullegie S, Schilder AGM, Kortekaas MF, Damoiseaux RAMJ, Verheij TJM, Venekamp RP. Incidence and management of acute otitis media in adults: a primary care-based cohort study. *Fam Pract*. 2021;38(4):448-453. PMID 33506857. doi:10.1093/fampra/cmaa150 | Abstract only |
| Piercefield 2011 | Piercefield EW, Collier SA, Hlavsa MC, Beach MJ. Estimated burden of acute otitis externa — United States, 2003-2007. *MMWR Morb Mortal Wkly Rep*. 2011;60(19):605-609. [UNVERIFIED — check manually: volume, issue, and pages were not printed on the web page that we read] | cdc.gov/mmwr/preview/mmwrhtml/mm6019a2.htm, Results text and Table |

## Acute sinusitis script

Population: adults with clinically suspected acute rhinosinusitis (ARS) in primary care, ED, or ENT clinics. These are the populations of the Ebell 2019 ABRS studies (Table 1: Berg 1981, 1985, 1988; Hansen 1995; van Buchem 1995; Laine 1998; Autio 2015).

### Acute bacterial rhinosinusitis (ABRS)

All LRs are from Ebell 2019 Table 4 ("Accuracy of Signs and Symptoms of ABRS Diagnosed by Purulent Antral Puncture or Positive Bacterial Culture"). The second column header in Table 4 prints "Sensitivity" twice. The values in that column are specificities. Ebell 2019 does not report the number of patients for each finding.

| Feature | Table 4 row | Studies | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|---|
| `cacosmia` | Cacosmia | 3 | 4.3 (0.94-14) | 0.86 (0.76-0.99) | none | yes | VERIFIED |
| `tooth_pain` | Pain in teeth | 3 | 2.0 (1.1-3.7) | 0.77 (0.50-0.96) | facial_pain | yes | VERIFIED |
| `purulent_nasal_discharge` | Purulent nasal discharge (symptom) | 3 | 1.3 (0.99-1.6) | 0.74 (0.47-1.0) | purulence | yes | VERIFIED |
| `pain_bending_forward` | Pain bending forward | 3 | 1.0 (0.87-1.3) | 0.95 (0.69-1.3) | facial_pain | yes | VERIFIED |
| `maxillary_tenderness` | Sinus tenderness, maxillary (physical examination) | 5 | 0.86 (0.23-2.2) | 1.2 (0.55-2.1) | facial_pain | yes, guided self-exam (press on cheeks) | VERIFIED |
| `purulent_discharge_exam` | Nasal discharge, purulent (physical examination) | 5 | 0.88 (0.36-1.9) | 1.2 (0.57-1.8) | purulence | no (in-person exam) | VERIFIED |

Groups. `facial_pain` holds tooth pain, pain on bending forward, and maxillary tenderness. `purulence` holds the reported and the examined purulent discharge. Ebell 2019 does not report the joint accuracy of these findings. With a group, only the strongest finding counts.

Prior: p = 0.31. Ebell 2019 Table 2 ("Prevalence of ARS and ABRS in the Included Study Populations") gives the pooled ABRS prevalence by bacterial culture as 31% (95% CI, 24%-40%) in 3 studies (Hansen 1995, 174 patients, 35%; van Buchem 1995, 113 patients, 34%; Autio 2015, 43 patients, 19%). The pooled prevalence by purulent antral puncture is 49% (45%-53%). We used the culture value. Status: PLACEHOLDER (DS-5).

### Viral or other non-bacterial sinus symptoms

Definition: the complement of ABRS in the Ebell 2019 Table 4 studies. Prior p = 0.69 (complement of 0.31). Status: PLACEHOLDER (DS-5).

| Feature | LR+ (95% CI) | LR− (95% CI) | Status |
|---|---|---|---|
| `cacosmia` | 0.23 (0.07-1.06) | 1.16 (1.01-1.32) | DERIVED (reciprocal) |
| `tooth_pain` | 0.50 (0.27-0.91) | 1.30 (1.04-2.00) | DERIVED (reciprocal) |
| `purulent_nasal_discharge` | 0.77 (0.62-1.01) | 1.35 (1.00-2.13) | DERIVED (reciprocal) |
| `pain_bending_forward` | 1.00 (0.77-1.15) | 1.05 (0.77-1.45) | DERIVED (reciprocal) |
| `maxillary_tenderness` | 1.16 (0.45-4.35) | 0.83 (0.48-1.82) | DERIVED (reciprocal) |
| `purulent_discharge_exam` | 1.14 (0.53-2.78) | 0.83 (0.56-1.75) | DERIVED (reciprocal) |

### Orbital or intracranial complication (cannot-miss)

Prior: p = 0.00003. The Hansen 2012 abstract gives severe ARS complications in an estimated 1 in 32,000 adult ARS cases (1 in 12,000 pediatric cases) in The Netherlands in 2004. The study found 47 hospitalized patients with 48 complications (16 intracranial, 32 orbital). We read only the abstract. Status: PLACEHOLDER (DS-5).

LRs: none. See "Unverified and omitted".

`must_ask`: `periorbital_swelling`, `vision_change`, `severe_headache`, `confusion_or_drowsiness`. These features have no LRs. See "Engine behavior".

Thresholds (illustrative, source string "PLACEHOLDER: CPD decision-analysis memo; illustrative values"):

| Input | Value | Reason |
|---|---|---|
| benefit B | 100 | An untreated orbital or intracranial complication can cause vision loss or death. Same-day in-person care when it is present has a very large net benefit. |
| harm R | 1 | The unit of harm is one unnecessary same-day in-person visit. |
| test_se | 0.95 | Illustrative sensitivity of an in-person evaluation with imaging. Not sourced. |
| test_sp | 0.90 | Illustrative specificity of the same evaluation. Not sourced. |
| test_harm | 0.02 | Burden of the visit and imaging. |

The engine calculates T_test = 0.0013 and T_treat = 0.149. The prior (0.00003) is below T_test, so the engine marks the complication as ruled out at the start.

## Acute cough script

Population: adults with acute cough (28 days or less) in primary care. The pneumonia and pertussis values come from the same cohort (GRACE, 12 European countries, 2007-2010).

### Community-acquired pneumonia (cannot-miss)

Reference standard: pneumonia on a chest radiograph within 7 days, judged by radiologists blind to other data (van Vugt 2013 Methods). All LRs are DERIVED from van Vugt 2013 Table 1 ("Association between diagnostic variables and pneumonia in 2820 patients presenting with acute cough in primary care"). Table 1 gives the number of all patients with each finding and the number of patients with pneumonia and the finding. We calculated TP = pneumonia with the finding, FN = 140 − TP, FP = all with the finding − TP, TN = 2680 − FP. Table 1 also reports a few missing values for each variable (0 to 67). We counted missing values as absent, because Table 1 does not report missing values by pneumonia status. The effect on the LRs is small (at most 2.4% missing, for tachypnoea, which is not used).

| Feature | Table 1 row | All, n | Pneumonia, n | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `fever_history` | Fever (history, day 1) | 989 | 82 | 82 | 58 | 907 | 1773 | 1.73 (1.49-2.01) | 0.63 (0.51-0.76) | fever | yes |
| `measured_temperature_high` | Temperature >37.8 °C | 158 | 22 | 22 | 118 | 136 | 2544 | 3.10 (2.04-4.70) | 0.89 (0.83-0.95) | fever | yes, guided self-measurement with a home thermometer |
| `breathlessness` | Breathlessness | 1594 | 96 | 96 | 44 | 1498 | 1182 | 1.23 (1.09-1.38) | 0.71 (0.56-0.91) | none | yes |
| `runny_nose_absent` | Runny nose absent | 808 | 61 | 61 | 79 | 747 | 1933 | 1.56 (1.28-1.91) | 0.78 (0.68-0.91) | none | yes |
| `chest_pain` | Chest pain | 1304 | 80 | 80 | 60 | 1224 | 1456 | 1.25 (1.08-1.45) | 0.79 (0.65-0.96) | none | yes |
| `phlegm` | Phlegm | 2239 | 120 | 120 | 20 | 2119 | 561 | 1.08 (1.01-1.16) | 0.68 (0.45-1.03) | none | yes |
| `pulse_over_100` | Tachycardia (pulse >100 beats/min) | 111 | 17 | 17 | 123 | 94 | 2586 | 3.46 (2.13-5.64) | 0.91 (0.86-0.97) | none | yes, guided self-count of the wrist pulse (more than 50 in 30 seconds), or a watch or pulse oximeter |
| `crackles` | Crackles | 265 | 45 | 45 | 95 | 220 | 2460 | 3.92 (2.98-5.14) | 0.74 (0.66-0.83) | none | no (in-person exam) |
| `diminished_breath_sounds` | Diminished vesicular breathing | 362 | 31 | 31 | 109 | 331 | 2349 | 1.79 (1.29-2.49) | 0.89 (0.81-0.97) | none | no (in-person exam) |

Status: all DERIVED. The source measured temperature and pulse in the clinic. The accuracy of self-measurement at home was not studied. The reviewer can set `remote_askable: false` for `measured_temperature_high` and `pulse_over_100` if the self-measurements are not accepted.

Group `fever` holds the reported fever and the measured temperature. Only the stronger finding counts.

Prior: p = 0.050. van Vugt 2013 Table 1 gives radiographic pneumonia in 140 of 2820 adults (5.0%). For comparison, Marchello 2019 Table 4 uses simulated prevalences of 4% (primary care) and 20% (ED). The Ebell 2020 abstract (PMID 32329557) gives a CAP prevalence of 10% in 9 primary-care studies. Status: PLACEHOLDER (DS-5).

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 10 | Prompt antibiotics and follow-up for pneumonia reduce complications. Most outpatient pneumonia in adults under 65 is not severe, so B is lower than for an orbital complication or an abscess. |
| harm R | 1 | One unnecessary same-day visit and chest radiograph. |
| test_se | 0.90 | Illustrative sensitivity of an in-person exam with a chest radiograph. Not sourced. |
| test_sp | 0.95 | Illustrative specificity of the same evaluation. Not sourced. |
| test_harm | 0.05 | Burden of the visit, radiation, and cost. |

The engine calculates T_test = 0.0110 and T_treat = 0.462.

### Acute bronchitis or other non-pneumonia cough

Definition: no radiographic pneumonia in van Vugt 2013 (the complement of pneumonia). This diagnosis includes pertussis, influenza, COVID-19, and other viral infections. Prior p = 0.950 (2680 of 2820). Status: PLACEHOLDER (DS-5).

| Feature | LR+ (95% CI) | LR− (95% CI) | Status |
|---|---|---|---|
| `fever_history` | 0.58 (0.50-0.67) | 1.60 (1.31-1.95) | DERIVED (reciprocal) |
| `measured_temperature_high` | 0.32 (0.21-0.49) | 1.13 (1.05-1.21) | DERIVED (reciprocal) |
| `breathlessness` | 0.82 (0.73-0.92) | 1.40 (1.09-1.80) | DERIVED (reciprocal) |
| `runny_nose_absent` | 0.64 (0.52-0.78) | 1.28 (1.10-1.48) | DERIVED (reciprocal) |
| `chest_pain` | 0.80 (0.69-0.93) | 1.27 (1.04-1.54) | DERIVED (reciprocal) |
| `phlegm` | 0.92 (0.86-0.99) | 1.47 (0.97-2.21) | DERIVED (reciprocal) |
| `pulse_over_100` | 0.29 (0.18-0.47) | 1.10 (1.03-1.17) | DERIVED (reciprocal) |
| `crackles` | 0.26 (0.19-0.34) | 1.35 (1.21-1.52) | DERIVED (reciprocal) |
| `diminished_breath_sounds` | 0.56 (0.40-0.77) | 1.13 (1.03-1.23) | DERIVED (reciprocal) |

### Pertussis

Reference standard in Teepe 2015: PCR of a nasopharyngeal swab or sputum, or anti-pertussis-toxin IgG of 125 IU/mL or more at day 28. Ebell 2017 pooled studies that used PCR, culture, or serology.

| Feature | Source row | LR+ (95% CI) | LR− (95% CI) | Group | Remote | Status |
|---|---|---|---|---|---|---|
| `paroxysmal_cough` | Ebell 2017 Table 3, Paroxysmal cough, Adults (6/6 studies) | 1.2 (1.04-1.6) | 0.50 (0.33-0.75) | pertussis_cough_pattern | yes | VERIFIED |
| `posttussive_vomiting` | Ebell 2017 Table 3, Posttussive vomiting, Adults (7/8 studies) | 1.7 (1.3-2.3) | 0.83 (0.73-0.93) | pertussis_cough_pattern | yes | VERIFIED |
| `whoop` | Ebell 2017 Table 3, Whooping cough, Adults (7/8 studies) | 1.2 (0.81-1.8) | 0.97 (0.81-1.8) | pertussis_cough_pattern | yes | VERIFIED |
| `fever_history` | Ebell 2017 Table 3, Fever, all ages (7/8 studies) | 0.76 (0.45-1.2) | 1.0 (0.95-1.1) | fever | yes | VERIFIED (no adult-only row) |
| `cough_over_2_weeks` | Teepe 2015 Table 2, Cough duration >2 weeks before index consultation: 525 of 3074 all, 25 of 93 pertussis | 1.60 (1.14-2.26) | 0.88 (0.78-0.99) | none | yes | DERIVED: TP 25, FN 68, FP 500, TN 2481; Table 2 reports 45 missing values, counted as absent |

Group `pertussis_cough_pattern`. Whoop and vomiting after a cough come after paroxysms, so these findings are not independent. Only the strongest counts.

Prior: p = 0.030. Teepe 2015 Table 1 and Results text: acute pertussis in 93 of 3074 adults with acute cough (3%, 95% CI, 2.5%-3.7%). The prevalence in adults with cough for more than 2 weeks was 25 of 525 (5%). Ebell 2017 gives 12.4% in primary-care patients with prolonged cough. Status: PLACEHOLDER (DS-5).

Pertussis is not cannot-miss in this draft. The reviewer must decide if it needs thresholds (for example, for household contacts with infants or for pregnancy).

## Red-eye script

Population: adults with a red eye in primary care. The lane gate must exclude contact lens wearers and eye injury (YAML comment).

### Bacterial conjunctivitis

Source population (Rietveld 2004): 184 consecutive adults in 25 Dutch health centres with a red eye and either (muco)purulent discharge or a glued eyelid, not wearing contact lenses. 177 were analyzed. Reference standard: bacterial culture. All LRs are DERIVED from Rietveld 2004 Table 1 ("Baseline characteristics and index test results"), which gives counts for culture-positive (n = 57) and culture-negative (n = 120) patients.

| Feature | Table 1 row | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Group | Remote |
|---|---|---|---|---|---|---|---|---|---|
| `both_eyes_glued` | Glued eyes in the morning: two (22 vs 13) | 22 | 35 | 13 | 107 | 3.56 (1.94-6.55) | 0.69 (0.56-0.85) | glued_bilateral | yes |
| `any_eye_glued` | Glued eyes: one (30 vs 74) plus two (22 vs 13), compared with none (5 vs 33) | 52 | 5 | 87 | 33 | 1.26 (1.10-1.44) | 0.32 (0.13-0.77) | glued_bilateral | yes |
| `bilateral_redness` | Bilateral involvement (21 vs 19) | 21 | 36 | 19 | 101 | 2.33 (1.36-3.97) | 0.75 (0.61-0.93) | glued_bilateral | yes, patient report or photo |
| `itching` | Itching (33 vs 76) | 33 | 24 | 76 | 44 | 0.91 (0.70-1.19) | 1.15 (0.78-1.69) | none | yes |
| `history_conjunctivitis` | History of conjunctivitis (5 vs 25) | 5 | 52 | 25 | 95 | 0.42 (0.17-1.04) | 1.15 (1.02-1.30) | none | yes |

Cross-check. The Narayana 2015 abstract gives pooled values of LR 3.6 (95% CI, 1.9-6.5) for matting of both eyes and LR 0.3 (0.1-0.8) for absence of morning gluing of either eye. These agree with our derived `both_eyes_glued` LR+ (3.56) and `any_eye_glued` LR− (0.32).

Group `glued_bilateral`. Two glued eyes implies two involved eyes, and any gluing includes two glued eyes. Only the strongest finding counts.

The Table 1 percentages in the PMC page do not always match the counts when rounded (for example, 5 of 57 is printed as 8%). The counts in each row add up to 57 and 120. We used the counts.

Prior: p = 0.32. Rietveld 2004 Results: positive culture in 57 of 177 (32%). This prior applies to adults with discharge or glued eyelids. It does not apply to all red eyes. Status: PLACEHOLDER (DS-5).

### Non-bacterial conjunctivitis

Definition: culture-negative patients in Rietveld 2004 (the complement). This includes viral conjunctivitis and possibly allergic or irritant conjunctivitis. Prior p = 0.68 (120 of 177). Status: PLACEHOLDER (DS-5).

| Feature | LR+ (95% CI) | LR− (95% CI) | Status |
|---|---|---|---|
| `both_eyes_glued` | 0.28 (0.15-0.52) | 1.45 (1.17-1.80) | DERIVED (reciprocal) |
| `any_eye_glued` | 0.79 (0.69-0.91) | 3.13 (1.29-7.60) | DERIVED (reciprocal) |
| `bilateral_redness` | 0.43 (0.25-0.73) | 1.33 (1.08-1.65) | DERIVED (reciprocal) |
| `itching` | 1.09 (0.84-1.42) | 0.87 (0.59-1.28) | DERIVED (reciprocal) |
| `history_conjunctivitis` | 2.38 (0.96-5.88) | 0.87 (0.77-0.98) | DERIVED (reciprocal) |

### Serious eye disease (cannot-miss)

Definition (Yaphe 2003): serious pathology on slit-lamp exam, mainly uveitis and keratitis. The script label also names acute angle-closure glaucoma and scleritis, as in Narayana 2015. The reviewer must confirm the label.

| Feature | Source | TP | FN | FP | TN | LR+ (95% CI) | LR− (95% CI) | Remote | Status |
|---|---|---|---|---|---|---|---|---|---|
| `penlight_photophobia` | Yaphe 2003 abstract: penlight test positive in 8 of 10 with serious pathology and negative in 21 of 26 with less serious pathology | 8 | 2 | 5 | 21 | 4.16 (1.78-9.70) | 0.25 (0.07-0.87) | yes, guided self-test with a phone flashlight; source used a clinician penlight | DERIVED |

Two cautions apply. First, the Yaphe 2003 abstract says 30 patients, but the counts add up to 36. The unit can be eyes. The reviewer must check the full text. Second, the sample is small, so the CIs are wide. The Narayana 2015 abstract gives a pooled LR of 8.3 (95% CI, 2.7-25.9) for photophobia by direct illumination, but no LR−. We could not read its tables.

Prior: p = 0.28. Yaphe 2003 abstract: 10 of 36 (28%) red eyes had serious pathology in one general practice. This is a small, single-practice sample. Status: PLACEHOLDER (DS-5).

`must_ask`: `vision_change`, `severe_eye_pain`, `contact_lens_wearer`, `penlight_photophobia`. Only `penlight_photophobia` has an LR.

Thresholds (illustrative):

| Input | Value | Reason |
|---|---|---|
| benefit B | 30 | Prompt treatment of keratitis, iritis, or angle-closure glaucoma prevents vision loss. |
| harm R | 1 | One unnecessary same-day eye exam. |
| test_se | 0.95 | Illustrative sensitivity of a slit-lamp exam. Not sourced. |
| test_sp | 0.90 | Illustrative specificity of a slit-lamp exam. Not sourced. |
| test_harm | 0.02 | Burden of the visit. |

The engine calculates T_test = 0.0042 and T_treat = 0.367.

## Ear-pain script

Population: adults (18 or older) with ear pain. The lane gate must exclude children, diabetes or immunosuppression (malignant otitis externa), trauma, foreign body, and sudden hearing loss (YAML comment).

### Acute otitis media and acute otitis externa

LRs: none. See "Unverified and omitted".

Priors: p = 0.50 each. Status: PLACEHOLDER (DS-5), DERIVED from two sources. Rijk 2021 (abstract) gives an AOM incidence of 5.3 per 1000 person-years in Dutch primary-care patients aged 15 or older (2015-2018). Piercefield 2011 (Results text) gives an ambulatory-care visit rate for acute otitis externa of 5.3 per 1000 population in US adults aged 20 or older (NAMCS 2003-2007). We calculated each share as 5.3 / (5.3 + 5.3) = 0.50. The two rates come from different countries, years, and units (episodes and visits). The priors also ignore other causes of ear pain (referred pain, temporomandibular disorder, eustachian tube dysfunction). Both priors are therefore rough.

### Mastoiditis (cannot-miss)

Prior: p = 0.00077. Status: PLACEHOLDER (DS-5), DERIVED. Petersen 2007 Table 3 ("Risk of complications in the month after diagnosis of common respiratory infections (per 10 000)") gives mastoiditis after otitis media in patients aged 16-64 as 11.92 per 10,000 in 16,780 patients without an antibiotic prescription and 6.77 per 10,000 in 76,763 patients with one. The pooled value is (11.92 × 16,780 + 6.77 × 76,763) / 93,543 = 7.7 per 10,000. Petersen excluded complications recorded on the day of the otitis media diagnosis (Methods). The denominator is otitis media episodes, not ear pain, and the value is an incidence in the next month, not a prevalence at the visit.

LRs: none. `must_ask`: `swelling_behind_ear`, `ear_pushed_forward`, `severe_headache_or_stiff_neck`, `confusion_or_drowsiness`. These features have no LRs.

Thresholds (illustrative): benefit B = 100, harm R = 1, test_se = 0.95, test_sp = 0.90, test_harm = 0.02. The reasons are the same as for the sinusitis complication. The engine calculates T_test = 0.0013 and T_treat = 0.149. The prior (0.00077) is below T_test, so the engine marks mastoiditis as ruled out at the start.

## Engine behavior with these numbers

We ran `workup.step` turn by turn with a simulated patient who confirms each answer (`confirmed: true`). The first-step results are from the validation command in the task brief.

| Script | First step | Path with all answers absent | Path with key findings present |
|---|---|---|---|
| acute_sinusitis | ASK `periorbital_swelling`, `vision_change` (must_ask; the complication is ruled out by its prior) | Turn 1 asks `severe_headache`, `confusion_or_drowsiness`. Turns 2 and 3 ask `maxillary_tenderness`, `pain_bending_forward`, `cacosmia`. COMPLETE at turn 4 (ABRS p = 0.32). | `cacosmia` and `tooth_pain` present: COMPLETE at turn 5 with ABRS p = 0.74. `periorbital_swelling` present: COMPLETE at turn 4, the same as all absent. |
| cough_acute | ASK `phlegm`, `breathlessness` (pneumonia is in the middle zone: p = 0.050, T_test = 0.011) | Turns 1 to 3 ask the other pneumonia features. DEFER at turn 4 with `cannot_miss_middle_zone_no_remote_test` (pneumonia p = 0.009, p95 = 0.014, which is above T_test). | Fever, breathlessness, high temperature, and pulse over 100 present: DEFER at turn 4 (pneumonia p = 0.23, p95 = 0.39, below T_treat 0.46). The engine does not ask the pertussis features in either path, because the pneumonia workup comes first and then the case defers. |
| red_eye | ASK `penlight_photophobia` (serious eye disease is in the middle zone: p = 0.28) | DEFER at turn 1 with `cannot_miss_middle_zone_no_remote_test` (p = 0.089, p95 = 0.23). | `penlight_photophobia` present: ESCALATE at turn 1 (p = 0.62, p95 = 0.76). |
| ear_pain | ASK `swelling_behind_ear`, `ear_pushed_forward` (must_ask; mastoiditis is ruled out by its prior) | Turn 1 asks the other two red flags. COMPLETE at turn 2. AOM and OE stay at 0.50. | `swelling_behind_ear` present: COMPLETE at turn 2, the same as all absent. |

The reviewer must know three consequences.

First, a PRESENT answer to a red flag that has no LR does not change the engine decision. This applies to `periorbital_swelling`, `vision_change`, `severe_headache`, `confusion_or_drowsiness` (sinusitis), `coughing_blood` (cough), `vision_change`, `severe_eye_pain`, `contact_lens_wearer` (red eye), and all four ear-pain red flags. In the simulation, periorbital swelling and swelling behind the ear both gave COMPLETE. `must_ask` makes the engine ask these questions; it does not make the engine act on the answer. Escalation for these findings now depends on the ANCHOR red-flag floor (`anchor_bridge.py::red_flag_floor`) or a lane-gate hard rule. The engine team should decide if a PRESENT `must_ask` finding without an LR must give ESCALATE or DEFER.

Second, the red-eye script cannot close an encounter remotely with these numbers. With the photophobia test absent, serious eye disease stays in the middle zone and the case defers. With the test present, the case escalates. The cough script also defers when all answers are absent, because p95 (0.014) stays just above T_test (0.011). Both results depend on the illustrative thresholds and the placeholder priors.

Third, the ear-pain script completes without a separation of AOM from OE. Their entropy (0.69 nats) is above eta (0.5), but no feature has a positive score. `workup.step` returns RESIDUAL_UNCERTAINTY only after the question budget is spent, so it returns COMPLETE before that. The reviewer must decide if the ear-pain lane can open before sourced LRs (or an otoscope image pathway) are added.

## Unverified and omitted

| Item | Reason |
|---|---|
| Orbital or intracranial complication LRs (periorbital swelling, vision change, severe headache, altered mental status) | [UNVERIFIED — omitted]. We found no diagnostic-accuracy study with a comparison group of ARS without complications. Hansen 2012 is a case series of hospitalized complications. |
| Double sickening, preceding respiratory infection, hyposmia, nasal speech, transillumination, and other Ebell 2019 Table 3 rows | [UNVERIFIED — omitted]. Table 3 uses ARS by any reference standard (mostly imaging), not ABRS. For example, double sickening has LR+ 1.30 (0.77-2.40) and LR− 0.69 (0.20-1.50) for ARS. These LRs do not apply to the bacterial diagnosis. |
| Nasal congestion or obstruction (ABRS LR+ 0.98 [0.83-1.3], LR− 1.3 [0.70-2.3]) and cough (ABRS LR+ 0.93 [0.70-1.1], LR− 1.2 [0.79-1.7]), Ebell 2019 Table 4 | VERIFIED but not used. Both LRs are near 1 and almost all patients with sinus symptoms have these findings. The reviewer can add them. |
| Overall clinical impression (ABRS LR+ 3.9 [2.4-5.9], LR− 0.33 [0.20-0.50], Ebell 2019 Table 4) | Not used. It is a clinician judgment, not a patient question. |
| Ebell 2017 clinical decision rule for ABRS (tender maxillary sinus, maxillary toothache, CRP > 15 mg/L, preceding URI, purulent discharge, previous sinusitis), listed in the Ebell 2019 table of clinical decision rules | [UNVERIFIED — omitted]. The rule needs a CRP test. We did not read the source study. |
| Williams JW Jr, Simel DL. Does this patient have sinusitis? Diagnosing acute sinusitis by history and physical examination. *JAMA*. 1993;270(10):1242-1246 (PMID 8355389; Rational Clinical Examination) | [UNVERIFIED — omitted]. Not read. Ebell 2019 includes the Williams 1992 cohort. |
| Pulmonary embolism as a cannot-miss diagnosis in acute cough | [UNVERIFIED — omitted]. We found no LRs for PE in an acute-cough population. `coughing_blood` is a must_ask red flag with no LR. The lane gate must escalate pleuritic chest pain with severe breathlessness, leg swelling, or hemoptysis. |
| Ebell MH, Chupp H, Cai X, Bentivegna M, Kearney M. Accuracy of signs and symptoms for the diagnosis of community-acquired pneumonia: a meta-analysis. *Acad Emerg Med*. 2020;27(7):541-553 (PMID 32329557, doi:10.1111/acem.13965) | [UNVERIFIED — omitted]. Full text not available to us. The abstract gives LR+ only for a few findings (for example, measured temperature, LR+ 2.52 [2.02-3.20]; egophony, LR+ 6.17 [1.34-18.0]) and LR− only for absent abnormal vital signs (0.25 [0.11-0.48]). We used the van Vugt 2013 counts, which give paired LRs in a primary-care cough population. |
| Metlay JP, Kapoor WN, Fine MJ. Does this patient have community-acquired pneumonia? *JAMA*. 1997;278(17):1440-1445 (PMID 9356004; Rational Clinical Examination) | [UNVERIFIED — omitted]. Not read. |
| Marchello 2019 decision-rule LRs: any abnormal vital sign, LR+ 1.84 (1.25-3.03), LR− 0.24 (0.17-0.34); any abnormal vital sign or pulmonary exam finding, LR+ 1.79 (1.22-3.01), LR− 0.10 (0.07-0.13) (Table 3) | VERIFIED but not used. These rules need measured vital signs and a lung exam (respiratory rate, temperature, pulse, auscultation), so they are not remote features. They are the strongest rule-out data for an in-person visit. |
| van Vugt 2013 severe breathlessness, severe chest pain, diarrhoea, tachypnoea, blood pressure below 90/60, CRP, procalcitonin | Not used. The severe forms overlap with breathlessness and chest pain. CRP and procalcitonin are laboratory tests. The derived values are in our calculation log and can be added. |
| Ebell 2017 "Sputum production" row (LR+ 1.2 [1.1-1.3], LR− 0.63 [0.39-0.89]) | [UNVERIFIED — omitted]. The abstract describes this finding as "absence of sputum", but the table label is "Sputum production". We could not resolve the direction. |
| Other Ebell 2017 rows (overall clinical impression, sleep disturbed by cough, headache absent, wheezing absent, sneezing, dyspnea, apnea, cyanosis, chest pain, CDC clinical criteria) | Not used. They are all ages (not adults only), near 1, or a clinician judgment. |
| Influenza and COVID-19 as separate diagnoses | [UNVERIFIED — omitted]. Not searched. They are inside the non-pneumonia diagnosis. |
| Narayana 2015 pooled LRs for serious eye disease (anisocoria > 1 mm, LR 6.5 [2.6-16.3]; photophobia by indirect illumination, LR 28.8 [1.8-459]; near synkinesis test, LR 21.4 [12-38.2]) and for bacterial conjunctivitis (complete redness obscuring tarsal vessels, LR 4.6 [1.2-17.1]; observed purulent discharge, LR 3.9 [1.7-9.1]; no red eye at 20 feet, LR 0.2 [0-0.8]) | [UNVERIFIED — omitted]. Abstract values only, with no paired LR−. The publisher page returned HTTP 403. Most are clinician exam findings. |
| Rietveld 2004 purulent secretion (derived LR+ 0.77 [0.42-1.43], LR− 1.08 [0.91-1.27]) | Not used. The clinician observed it, and the value disagrees in direction with the Narayana 2015 pooled LR of 3.9 for observed purulent discharge. The reviewer must decide. |
| Vision change, severe eye pain, and contact lens use as LRs for serious eye disease or keratitis | [UNVERIFIED — omitted]. We found no diagnostic-accuracy study with paired LRs. They are must_ask red flags with no LR. |
| Allergic conjunctivitis as a separate diagnosis | [UNVERIFIED — omitted]. No sourced prior or LRs in a red-eye population. Rietveld 2004 recruited presumed infectious conjunctivitis. |
| AOM symptom LRs: Rothman R, Owens T, Simel DL. Does this child have acute otitis media? *JAMA*. 2003;290(12):1633-1640 (PMID 14506123, doi:10.1001/jama.290.12.1633) | [UNVERIFIED — omitted]. Full text not read. The abstract gives a range only for ear pain (LR+ 3.0-7.3) in children, with clinician diagnosis as the reference standard. |
| AOM earache LR from Heikkinen T, Ruuskanen O. Signs and symptoms predicting acute otitis media. *Arch Pediatr Adolesc Med*. 1995;149(1):26-29 (PMID 7827655, doi:10.1001/archpedi.1995.02170130028006) | Not used. The abstract gives specificity 92% and sensitivity 60% (LR+ 7.5, LR− 0.43, no CI), but for AOM compared with uncomplicated URI in children younger than 4 years. In an ear-pain script every patient has ear pain, so the finding has no use. |
| Otitis externa features (tragal tenderness, pain when the ear is pulled, recent swimming, itching, discharge) | [UNVERIFIED — omitted]. A PubMed search found no diagnostic-accuracy study that compares OE with AOM. |
| Mastoiditis LRs (postauricular swelling, protruding auricle, fever) | [UNVERIFIED — omitted]. No diagnostic-accuracy study with a comparison group found. |
| Otitis externa incidence from Rowlands S et al. *Br J Gen Pract*. 2001;51(468):533-538 (PMID 11462312) | [UNVERIFIED — omitted]. The full text is a scanned PDF that we could not read. We used Piercefield 2011 instead. |
| Feature `cost`, `harm`, `leak` | Not set (defaults). No fee-schedule or leak source was given. The engine calculates the leak from the LRs. For features with no LR, the engine uses a leak of 0.5. |
