# Titration-lane and contraception-lane rule sources (DRAFT 0.1.0-draft)

Status: DRAFT for pharmacist and physician sign-off. Do not deploy.

Files covered:
- `compass_pcp/data/rules/titration.yaml`: 21 gate rules and 1 lab-recency rule (lanes `htn_titration` and `dm_titration`).
- `compass_pcp/data/rules/contraception.yaml`: 34 gate rules (lane `contraception`).

All sources were accessed on 2026-10-27. We fetched ADA and AGS Beers full text from PubMed Central, the KDIGO 2024 PDF from kdigo.org, the CDC U.S. MEC 2024 PDF and appendix web page from cdc.gov, and FDA labels as SPL XML from the DailyMed v2 API. For each quoted statement below, we searched the fetched text for the exact string. The label versions are the ones listed in `docs/clinical/REFILL_RULE_SOURCES.md`.

## Sources

| Key | Source | URL / DOI |
|---|---|---|
| ADA26-S6 | ADA Professional Practice Committee. 6. Glycemic Goals, Hypoglycemia, and Hyperglycemic Crises: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1):S132–S149 | https://doi.org/10.2337/dc26-S006 (PMC12690178) |
| ADA26-S9 | ADA. 9. Pharmacologic Approaches to Glycemic Treatment: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1) | https://doi.org/10.2337/dc26-S009 (PMC12690185) |
| ADA26-S10 | ADA. 10. Cardiovascular Disease and Risk Management: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1) | https://doi.org/10.2337/dc26-S010 (PMC12690187) |
| ADA26-S13 | ADA. 13. Older Adults: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1) | https://doi.org/10.2337/dc26-S013 (PMC12690186) |
| KDIGO24 | KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD. Kidney Int. 2024;105(4S):S117–S314 | https://doi.org/10.1016/j.kint.2023.10.018 (PDF: https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf) |
| BEERS23 | 2023 American Geriatrics Society Beers Criteria Update Expert Panel. J Am Geriatr Soc. 2023;71:2052–2081 | https://doi.org/10.1111/jgs.18372 (PMC12478568) |
| MEC24 | Nguyen AT, Curtis KM, Tepper NK, et al. U.S. Medical Eligibility Criteria for Contraceptive Use, 2024. MMWR Recomm Rep 2024;73(No. RR-4):1–126 | https://doi.org/10.15585/mmwr.rr7304a1 (PDF: https://www.cdc.gov/mmwr/volumes/73/rr/pdfs/rr7304a1-H.pdf; appendix: https://www.cdc.gov/mmwr/volumes/73/rr/rr7304a1_appendix.htm) |

Version note: the request allowed ADA 2025 or 2026. We read the 2026 Standards (published December 2025) for every titration rule. The refill rules written earlier cite ADA 2025, and the two editions number some recommendations differently (for example, the diuretic potassium recommendation is 10.12 in 2025 and 10.11 in 2026).

Citation note: the MEC24 authors, volume, issue, pages, and DOI were checked against the report's first page and the Crossref record for doi:10.15585/mmwr.rr7304a1 on 2026-10-27.

## Titration rules (`titration.yaml`)

### Blood pressure, any antihypertensive increase

**htn_bp_at_or_below_goal**: `titrate:antihypertensive & bp:at_or_below_individual_goal`
- ADA26-S10, Recommendation 10.3: "For people with diabetes and hypertension, blood pressure goals should be individualized through a shared decision-making process that addresses cardiovascular risk, potential adverse effects of antihypertensive medications, and individual preferences."
- ADA26-S10, Recommendation 10.4: "If it can be safely attained, the on-treatment blood pressure goal is <130/80 mmHg; a systolic blood pressure goal <120 mmHg should be encouraged in individuals with high cardiovascular or kidney risk."
- ADA26-S10, Recommendation 10.6: "In individuals with confirmed office-based blood pressure ≥130/80 mmHg, pharmacologic therapy should be initiated and titrated to achieve their individualized blood pressure goal."
- ADA26-S13, Recommendation 13.9: "The on-treatment blood pressure goal for most older adults with diabetes is <130/80 mmHg when it can be achieved safely, A and more a relaxed blood pressure goal (e.g., <140/90 mmHg) may be used for people with poor health, limited life expectancy, or high risk for adverse effects of hypertensive therapy."
- Reviewer note: these sources apply to adults with diabetes. For hypertension without diabetes, the goal must come from the 2025 AHA/ACC guideline, which we could not read (see Omitted items). The predicate uses the documented individual goal, so the rule holds when no goal is documented.

**htn_bp_not_confirmed**: `titrate:antihypertensive & bp:fewer_than_2_readings_on_2_occasions`
- ADA26-S10, Recommendation 10.1: "Hypertension is defined as a systolic blood pressure ≥130 mmHg or a diastolic blood pressure ≥80 mmHg based on an average of two or more measurements obtained on two or more occasions."
- ADA26-S10, Recommendation 10.6 (quoted above) says "confirmed office-based blood pressure".
- Reviewer note: ADA 10.1 defines the diagnosis. Using the same two-readings, two-occasions standard for a titration step is a lane-policy choice. ADA26-S10 also says "home blood pressure assessment may be useful to monitor antihypertensive treatment", so home readings can count.

**htn_symptomatic_hypotension**: `titrate:antihypertensive & sx:symptomatic_hypotension` (out_of_lane)
- KDIGO24, Practice Point 3.6.5: "Consider reducing the dose or discontinuing ACEi or ARB in the setting of either symptomatic hypotension or uncontrolled hyperkalemia despite medical treatment".
- ADA26-S13, Recommendation 13.9 (quoted above) allows a relaxed goal for people at "high risk for adverse effects of hypertensive therapy".
- Reviewer note: KDIGO names ACE inhibitors and ARBs. The rule applies the same stop to every antihypertensive increase, which is a lane-policy extension.

**nondhp_ccb_titration_sbp_lt_90**: `titrate:nondhp_ccb & vital:sbp_lt_90`
- Cardizem CD label, Contraindications: "(3) patients with hypotension (less than 90 mm Hg systolic)".
- Verapamil ER label, Contraindications: "Hypotension (systolic pressure less than 90 mm Hg) or cardiogenic shock".

### RAS inhibitors and MRAs

**rasi_titration_potassium_gt_5_5**: `[titrate:ace_inhibitor | titrate:arb] & lab:potassium_gt_5_5`
- KDIGO24, Figure 32: "Actions to manage hyperkalemia (potassium >5.5 mmol/l) in chronic kidney disease".
- KDIGO24, Practice Point 3.6.2: "Changes in BP, serum creatinine, and serum potassium should be checked within 2–4 weeks of initiation or increase in the dose of a RASi, depending on the current GFR and serum potassium."
- Reviewer note: the 28-day potassium window in the file header is lane policy.

**rasi_titration_creatinine_rise_gt_30pct**: `[ace | arb] & delta:creatinine_rise_gt_30pct_after_last_rasi_change`
- KDIGO24, Practice Point 3.6.4: "Continue ACEi or ARB therapy unless serum creatinine rises by more than 30% within 4 weeks following initiation of treatment or an increase in dose."
- ADA26-S10, text: "Elevations in serum creatinine (up to 30% from baseline) with ACE inhibitors or ARBs must not be confused with AKI".

**rasi_titration_no_bmp_after_last_change**: `[ace | arb] & monitor:no_bmp_2_to_4_weeks_after_last_rasi_change`
- KDIGO24, Practice Point 3.6.2 (quoted above).
- ADA26-S10, text: "Serum creatinine and potassium should be monitored after initiation of treatment with an ACE inhibitor or ARB, MRA, or diuretic and monitored during treatment and following uptitration of these medications, particularly among individuals with reduced glomerular filtration".

**rasi_dual_blockade**: `[titrate:ace_inhibitor | titrate:arb] & [med:ace_inhibitor | med:arb | med:arni | med:direct_renin_inhibitor]`
- ADA26-S10, Recommendation 10.9: "Multiple-drug therapy is generally required to achieve blood pressure goals. However, avoid any combination of ACE inhibitors, ARBs (including ARBs and neprilysin inhibitors), and direct renin inhibitors."
- KDIGO24, Recommendation 3.6.4: "We recommend avoiding any combination of ACEi, ARB, and direct renin inhibitor (DRI) therapy in people with CKD, with or without diabetes (1B)."
- BEERS23, Table 5: "Avoid routinely using 2 or more RAS inhibitors, or a RAS inhibitor and potassium-sparing diuretic, concurrently in those with chronic kidney disease Stage 3a or higher."

**rasi_mra_titration_pregnancy_possible**: `[ace | arb | mra] & preg:possible`
- ADA26-S10, Recommendation 10.12: "In sexually active individuals of childbearing potential who are not using reliable contraception, avoid ACE inhibitors, ARBs, MRAs, direct renin inhibitors, and neprilysin inhibitors, as they are contraindicated in pregnancy."
- Lisinopril and Cozaar labels, Boxed Warning (quoted in `REFILL_RULE_SOURCES.md`, rule `rasi_pregnancy_possible`).

**mra_titration_potassium_gt_4_8**: `titrate:mra & lab:potassium_gt_4_8`
- KDIGO24, Figure 26 (finerenone protocol), column "K+ ≤4.8 mmol/l": "Increase dose to 20 mg daily, if on 10 mg daily". Column "K+ 4.9–5.5 mmol/l": "Continue finerenone 10 mg or 20 mg". Column "K+ >5.5 mmol/l": "Hold finerenone".
- KDIGO24, Figure 26 legend: "This algorithm could be used for steroidal MRA."
- Reviewer note: the figure is a finerenone protocol. Applying the ≤4.8 increase threshold to spironolactone or eplerenone rests on the legend sentence above. In the 4.9 to 5.5 column the figure says to continue the current dose without an increase, so the rule holds the increase; it does not stop the drug.

### Diuretics

**diuretic_titration_potassium_below_lln**: `[titrate:thiazide | titrate:loop_diuretic] & ref:potassium_below_lln`
- ADA26-S10, Recommendation 10.11: "Monitor for hypokalemia when diuretics are used at routine visits and 7–14 days after initiation or after a dose change and periodically as clinically appropriate."
- Reviewer note: ADA gives no potassium number. The predicate uses the reporting laboratory's lower reference limit. Sign-off decides whether to keep this rule or to replace it with a fixed number from a source.

### Glucose lowering, any increase

**dm_titration_a1c_at_or_below_goal**: `titrate:glucose_lowering & glycemia:a1c_at_or_below_individual_goal`
- ADA26-S6, Recommendation 6.3a: "An A1C goal of <7% (<53 mmol/mol) is appropriate for many nonpregnant adults without severe hypoglycemia or hypoglycemia affecting health or quality of life."
- ADA26-S6, Recommendation 6.5: "Less stringent glycemic goals may be appropriate for individuals with significant cognitive and/or functional limitations, frailty, or severe comorbidities or where the harms of treatment, including hypoglycemia, are greater than the benefits."
- ADA26-S6, Recommendation 6.8: "Reassess glycemic goals based on the individualized criteria shown in Fig. 6.1."
- ADA26-S13, Recommendation 13.7a: "Older adults with diabetes with few and stable coexisting chronic illnesses, and intact cognitive and functional status, should have lower glycemic goals (such as A1C <7.0–7.5% [<53–58 mmol/mol])". Recommendation 13.7b gives "less stringent goals (such as A1C <8.0% [<64 mmol/mol]" for intermediate or complex health.
- Reviewer note: A1C goals are individual. The rule uses the documented goal and holds when none is documented. It does not apply a fixed 7%.

**dm_titration_level_2_or_3_hypoglycemia**: `titrate:glucose_lowering & hx:hypoglycemia_level_2_or_3_since_last_change` (out_of_lane)
- ADA26-S6, Recommendation 6.19: "One or more episodes of level 2 or 3 hypoglycemia should prompt reevaluation of the treatment plan, including deintensifying or switching diabetes medications if appropriate."
- ADA26-S6, Hypoglycemia section: "Level 2 hypoglycemia (defined as a blood glucose concentration <54 mg/dL [<3.0 mmol/L])" and "level 3 hypoglycemia is defined as a severe event characterized by altered mental and/or physical functioning that requires assistance from another person for recovery, irrespective of glucose level."

**hypoglycemic_agent_titration_glucose_lt_70**: `[titrate:basal_insulin | titrate:sulfonylurea] & hx:glucose_lt_70_since_last_change`
- ADA26-S6, Recommendation 6.3c: "A goal percent time <70 mg/dL (<3.9 mmol/L) of <4% (or <1% for older adults) and a goal percent time <54 mg/dL (<3.0 mmol/L) of <1% are recommended in people using CGM to prevent hypoglycemia. Deintensify or modify therapy if these goals are not met."
- ADA26-S6, Recommendation 6.6: "Deintensify hypoglycemia-causing medications (insulin, sulfonylureas, or meglitinides), or switch to a medication class with lower hypoglycemia risk, for individuals who are at high risk for hypoglycemia, within individualized glycemic goals."
- ADA26-S6, Hypoglycemia section: "Level 1 hypoglycemia is defined as a measurable glucose concentration <70 mg/dL (<3.9 mmol/L) and ≥54 mg/dL (≥3.0 mmol/L)." and "a measured glucose level <70 mg/dL (<3.9 mmol/L) is considered clinically important, regardless of symptoms."
- Reviewer note: ADA sets a CGM percentage goal (< 4% below 70) and does not say that one reading below 70 forbids an increase. Holding on any value below 70 is a conservative lane-policy reading. Sign-off can relax it to the CGM percentage for CGM users.

**basal_insulin_titration_fasting_lt_80**: `titrate:basal_insulin & smbg:fasting_lt_80_since_last_change`
- ADA26-S6, Table 6.3 (glycemic goals for many nonpregnant adults): "Preprandial capillary plasma glucose | 80–130 mg/dL* (4.4–7.2 mmol/L)".

**basal_insulin_titration_overbasalization**: `titrate:basal_insulin & glycemia:overbasalization_signs`
- ADA26-S9, Recommendation 9.26: "Monitor for signs of overbasalization during insulin therapy, such as significant bedtime-to-morning or postprandial-to-preprandial glucose differential, occurrences of hypoglycemia (aware or unaware), and high glycemic variability. When overbasalization is suspected, a thorough reevaluation should occur promptly to further tailor therapy to the individual’s needs."
- Reviewer note: ADA 2026 gives no units/kg threshold for overbasalization. The predicate is a documented clinical finding.

**hypoglycemic_agent_titration_high_risk**: `[basal_insulin | sulfonylurea] & dx:high_hypoglycemia_risk`
- ADA26-S6, Recommendation 6.6 (quoted above).
- ADA26-S13, Recommendation 13.14a: "Deintensify hypoglycemia-causing medications (e.g., insulin, sulfonylureas, or meglitinides) or switch to a medication class with low hypoglycemia risk for individuals who are at high risk for hypoglycemia, using individualized glycemic goals."
- ADA26-S6, Table 6.5, "Major risk factors": "Recent (within the past 3–6 months) level 2 or 3 hypoglycemia", "Intensive insulin therapy*", "Impaired hypoglycemia awareness", "Kidney failure", "Cognitive impairment or dementia", "History of metabolic surgery", "Food insecurity", "Low-income status§".

**sulfonylurea_titration_age_ge_65**: `titrate:sulfonylurea & age_ge_65`
- BEERS23, Table 2, "Sulfonylureas (all, including short- and longer-acting)": "Avoid sulfonylureas as first- or second-line monotherapy or add-on therapy unless there are substantial barriers to the use of safer and more effective agents."

**weekly_glp1_titration_lt_4_weeks**: `[titrate:semaglutide | titrate:dulaglutide] & titration:days_on_current_dose_lt_28`
- Ozempic label 2.2 (Highlights): "If additional glycemic control is needed, increase the dosage to 1 mg once weekly after at least 4 weeks on the 0.5 mg dose." and "If additional glycemic control is needed, increase the dosage to 2 mg once weekly after at least 4 weeks on the 1 mg dosage."
- Trulicity label 2.1: "If additional glycemic control is needed, increase the dosage in 1.5 mg increments after at least 4 weeks on the current dosage."

**liraglutide_titration_lt_1_week**: `titrate:liraglutide & titration:days_on_current_dose_lt_7`
- Victoza label 2.1: "If additional glycemic control is required, increase the dosage in 0.6 mg increments after at least one week on the current dosage, to reduce the risk of gastrointestinal adverse reactions".

**pioglitazone_titration_heart_failure_signs**: `titrate:pioglitazone & sx:edema_weight_gain_or_dyspnea` (out_of_lane)
- Actos label, Boxed Warning: "After initiation of ACTOS, and after dose increases, monitor patients carefully for signs and symptoms of heart failure (e.g., excessive, rapid weight gain, dyspnea, and/or edema)."

### Lab recency

| id | Class | LOINC | Days | Statement |
|---|---|---|---|---|
| a1c_before_glucose_titration | glucose_lowering | 4548-4, 17856-6, 4549-2 | 92 | ADA26-S6, Recommendation 6.2: "Assess glycemic status at least two times a year, and more frequently (e.g., every 3 months) for individuals not meeting glycemic goals or with recent treatment changes". Recommendation 6.1 also allows CGM metrics; see Schema limitations. |

LOINC codes were verified against the NLM Clinical Tables LOINC service on 2026-10-27 (4548-4 Hemoglobin A1c/Hemoglobin.total in Blood; 17856-6, the same by HPLC; 4549-2, the same by electrophoresis).

## Contraception rules (`contraception.yaml`)

MEC24 category definitions (Box K1): "U.S. MEC 3 = A condition for which the theoretical or proven risks usually outweigh the advantages of using the method" and "U.S. MEC 4 = A condition that represents an unacceptable health risk if the contraceptive method is used".

We read each category in Table D1 (combined hormonal contraceptives, CHC) or Table C1 (progestin-only, POP column) of the PDF and cross-checked it against the summary Table K1 on the appendix web page. The table cells below are the CHC (Table D1) or POP (Table C1) category for the stated row.

### Combined hormonal contraceptives

| Rule | Table D1 row (verbatim condition) | CHC category |
|---|---|---|
| chc_age_ge_35_smokes_ge_15 | Smoking, "b. Age ≥35 years", "ii. ≥15 cigarettes per day" | 4 |
| chc_age_ge_35_smokes_lt_15 | Smoking, "b. Age ≥35 years", "i. <15 cigarettes per day" | 3 |
| chc_hypertension | Hypertension, "a. Adequately controlled hypertension"; "i. Systolic 140–159 mm Hg or diastolic 90–99 mm Hg" | 3; 3 |
| chc_bp_ge_160_100_or_vascular_disease | Hypertension, "ii. Systolic ≥160 mm Hg or diastolic ≥100 mm Hg"; "c. Vascular disease" | 4; 4 |
| chc_migraine_with_aura | Headaches, b. Migraine, "ii. With aura" | 4 |
| chc_dvt_pe_history | DVT/PE, "a. Current or history of DVT/PE, receiving anticoagulant therapy (therapeutic dose)" 3; "i. Higher risk for recurrent DVT/PE (one or more risk factors)" 4; "ii. Lower risk for recurrent DVT/PE (no risk factors)" 3 | 3 or 4 |
| chc_thrombophilia | "Thrombophilia (e.g., factor V Leiden mutation; prothrombin gene mutation; protein S, protein C, and antithrombin deficiencies; or antiphospholipid syndrome)" | 4 |
| chc_postpartum_lt_21_days | Breastfeeding "a. <21 days postpartum"; Postpartum (nonbreastfeeding) "a. <21 days postpartum" | 4; 4 |
| chc_postpartum_21_to_42_days_vte_risk | Breastfeeding b.i and c.i; Postpartum (nonbreastfeeding) b.i, "i. With other risk factors for VTE (e.g., age ≥35 years, previous VTE, thrombophilia, immobility, transfusion at delivery, peripartum cardiomyopathy, BMI ≥30 kg/m2, postpartum hemorrhage, postcesarean delivery, preeclampsia, or smoking)" | 3 |
| chc_breastfeeding_21_to_lt_30_days | Breastfeeding "b. 21 to <30 days postpartum", i (with VTE risk factors) and "ii. Without other risk factors for VTE" | 3; 3 |
| chc_ischemic_heart_disease_or_stroke | "Current and history of ischemic heart disease"; "Stroke (history of cerebrovascular accident)" | 4; 4 |
| chc_complicated_valvular_disease | Valvular heart disease, "b. Complicated (pulmonary hypertension, risk for atrial fibrillation, or history of subacute bacterial endocarditis)" | 4 |
| chc_peripartum_cardiomyopathy | Peripartum cardiomyopathy, a.i "<6 months" 4; a.ii "≥6 months" 3; "b. Moderately or severely impaired cardiac function" 4 | 3 or 4 |
| chc_diabetes_vascular_or_gt_20_years | Diabetes, "c. Nephropathy, retinopathy, or neuropathy"; "d. Other vascular disease or diabetes of >20 years’ duration" | 3/4; 3/4 |
| chc_multiple_ascvd_risk_factors | "Multiple risk factors for atherosclerotic cardiovascular disease (e.g., older age, smoking, diabetes, hypertension, low HDL, high LDL, or high triglyceride levels)" | 3/4 |
| chc_major_surgery_prolonged_immobilization | Surgery, b. Major surgery, "ii. With prolonged immobilization" | 4 |
| chc_liver_disease_cat_4 | Cirrhosis "b. Decompensated (impaired liver function)"; Liver tumors "ii. Hepatocellular adenoma"; "b. Malignant (hepatocellular carcinoma)" | 4; 4; 4 |
| chc_sle_antiphospholipid | Systemic lupus erythematosus, "a. Positive (or unknown) antiphospholipid antibodies" | 4 |
| chc_ckd_nephrotic_or_dialysis | Chronic kidney disease, "a. Current nephrotic syndrome", "b. Hemodialysis", "c. Peritoneal dialysis" | 4; 4; 4 |
| chc_sickle_cell_disease | "Sickle cell disease" | 4 |
| chc_transplant_graft_failure | Solid organ transplantation, "b. Graft failure" | 4 |
| chc_superficial_venous_thrombosis | Superficial venous disorders, "b. Superficial venous thrombosis (acute or history)" | 3 |
| chc_gallbladder_or_coc_cholestasis | Gallbladder disease, b. Symptomatic, "i. Current" and "iii. Medically treated"; History of cholestasis, "b. Past COC related" | 3; 3; 3 |
| chc_ms_prolonged_immobility | Multiple sclerosis, "b. With prolonged immobility" | 3 |
| chc_past_breast_cancer | Breast disease, d. Breast cancer, "ii. Past and no evidence of current disease for 5 years" | 3 |
| chc_interacting_drug | Anticonvulsant therapy, "a. Certain anticonvulsants (phenytoin, carbamazepine, barbiturates, primidone, topiramate, oxcarbazepine)"; "b. Lamotrigine"; Antimicrobial therapy, "d. Rifampin or rifabutin therapy" | 3; 3; 3 |
| coc_malabsorptive_bariatric_surgery | History of bariatric surgery, "b. Malabsorptive procedures: decrease absorption of nutrients and calories by shortening the functional length of the small intestine (Roux-en-Y gastric bypass or biliopancreatic diversion)" | "COCs: 3", "Patch and ring: 1" |
| hormonal_current_breast_cancer (CHC) | Breast cancer, "i. Current" | 4 |

Supporting statements from MEC24 used in the predicate definitions:
- Hypertension clarification (Table D1): "A single reading of blood pressure level is not sufficient to classify a person as hypertensive." The BP predicates therefore require a mean of at least two readings.
- Smoking (main text): "a person who smokes and is aged <35 years generally can use COCs (category 2)", so there is no rule for smokers under 35.

Reviewer notes:
- `chc_dvt_pe_history`, `chc_peripartum_cardiomyopathy`, `chc_diabetes_vascular_or_gt_20_years`, and `chc_multiple_ascvd_risk_factors` cover rows where the category is 3 or 4 depending on detail. They use `out_of_lane` so a clinician decides.
- Table D1 also lists acute viral hepatitis (initiation 3/4, continuation 2). This lane renews an existing method, so the continuation category applies and there is no rule.
- `chc_interacting_drug`: MEC24 lists lamotrigine as category 3 for CHC (Table D1, "b. Lamotrigine"). The lamotrigine refill rules in `refill.yaml` do not repeat this.

### Progestin-only pills (POP column of Table C1)

| Rule | Table C1 row (verbatim condition) | POP category |
|---|---|---|
| pop_ischemic_heart_disease_or_stroke | "Current and history of ischemic heart disease" and "Stroke (history of cerebrovascular accident)", POP Initiation 2 / Continuation 3 | 3 (continuation) |
| pop_past_breast_cancer | Breast cancer, "ii. Past and no evidence of current disease for 5 years" | 3 |
| hormonal_current_breast_cancer (POP) | Breast cancer, "i. Current" | 4 |
| pop_hepatocellular_carcinoma | Liver tumors, "b. Malignant (hepatocellular carcinoma)" | 3 |
| pop_interacting_drug | "a. Certain anticonvulsants (phenytoin, carbamazepine, barbiturates, primidone, topiramate, and oxcarbazepine)"; "d. Rifampin or rifabutin therapy" | 3; 3 |
| pop_malabsorptive_bariatric_surgery | History of bariatric surgery, "b. Malabsorptive procedures" | 3 |
| drsp_pop_ckd_hyperkalemia | Chronic kidney disease a–c, POP cell "DRSP POP with known hyperkalemia: 4"; clarification: "Persons with known hyperkalemia should not use DRSP POPs because of the risk for worsening hyperkalemia (category 4)." | 4 |

Reviewer notes:
- For POP, SLE with positive or unknown antiphospholipid antibodies is category 2, thrombophilia is category 2, decompensated cirrhosis is category 2, and lamotrigine is category 1, so there are no POP rules for them. (DMPA, which is not in this lane, has category 3 for several of these.)
- Table K1 on the web page has merged cells for rows with initiation and continuation columns. For those rows we used the PDF tables C1 and D1, where the column positions are clear.

## Omitted items

- **2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA/SGIM High Blood Pressure Guideline** (Hypertension 2025, doi:10.1161/HYP.0000000000000249; Circulation, doi:10.1161/CIR.0000000000001356; J Am Coll Cardiol 2025;86(18):1567–1678, doi:10.1016/j.jacc.2025.05.007) [UNVERIFIED — omitted]. Europe PMC lists the 2025 guideline in all three journals and several published corrections (2025 and 2026). A web search result from the AHA professional site states that it replaces the 2017 ACC/AHA guideline. We could not read the text: ahajournals.org and jacc.org returned HTTP 403 (Cloudflare) to curl, to WebFetch, and to a headless browser. The guideline is not in PubMed Central. We did not use the third-party summaries or the KDOQI and ERBP commentaries as primary sources. The BP goal for people without diabetes or CKD, the follow-up interval after a titration step, and any orthostatic hypotension threshold are therefore not encoded.
- **2017 ACC/AHA High Blood Pressure Guideline** (Hypertension 2018;71:e13–e115, doi:10.1161/HYP.0000000000000065) [UNVERIFIED — omitted]. The same publisher block applied, and the 2025 guideline replaces it.
- **Overbasalization dose threshold** (for example, basal insulin above a units/kg value) [UNVERIFIED — omitted]. ADA 2026 Section 9 describes overbasalization signs but gives no dose threshold.
- **Metformin uptitration at eGFR 30–45** [UNVERIFIED — omitted]. The metformin label addresses initiation and continuation at these values, not a dose increase.
- **SPR 2024 (U.S. Selected Practice Recommendations) BP check before CHC renewal.** We did not read SPR 2024, so there is no BP-recency rule for CHC renewal.
- **MEC24 conditions that need data the lane does not have** (for example, "Known thrombogenic mutations" found only by testing, or "Endometrial cancer"). These need a structured record field before a rule is useful.

## Schema limitations

1. **The titration lane needs the refill rules too.** `titration.yaml` assumes the lane also evaluates `refill.yaml` for the drug being titrated. Nothing in `gate.py` composes rule sets; the caller must load both.
2. **`titrate:` predicates are a second closed world.** The builder must set every `titrate:<class>` that was not requested to FALSE, in the same way as `rx_class`.
3. **Change-relative predicates are not `lab_bounds`.** `delta:creatinine_rise_gt_30pct_after_last_rasi_change`, `monitor:no_bmp_2_to_4_weeks_after_last_rasi_change`, `hx:glucose_lt_70_since_last_change`, and `titration:days_on_current_dose_lt_<n>` need the date of the last dose change. `lab_bounds` cannot compute them.
4. **`LabRecencyRule` accepts LOINC codes only.** ADA26-S6 6.1 accepts CGM metrics (time in range) as an alternative to A1C. A person who uses CGM and has no recent A1C will get a recency finding that the pharmacist must override.
5. **No negation and no "3 versus 4" split.** MEC rows that depend on detail (for example DVT/PE recurrence risk) are encoded once at the higher routing level.
6. **Contraception lane predicates have no freshness window field.** For example, the BP predicates need a lane-policy window for "current" BP, which must be set in the predicate builder. [LANE POLICY: needs sign-off.]
