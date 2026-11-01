# Refill-lane rule sources (DRAFT 0.1.0-draft)

Status: DRAFT for pharmacist and physician sign-off. Do not deploy.

Files covered:
- `compass_pcp/data/rules/refill.yaml`: 93 gate rules and 9 lab-recency rules.
- `compass_pcp/data/rules/refill_monitoring.yaml`: 7 monitoring contracts.

The titration and contraception rule files have their own sources document, `docs/clinical/TITRATION_CONTRACEPTION_SOURCES.md`.

All sources were accessed on 2026-10-27. Three SPLs in the table are older versions (Flomax, July 2024; Nesina, March 2025; Actos, April 2025), and the reviewer must check them against the current label. For each FDA label, we fetched the structured product label (SPL) XML from the DailyMed v2 API, converted it to text, and searched it for the quoted sentence. Several SPLs come from repackagers. They reproduce the manufacturer text, but the reviewer must compare each one with the reference listed drug label before sign-off. For each guideline, we read the quoted text in the full document (KDIGO PDF, PMC full text, NICE web page, eCFR).

## Sources

| Key | Source | URL / DOI |
|---|---|---|
| KDIGO24 | KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD. Kidney Int. 2024;105(4S):S117–S314 | https://doi.org/10.1016/j.kint.2023.10.018 (PDF: https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf) |
| ADA25-S2 | ADA. 2. Diagnosis and Classification of Diabetes: Standards of Care in Diabetes—2025. Diabetes Care 2025;48(Suppl 1) | https://doi.org/10.2337/dc25-S002 (PMC11635041) |
| ADA25-S10 | ADA. 10. Cardiovascular Disease and Risk Management: Standards of Care in Diabetes—2025 | https://doi.org/10.2337/dc25-S010 (PMC11635050) |
| ADA25-S13 | ADA. 13. Older Adults: Standards of Care in Diabetes—2025 | https://doi.org/10.2337/dc25-S013 (PMC11635042) |
| ADA26-S6 | ADA. 6. Glycemic Goals, Hypoglycemia, and Hyperglycemic Crises: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1):S132–S149 | https://doi.org/10.2337/dc26-S006 (PMC12690178) |
| BEERS23 | 2023 American Geriatrics Society Beers Criteria Update Expert Panel. J Am Geriatr Soc. 2023;71:2052–2081 | https://doi.org/10.1111/jgs.18372 (PMC12478568) |
| NICE185 | NICE CG185, Bipolar disorder: assessment and management (last updated 02 September 2025), section 1.10 | https://www.nice.org.uk/guidance/cg185/chapter/Recommendations |
| APA-PIP | Fochtmann LJ, Medicus J, Hong SH, et al. Performance in Practice: Practice Assessment Tool for the Care of Patients With Schizophrenia. Focus. 2020. Table 1 restates the APA 2020 schizophrenia guideline. **This is a secondary source: we did not read the primary APA guideline text.** | https://doi.org/10.1176/appi.focus.20200034 (PMC7725154) |
| CFR | 21 CFR 1306.12 and 1306.22 (eCFR, version 2026-10-01) | https://www.ecfr.gov/current/title-21/chapter-II/part-1306 |

FDA labels (DailyMed SPL set IDs; URL form `https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=<setid>`):

| Drug | SPL title (publisher) | setid | SPL published |
|---|---|---|---|
| Lisinopril | Lisinopril tablet (St. Mary's Medical Park Pharmacy) | 5eff766f-82e2-4cd6-e053-2a91aa0a4782 | Oct 19, 2026 |
| Losartan | Cozaar (Organon) | 9949448f-c3b9-44ee-94ed-c1aca8c90f39 | Jan 21, 2026 |
| Hydrochlorothiazide | Hydrochlorothiazide tablet (RemedyRepack) | f20fd735-30c7-4f89-8ceb-b6186646eea6 | Oct 26, 2026 |
| Spironolactone | Spironolactone tablet (Major) | 0c45d793-6f2f-4622-b5ed-6875acfbc02b | Oct 23, 2026 |
| Metformin | Metformin HCl tablet (RemedyRepack) | bfd6ec0f-8264-4877-aa6d-f347f53bc426 | Oct 26, 2026 |
| Empagliflozin | Jardiance (RedPharm) | 59ed43d9-b4e0-72a2-e063-6394a90a327d | Aug 27, 2026 |
| Dapagliflozin | Farxiga (RemedyRepack) | ef9e9c8c-5460-4193-952a-0c249dd071bd | Sep 21, 2026 |
| Glipizide | Glipizide tablet (A-S Medication Solutions) | a38cfe61-4aa5-498c-bca5-03a8213303bb | Oct 15, 2026 |
| Atorvastatin | Lipitor (Viatris) | a60cc18b-0631-4cf0-b021-9f52224ece65 | Jul 15, 2026 |
| Simvastatin | Simvastatin tablet (St. Mary's Medical Park Pharmacy) | faa81817-3ffa-b83c-e053-6294a90a3f85 | Oct 26, 2026 |
| Levothyroxine | Levothyroxine sodium tablet (Bryant Ranch Prepack) | 48a366d8-f5ac-47b0-84e3-f88251def70c | Oct 23, 2026 |
| Lithium | Lithium carbonate ER tablet (PD-Rx) | 039f188c-413a-6e64-e063-6294a90a2972 | Oct 19, 2026 |
| Warfarin | Warfarin sodium tablet (Sun) | 8ad881e0-ca41-42ad-9d7d-eb85b3a30af0 | Oct 26, 2026 |
| Apixaban | Eliquis (Aphena) | 41a133ef-e461-48ad-8221-b735bdd0ec25 | Sep 25, 2026 |
| Rivaroxaban | Xarelto (Janssen) | 10db92f9-2300-4a80-836b-673e1ae91610 | Sep 11, 2026 |
| Dabigatran | Dabigatran etexilate capsule (A-S Medication Solutions) | c0379093-3e19-45ae-a616-0f24a1d255f4 | Oct 21, 2026 |
| Divalproex | Divalproex sodium DR tablet (Major) | fb39a94e-93e6-4afe-a300-f80e8f1e0fa6 | Oct 23, 2026 |
| Methotrexate | Methotrexate tablet (American Health Packaging) | aafd97c1-3a0a-42b2-845a-a9db9bb7d876 | Oct 06, 2026 |
| Topiramate | Topiramate tablet (A-S Medication Solutions) | 88156c4e-bc29-497d-8110-e59d800ff38a | Oct 14, 2026 |
| Isotretinoin | Zenatane (Dr. Reddy's) | 27b3cf26-f22e-5b70-1c24-009933b7c6ee | Oct 09, 2026 |
| Ibuprofen | Ibuprofen tablet (PD-Rx) | 0fa4cd66-66ad-4ec9-b38c-6b5840df39df | Oct 26, 2026 |
| Naproxen | Naproxen DR tablet (PD-Rx) | 2d01e583-670a-46f4-b5f2-3fad46d0376f | Oct 16, 2026 |
| Methylphenidate (example CII) | Metadate CD (Lannett) | 29f06562-6b6a-4ca6-b62e-d08a45fb3dd4 | Oct 26, 2026 |
| Metoprolol succinate ER | Metoprolol succinate ER tablet (Ascend) | 58441cd3-6043-4bb8-adab-1b32a203bfb2 | Oct 21, 2026 |
| Carvedilol | Coreg (Waylis) | 07c619c6-4a0c-445e-94fa-664a54f68a39 | Aug 03, 2026 |
| Atenolol | Tenormin (Upsher-Smith) | 6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a | May 01, 2026 |
| Propranolol | Propranolol HCl tablet (Northwind) | 03afbc5a-a9dc-e823-e063-6394a90a0cb2 | Oct 21, 2026 |
| Diltiazem | Cardizem CD (Bausch) | 1042fa13-e6af-46b9-8008-6c941f0978b1 | Dec 12, 2025 |
| Verapamil | Verapamil HCl ER tablet (A-S Medication Solutions) | 5467dad4-f3ba-4036-b5f4-4d2d4d5abc34 | Oct 08, 2026 |
| Clonidine | Clonidine HCl tablet (Alembic) | cf493e6a-1603-4c7d-a442-69a119bec843 | Oct 23, 2026 |
| Hydralazine | Hydralazine HCl tablet (Cardinal Health) | 336b11da-e592-4386-921f-3c136d754f2a | Oct 19, 2026 |
| Isosorbide mononitrate | Isosorbide mononitrate tablet (Coupler) | 55f240e1-3056-38cc-e063-6294a90a814e | Jul 07, 2026 |
| Semaglutide | Ozempic (A-S Medication Solutions) | 42bdd912-2393-44c4-b7e0-47672ca28991 | Jul 31, 2026 |
| Dulaglutide | Trulicity (Eli Lilly) | 463050bd-2b1c-40f5-b3c3-0a04bb433309 | Aug 10, 2026 |
| Liraglutide | Victoza (Novo Nordisk) | 5a9ef4ea-c76a-4d34-a604-27c5b505f5a4 | Nov 17, 2025 |
| Sitagliptin | Januvia (A-S Medication Solutions) | 1b03c82f-b52e-4092-b9dc-f2c9b0d6ab40 | Jul 10, 2026 |
| Saxagliptin | Saxagliptin tablet (Glenmark) | e286ffd4-c598-47fb-af06-2e15f7e6f99f | Jan 28, 2026 |
| Linagliptin | Tradjenta (Cardinal Health) | dfe327e8-f6ab-41e5-bdef-d520118cd83a | Sep 08, 2025 |
| Alogliptin | Nesina (Takeda) | a3768c7e-aa4c-44d3-bc53-43bb7346c0b0 | Mar 24, 2025 |
| Insulin glargine | Lantus (Sanofi-Aventis) | d5e07a0c-7e14-4756-9152-9fea485d654a | Jul 02, 2025 |
| Pioglitazone | Actos (Takeda) | d2ddc491-88a9-4063-9150-443b4fa4330c | Apr 09, 2025 |
| Allopurinol | Allopurinol tablet (AvPAK) | 5d330416-4289-762e-e063-6294a90a532e | Oct 12, 2026 |
| Febuxostat | Uloric (Takeda) | 54de10ef-fe5f-4930-b91d-6bbb04c664bd | Dec 25, 2025 |
| Salmeterol | Serevent Diskus (GSK) | 12d9728e-6b5c-4aee-bfb0-745e542ed2e4 | Sep 07, 2026 |
| Fluticasone/salmeterol | Advair HFA (GSK) | dfaca6f9-3277-47b2-319d-1377917cb54c | May 20, 2026 |
| Tiotropium | Spiriva HandiHaler (Boehringer Ingelheim) | 820839ef-e53d-47e8-a3b9-d911ff92e6a9 | Nov 20, 2025 |
| Montelukast | Singulair (Organon) | 482dcc92-b47f-4ea6-854a-f5ac2aea7842 | Jun 25, 2025 |
| Sertraline | Zoloft (Viatris) | fda754f6-d0f3-4dce-a17a-927d64f912f7 | Jul 24, 2025 |
| Escitalopram | Lexapro (Allergan) | 13bb8267-1cab-43e5-acae-55a4d957630a | Jan 01, 2026 |
| Citalopram | Celexa (Allergan) | 4259d9b1-de34-43a4-85a8-41dd214e9177 | Aug 20, 2026 |
| Fluoxetine | Prozac (Dista) | c88f33ed-6dfb-4c5e-bc01-d8e36dd97299 | Jan 14, 2026 |
| Paroxetine | Paxil CR (Apotex) | 483bd97f-c4d0-4e23-aaa8-6334f4471e0c | Oct 02, 2026 |
| Duloxetine | Duloxetine HCl DR capsule (Yaopharma) | 90224073-178d-7ec5-e053-2995a90a20fc | Jul 09, 2026 |
| Venlafaxine | Venlafaxine ER tablet (Almatica) | e81a2daf-b8b2-7c05-b532-bc775700b100 | Oct 15, 2026 |
| Bupropion | Wellbutrin XL (Bausch) | a435da9d-f6e8-4ddc-897d-8cd2bf777b21 | Feb 06, 2026 |
| Mirtazapine | Remeron (Organon) | 98ad1917-a094-44f5-a28f-a64a8cfcd887 | Aug 08, 2025 |
| Trazodone | Trazodone HCl tablet (Aphena) | 5e85d801-af62-b939-e063-6294a90afacb | Oct 26, 2026 |
| Gabapentin | Neurontin (Viatris) | 97935fd9-1d4a-43b6-a5d9-de994591187b | Aug 06, 2026 |
| Pregabalin | Pregabalin capsule (RemedyRepack) | f30a7a3b-d45e-4e0b-ab1b-1369b2f02320 | Oct 21, 2026 |
| Famotidine | Famotidine tablet (RedPharm) | 55730918-d9e8-eaad-e063-6394a90aeda2 | Oct 19, 2026 |
| Alendronate | Alendronate sodium tablet (Marlex) | b63421af-ec03-1de7-e053-2a95a90abec6 | Oct 21, 2026 |
| Risedronate | Risedronate sodium DR tablet (Mylan) | c89430be-15f1-4b8b-ab7e-738de716ee7d | May 21, 2026 |
| Tamsulosin | Flomax (RedPharm) | b3384748-92f1-0b49-e053-2a95a90abc73 | Jul 29, 2024 |
| Finasteride | Proscar (Organon) | 6f988153-fc74-4ca4-b29a-111f750c4a4b | Mar 31, 2026 |
| Carbamazepine | Tegretol (Novartis) | 8d409411-aa9f-4f3a-a52c-fbcb0c3ec053 | Aug 21, 2026 |
| Lamotrigine | Lamictal (GSK) | d7e3572d-56fe-4727-2bb4-013ccca22678 | Aug 20, 2026 |
| Levetiracetam | Keppra (UCB) | 3ca9df05-a506-4ec8-a4fe-320f1219ab21 | Jan 29, 2026 |
| Amiodarone | Amiodarone HCl tablet (RemedyRepack) | 4c149392-a4f0-4e2d-a13f-2b94810005de | Aug 07, 2026 |
| Digoxin | Digoxin tablet (Amneal) | dfac7f13-28be-423d-9389-9089da29da17 | Aug 17, 2026 |

## Gate rules (`refill.yaml` → `rules`)

### ACE inhibitors and ARBs

**rasi_potassium_gt_5_5**: `[rx_class:ace_inhibitor | rx_class:arb] & lab:potassium_gt_5_5`
- KDIGO24, Figure 32: "Actions to manage hyperkalemia (potassium >5.5 mmol/l) in chronic kidney disease." The figure lists first-line actions (review non-RASi medications, dietary potassium), then second-line medications, and then "3rd line: ... Reduce dose or discontinue RASi/MRA".
- Lisinopril label 5.5: "Serum potassium should be monitored periodically in patients receiving lisinopril." Cozaar label 5.4: "Monitor serum potassium periodically and treat appropriately. Dosage reduction or discontinuation of COZAAR may be required."
- Reviewer note: KDIGO uses 5.5 mmol/L as an action threshold that starts a stepwise plan. It is not a stop rule. The gate routes the case to a pharmacist and does not stop the drug.

**rasi_egfr_lt_15**: `[ace | arb] & lab:egfr_lt_15`
- KDIGO24, Practice Point 3.6.5: "Consider reducing the dose or discontinuing ACEi or ARB in the setting of either symptomatic hypotension or uncontrolled hyperkalemia despite medical treatment, or to reduce uremic symptoms while treating kidney failure (estimated glomerular filtration rate [eGFR] <15 ml/min per 1.73 m2)."
- Practice Point 3.6.7: "Continue ACEi or ARB in people with CKD even when the eGFR falls below 30 ml/min per 1.73 m2." For this reason, the rule does not use eGFR < 30.

**rasi_pregnancy_possible**: `[ace | arb] & preg:possible`
- Lisinopril label, Boxed Warning: "When pregnancy is detected, discontinue lisinopril as soon as possible." Cozaar label, Boxed Warning: "When pregnancy is detected, discontinue COZAAR as soon as possible. Drugs that act directly on the renin-angiotensin system can cause injury and death to the developing fetus."

**ace_inhibitor_allergy**: `rx_class:ace_inhibitor & allergy_class:ace_inhibitor`
- Lisinopril label, 4 Contraindications: "a history of angioedema or hypersensitivity related to previous treatment with an angiotensin converting enzyme inhibitor"; "hereditary or idiopathic angioedema".

**arb_allergy**: `rx_class:arb & allergy_class:arb`
- Cozaar label, 4 Contraindications: "Hypersensitivity to any component."

### Diuretics

**spironolactone_potassium_gt_5_5**: `rx_class:spironolactone & lab:potassium_gt_5_5`
- KDIGO24, Figure 26 (finerenone protocol): "K+ >5.5 mmol/l ... Hold finerenone". The legend says: "This algorithm could be used for steroidal MRA."
- Spironolactone label 5.1: "Monitor serum potassium within 1 week of initiation or titration of spironolactone and regularly thereafter."

**spironolactone_crcl_lt_30_age_ge_65**: `rx_class:spironolactone & age_ge_65 & lab:crcl_lt_30`
- BEERS23, Table 6: "Spironolactone | <30 | Hyperkalemia | Avoid | Moderate | Strong". The Beers criteria apply to "adults 65 years old and older" (Intent of Criteria).

**thiazide_sulfonamide_allergy**: `rx_class:thiazide & allergy_class:sulfonamide`
- Hydrochlorothiazide label, Contraindications: "Hypersensitivity to this product or to other sulfonamide-derived drugs".

### Metformin

**metformin_egfr_lt_30**: `rx_class:metformin & lab:egfr_lt_30`
- Metformin label 2.4: "Discontinue metformin hydrochloride tablets/metformin hydrochloride extended-release tablets if the patient's eGFR later falls below 30 mL/minute/1.73 m2". Label 4: "Severe renal impairment (eGFR below 30 mL/min/1.73 m2)" is listed as a contraindication.

**metformin_egfr_lt_45**: `rx_class:metformin & lab:egfr_lt_45`
- Metformin label 2.4: "In patients taking metformin ... whose eGFR later falls below 45 mL/min/1.73 m2, assess the benefit risk of continuing therapy." The highlights read: "Assess risk/benefit of continuing if eGFR falls below 45 mL/minute/1.73 m2".

### SGLT2 inhibitors

The two drugs have different label thresholds, so the rules use drug-level `rx_class` values.

**empagliflozin_egfr_lt_30**
- Jardiance label, 1 Indications (Limitations of Use): "JARDIANCE is not recommended for use to improve glycemic control in patients with type 2 diabetes mellitus with an eGFR less than 30 mL/min/1.73 m2".

**dapagliflozin_egfr_lt_45**
- Farxiga label 2.2 and 1: "FARXIGA is not recommended for use to improve glycemic control in patients with type 2 diabetes mellitus with an eGFR less than 45 mL/min/1.73 m2". Label 2: "Initiation with FARXIGA is not recommended in patients with an eGFR less than 25 mL/min/1.73 m2".

Both SGLT2 rules also use KDIGO24, Practice Point 3.7.1: "Once an SGLT2i is initiated, it is reasonable to continue an SGLT2i even if the eGFR falls below 20 ml/min per 1.73 m2, unless it is not tolerated or KRT is initiated." For this reason, the finding asks the pharmacist to confirm the indication instead of stopping the drug.

### Sulfonylureas

**glyburide_age_ge_65**
- ADA25-S13, Pharmacologic Therapy, Insulin Secretagogues: "If used, sulfonylureas with a shorter duration of action, such as glipizide, are preferred, and frequency of hypoglycemia monitored at each visit. Glyburide is a longer-acting sulfonylurea and should be avoided in older adults."
- BEERS23, Table 2: "If a sulfonylurea is used, choose short-acting agents (e.g., glipizide) over long- acting agents (e.g., glyburide, glimepiride)."
- Reviewer note: ADA S13 does not define "older adults" by a fixed age. The ≥65 cut point comes from Beers.

**sulfonylurea_age_ge_65**
- BEERS23, Table 2, "Sulfonylureas (all, including short- and longer-acting)": "Avoid sulfonylureas as first- or second-line monotherapy or add-on therapy unless there are substantial barriers to the use of safer and more effective agents." Quality: hypoglycemia High; strength Strong.
- Reviewer note: this rule fires on every sulfonylurea refill in an adult aged 65 or older. Check the expected volume before sign-off.

**sulfonylurea_hypoglycemia**: `rx_class:sulfonylurea & hx:hypoglycemia_since_last_review`
- ADA25-S13, Recommendation 13.4: "Ascertain and address episodes of hypoglycemia at routine visits because older adults with diabetes have a greater risk of hypoglycemia, especially when treated with hypoglycemic agents (e.g., sulfonylureas, meglitinides, and insulin)."
- ADA25-S13, Recommendation 13.16a: "Deintensify hypoglycemia-causing medications (e.g., insulin, sulfonylureas, or meglitinides) or switch to a medication class with low hypoglycemia risk for individuals who are at high risk for hypoglycemia".
- Glipizide label, Precautions (General, Hypoglycemia): "All sulfonylurea drugs are capable of producing severe hypoglycemia."
- Reviewer note: the definition of the predicate (which episodes count, and the look-back period) is lane policy and needs sign-off.

**sulfonylurea_allergy**
- Glipizide label, Contraindications: "Glipizide is contraindicated in patients with: 1. Known hypersensitivity to the drug."

### Statins

**statin_pregnancy_possible**
- Lipitor label 8.1: "Discontinue LIPITOR when pregnancy is recognized. Alternatively, consider the ongoing therapeutic needs of the individual patient." Simvastatin label 8.1: "Discontinue simvastatin when pregnancy is recognized. Alternatively, consider the ongoing therapeutic needs of the individual patient."

**statin_allergy**
- Lipitor label 4: "Hypersensitivity to atorvastatin or any excipients in LIPITOR."

### Lithium

**lithium_level_gt_1_2**
- Lithium label, Warnings: "The toxic concentrations for lithium (≥1.5 mEq/L) are close to the therapeutic range (0.8 to 1.2 mEq/L)."
- Lithium label, Dosage and Administration: "Desirable serum lithium concentrations are 0.6 to 1.2 mEq/L".
- Reviewer note: NICE185 1.10.15 recommends a lower target, "between 0.6 and 0.8 mmol per litre in people being prescribed lithium for the first time." The rule uses the label upper limit. The label range "0.6 to 1.2" includes 1.2, so `gt` is the correct operator here.

### Anticoagulants

**warfarin_route_pharmacist**: `rx_class:warfarin` (always fires)
- Warfarin label 2.4: "Warfarin sodium has a narrow therapeutic range (index), and its action may be affected by factors such as other drugs and dietary vitamin K. Therefore, anticoagulation must be carefully monitored during warfarin sodium therapy."

**rivaroxaban_crcl_lt_15**
- Xarelto label 2.1, Table 1: for treatment of DVT/PE, reduction in the risk of recurrence, and DVT prophylaxis, "CrCl <15 mL/min | Avoid Use".
- BEERS23, Table 6: "Avoid if CrCl <15 mL/ min."

**rivaroxaban_crcl_le_50**: `rx_class:rivaroxaban & lab:crcl_le_50`
- Xarelto label 2.1, Table 1, NVAF: "CrCl >50 mL/min | 20 mg once daily"; "CrCl ≤50 mL/min | 15 mg once daily".
- BEERS23, Table 6: "Reduce the dose if CrCl is 15–50 mL/min following manufacturer dosing recommendations based on indication-specific dosing."

**dabigatran_crcl_lt_30**
- Dabigatran label 2.2, NVAF: "CrCl > 30 mL/min: 150 mg twice daily"; "CrCl 15 to 30 mL/min: 75 mg twice daily"; "CrCl < 15 mL/min or on dialysis: Dosing recommendations cannot be provided".
- BEERS23, Table 6: "Avoid when CrCl <30 mL/min; dose adjustment is advised when CrCl >30 mL/min in the presence of drug-drug interactions."

**apixaban_dose_reduction_criteria**: at least 2 of (`age_ge_80`, `weight_le_60_kg`, `lab:creatinine_ge_1_5`), written as `(A|B) & (A|C) & (B|C)`
- Eliquis label 2.1: "In patients with at least 2 of the following characteristics: age greater than or equal to 80 years, body weight less than or equal to 60 kg, or serum creatinine greater than or equal to 1.5 mg/dL, the recommended dose is 2.5 mg orally twice daily."

### Teratogens with pregnancy not excluded

**valproate_pregnancy_possible**
- Divalproex label, Boxed Warning: "Valproate is therefore contraindicated for prophylaxis of migraine headaches in pregnant women and in women of childbearing potential who are not using effective contraception ... Valproate should not be used to treat women with epilepsy or bipolar disorder who are pregnant or who plan to become pregnant unless other medications have failed to provide adequate symptom control or are otherwise unacceptable."

**methotrexate_pregnancy_possible**
- Methotrexate label, Boxed Warning: "Methotrexate tablets can cause embryo-fetal toxicity, including fetal death. For non- neoplastic diseases, methotrexate tablets are contraindicated in pregnancy."

**topiramate_pregnancy_possible**
- Topiramate label 5.7: "Topiramate can cause fetal harm when administered to a pregnant woman. Data from pregnancy registries indicate that infants exposed to topiramate in utero have an increased risk of major congenital malformations, including but not limited to cleft lip and/or cleft palate (oral clefts)".

### Always out of lane

**isotretinoin_out_of_lane**: `rx_class:isotretinoin` (always fires; kind `out_of_lane`, routes to the ordering clinician)
- Zenatane label 5.2: "Zenatane is available only through a restricted program under a Risk Evaluation and Mitigation Strategy (REMS) called the iPLEDGE REMS".

**controlled_substance_out_of_lane**: `controlled_substance` (always fires; kind `out_of_lane`, routes to the ordering clinician)
- 21 CFR 1306.12(a): "The refilling of a prescription for a controlled substance listed in Schedule II is prohibited."
- 21 CFR 1306.22(a): "No prescription for a controlled substance listed in Schedule III or IV shall be filled or refilled more than six months after the date on which such prescription was issued. No prescription for a controlled substance listed in Schedule III or IV authorized to be refilled may be refilled more than five times."
- Example: Metadate CD label 9.1: "METADATE CD contains methylphenidate, a Schedule II controlled substance."
- Reviewer note: the regulation covers Schedules II to IV. Keeping Schedules III to V out of the lane is a lane-policy choice that goes further than the regulation.

### NSAIDs (chronic use)

**nsaid_crcl_lt_30_age_ge_65**
- BEERS23, Table 6: "NSAIDs (non-selective, COX-2 selective, and nonacetylated salicylates, oral and parenteral) | < 30 | May increase the risk of acute kidney injury and a further decline in kidney function | Avoid | Moderate | Strong".

**nsaid_chronic_age_ge_65**
- BEERS23, Table 2, Non-COX-2-selective NSAIDs, oral: "Avoid chronic use unless other alternatives are not effective and the patient can take a gastroprotective agent (proton-pump inhibitor or misoprostol)."

**nsaid_allergy**
- Ibuprofen label, Contraindications: "Ibuprofen tablets should not be given to patients who have experienced asthma, urticaria, or allergic-type reactions after taking aspirin or other NSAIDs."
- Naproxen DR label 4: "History of asthma, urticaria, or other allergic-type reactions after taking aspirin or other NSAIDs."

### AV-nodal agents and conduction disease

**av_nodal_agent_conduction_disease**: `[rx_class:beta_blocker | rx_class:nondhp_ccb | rx_class:amiodarone] & dx:av_block_gt_first_degree_or_sick_sinus_without_pacemaker`
- Metoprolol succinate ER label 4: "Metoprolol succinate extended-release tablets are contraindicated in severe bradycardia, second- or third- degree heart block, cardiogenic shock, decompensated heart failure, sick sinus syndrome (unless a permanent pacemaker is in place), and in patients who are hypersensitive to any component of this product."
- Coreg label 4: "Second- or third-degree AV block." and "Sick sinus syndrome."
- Tenormin label, Contraindications: "TENORMIN is contraindicated in sinus bradycardia, heart block greater than first degree, cardiogenic shock, and overt cardiac failure."
- Propranolol label, Contraindications: "Propranolol is contraindicated in 1) cardiogenic shock; 2) sinus bradycardia and greater than first degree block; 3) bronchial asthma; and 4) in patients with known hypersensitivity to propranolol hydrochloride."
- Cardizem CD label, Contraindications: "CARDIZEM CD is contraindicated in (1) patients with sick sinus syndrome except in the presence of a functioning ventricular pacemaker, (2) patients with second- or third-degree AV block except in the presence of a functioning ventricular pacemaker".
- Verapamil ER label, Contraindications: "Sick sinus syndrome (except in patients with a functioning artificial ventricular pacemaker)" and "Second- or third-degree AV block (except in patients with a functioning artificial ventricular pacemaker)".
- Amiodarone label 4: "Sick sinus syndrome, second- or third-degree atrioventricular block, bradycardia leading to syncope without a functioning pacemaker."
- Reviewer note: the labels also list "severe bradycardia" without a heart-rate number. We found no verified threshold, so the gate has no heart-rate rule.

### Beta-blockers

**nonselective_beta_blocker_asthma**: `[rx_class:propranolol | rx_class:carvedilol] & dx:asthma`
- Propranolol label, Contraindications: "3) bronchial asthma" (statement quoted above).
- Coreg label 4: "Bronchial asthma or related bronchospastic conditions. Deaths from status asthmaticus have been reported following single doses of COREG."
- Reviewer note: the metoprolol succinate label 5.3 says "Patients with bronchospastic diseases should, in general, not receive beta-blockers" but does not list asthma as a contraindication. Cardioselective agents are not in this rule.

**atenolol_crcl_le_35**: `rx_class:atenolol & lab:crcl_le_35`
- Tenormin label, Dosage and Administration: "The following maximum oral dosages are recommended for elderly, renally-impaired patients and for patients with renal impairment due to other causes". The table gives "15-35" mL/min/1.73m2 → "50 mg daily" and "<15" → "25 mg daily". The label also says: "No significant accumulation of TENORMIN occurs until creatinine clearance falls below 35 mL/min/1.73m2."
- Reviewer note: the label expresses CrCl per 1.73 m2. The other CrCl rules use Cockcroft-Gault in mL/min. The predicate builder must normalize to body surface area for this rule, or the pharmacist accepts the difference.

### Non-dihydropyridine calcium-channel blockers

**nondhp_ccb_sbp_lt_90**: `rx_class:nondhp_ccb & vital:sbp_lt_90`
- Cardizem CD label, Contraindications: "(3) patients with hypotension (less than 90 mm Hg systolic)".
- Verapamil ER label, Contraindications: "Hypotension (systolic pressure less than 90 mm Hg) or cardiogenic shock".

**nondhp_ccb_hfref**: `rx_class:nondhp_ccb & dx:hfref`
- BEERS23, Table 3 (Heart failure): "Avoid in heart failure with reduced ejection fraction: Nondihydropyridine calcium channel blockers (CCBs) Diltiazem Verapamil".
- Verapamil ER label, Contraindications: "Severe left ventricular dysfunction".
- Cardizem CD label, Warnings: "Worsening of congestive heart failure has been reported in patients with preexisting impairment of ventricular function."
- Reviewer note: Beers applies to adults 65 and older; the verapamil contraindication applies at any age. The rule has no age term.

### Clonidine

**clonidine_supply_lapsed**: `rx_class:clonidine & adherence:supply_lapsed`
- Clonidine tablet label, Warnings (Withdrawal): "Patients should be instructed not to discontinue therapy without consulting their physician. Sudden cessation of clonidine treatment has, in some cases, resulted in symptoms such as nervousness, agitation, headache, and tremor accompanied or followed by a rapid rise in blood pressure and elevated catecholamine concentrations in the plasma."
- Reviewer note: the label gives no gap length. Any lapse fires the rule. Lane policy decides whether a shorter grace period is acceptable.

**clonidine_htn_age_ge_65**: `rx_class:clonidine & age_ge_65 & indication:hypertension`
- BEERS23, Table 2: "Central alpha-agonists for the treatment of hypertension Clonidine Guanfacine" with the recommendation "Avoid clonidine as first-line treatment for hypertension."

### Hydralazine and nitrates

**hydralazine_lupus_like_symptoms**: `rx_class:hydralazine & sx:lupus_like_symptoms` (out_of_lane)
- Hydralazine label, Warnings: "In a few patients hydrALAZINE may produce a clinical picture simulating systemic lupus erythematosus including glomerulonephritis. In such patients hydrALAZINE should be discontinued unless the benefit-to-risk determination requires continued antihypertensive therapy with this drug."

**hydralazine_cad_or_rheumatic_mitral**: `rx_class:hydralazine & [dx:coronary_artery_disease | dx:rheumatic_mitral_valve_disease]`
- Hydralazine label, Contraindications: "Hypersensitivity to hydrALAZINE; coronary artery disease; mitral valvular rheumatic heart disease."
- Reviewer note: hydralazine is often prescribed with a nitrate in heart failure, and many such patients have coronary disease. Expect frequent coded overrides. Sign-off decides whether to keep this rule.

**nitrate_pde5_or_riociguat**: `rx_class:nitrate & [med:pde5_inhibitor | med:riociguat]`
- Isosorbide mononitrate tablet label (Coupler), Contraindications: "Do not use isosorbide mononitrate in patients who are taking certain drugs for erectile dysfunction (phosphodiesterase inhibitors), such as sildenafil, tadalafil, or vardenafil. Concomitant use can cause severe hypotension, syncope, or myocardial ischemia." and "Do not use isosorbide mononitrate in patients who are taking the soluble guanylate cyclase stimulator riociguat."

### GLP-1 receptor agonists and DPP-4 inhibitors

**glp1_ra_mtc_or_men2**: `rx_class:glp1_ra & dx:mtc_or_men2_personal_or_family`
- Ozempic label 4: "A personal or family history of MTC or in patients with MEN 2".
- Trulicity label 4: "Personal or family history of medullary thyroid carcinoma (MTC) or in patients with Multiple Endocrine Neoplasia syndrome type 2 (MEN 2)".
- Victoza label 4: "personal or family history of medullary thyroid carcinoma (MTC) or in patients with Multiple Endocrine Neoplasia syndrome type 2 (MEN 2)".

**incretin_pancreatitis_suspected**: `[rx_class:glp1_ra | rx_class:dpp4_inhibitor] & sx:pancreatitis_suspected` (out_of_lane)
- Ozempic label 5.2: "observe patients carefully for signs and symptoms of acute pancreatitis, which may include persistent or severe abdominal pain (sometimes radiating to the back), and which may or may not be accompanied by nausea or vomiting. If pancreatitis is suspected, discontinue OZEMPIC and initiate appropriate management."
- Trulicity label: "Discontinue if pancreatitis is suspected (5.2)." Victoza label: "Discontinue if pancreatitis is suspected. (5.2)"
- Januvia label: "If pancreatitis is suspected, promptly discontinue JANUVIA. (5.1)" Saxagliptin label: "If pancreatitis is suspected, promptly discontinue saxagliptin. (5.1)" Tradjenta label: "If pancreatitis is suspected, promptly discontinue TRADJENTA. (5.1)" Nesina label: "If pancreatitis is suspected, promptly discontinue NESINA. (5.1)"

**semaglutide_pregnancy_possible**: `rx_class:semaglutide & preg:possible`
- Ozempic label (Highlights, 8.3): "Discontinue OZEMPIC in women at least 2 months before a planned pregnancy due to the long washout period for semaglutide."
- Reviewer note: the label statement is about planned pregnancy. The rule fires when pregnancy is not excluded, which is broader.

**sitagliptin_egfr_lt_45**: `rx_class:sitagliptin & lab:egfr_lt_45`
- Januvia label 2.2: "For patients with moderate renal impairment (eGFR greater than or equal to 30 mL/min/1.73 m2 to less than 45 mL/min/1.73 m2), the dose of JANUVIA is 50 mg once daily." and "For patients with severe renal impairment (eGFR less than 30 mL/min/1.73 m2) or with end-stage renal disease (ESRD) requiring hemodialysis or peritoneal dialysis, the dose of JANUVIA is 25 mg once daily."

**saxagliptin_egfr_lt_45**: `rx_class:saxagliptin & lab:egfr_lt_45`
- Saxagliptin label (Highlights, 2.2): "Patients with an eGFR < 45 mL/min/1.73 m2 (moderate or severe renal impairment, or end-stage renal disease): Recommended dosage is 2.5 mg once daily regardless of meals."

**dpp4_heart_failure**: `[rx_class:saxagliptin | rx_class:alogliptin] & dx:heart_failure`
- Saxagliptin label 5.2: "Consider the risks and benefits of saxagliptin prior to initiating treatment in patients at a higher risk for heart failure. Observe patients for signs and symptoms of heart failure during therapy."
- Nesina label (Highlights, 5.2): "If heart failure develops, evaluate and manage according to current standards of care and consider discontinuation of NESINA."

### Basal insulin

**basal_insulin_hypoglycemia**: `rx_class:basal_insulin & hx:hypoglycemia_since_last_review`
- ADA26-S6, Recommendation 6.6: "Deintensify hypoglycemia-causing medications (insulin, sulfonylureas, or meglitinides), or switch to a medication class with lower hypoglycemia risk, for individuals who are at high risk for hypoglycemia, within individualized glycemic goals."
- ADA26-S6, Recommendation 6.10: "Review history of hypoglycemia at every clinical encounter for all individuals at risk for hypoglycemia, and evaluate hypoglycemic events as indicated."
- Lantus label 5.3: "Hypoglycemia is the most common adverse reaction associated with insulins, including LANTUS. Severe hypoglycemia can cause seizures, may be life-threatening or cause death."
- Reviewer note: this lane renews basal insulin at the same dose only. Any dose change belongs to the dm_titration lane (`titration.yaml`).

**hypoglycemic_agent_level_2_or_3_hypoglycemia**: `[rx_class:basal_insulin | rx_class:sulfonylurea] & hx:hypoglycemia_level_2_or_3_since_last_review` (out_of_lane)
- ADA26-S6, Recommendation 6.19: "One or more episodes of level 2 or 3 hypoglycemia should prompt reevaluation of the treatment plan, including deintensifying or switching diabetes medications if appropriate."
- ADA26-S6, Hypoglycemia section: "Level 2 hypoglycemia (defined as a blood glucose concentration <54 mg/dL [<3.0 mmol/L])" and "level 3 hypoglycemia is defined as a severe event characterized by altered mental and/or physical functioning that requires assistance from another person for recovery, irrespective of glucose level."

### Pioglitazone

**pioglitazone_symptomatic_heart_failure**: `rx_class:pioglitazone & dx:symptomatic_heart_failure`
- Actos label, Boxed Warning: "Thiazolidinediones, including ACTOS®, cause or exacerbate congestive heart failure in some patients". Label 4: "Initiation in patients with established NYHA Class III or IV heart failure".
- BEERS23, Table 3 (Heart failure): "Use with caution in patients with heart failure who are asymptomatic; avoid in patients with symptomatic heart failure: Dronedarone NSAIDs and COX-2 inhibitors Thiazolidinediones Pioglitazone".
- Reviewer note: the label contraindication is for initiation in NYHA III-IV. For a continuing patient, the rule uses the Beers "symptomatic heart failure" wording.

**pioglitazone_active_bladder_cancer**: `rx_class:pioglitazone & dx:active_bladder_cancer`
- Actos label (Highlights, 5.4): "Bladder cancer: May increase the risk of bladder cancer. Do not use in patients with active bladder cancer."

### Xanthine oxidase inhibitors

**allopurinol_new_rash**: `rx_class:allopurinol & sx:new_skin_rash` (out_of_lane)
- Allopurinol label (Highlights, 5.1): "Allopurinol has been associated with serious and sometimes fatal dermatological reactions. Discontinue allopurinol tablets at the first appearance of skin rash or other signs of hypersensitivity reaction."

**allopurinol_azathioprine_mercaptopurine**: `rx_class:allopurinol & med:azathioprine_or_mercaptopurine`
- Allopurinol label 7: "Concomitant use with allopurinol increases the exposure of either mercaptopurine or azathioprine which may increase the risk of myelosuppression. Reduce the dosage of mercaptopurine or azathioprine as recommended in their respective prescribing information when used concomitantly with allopurinol tablets".

**febuxostat_azathioprine_mercaptopurine**: `rx_class:febuxostat & med:azathioprine_or_mercaptopurine`
- Uloric label 4: "ULORIC is contraindicated in patients being treated with azathioprine or mercaptopurine".

**febuxostat_established_cv_disease**: `rx_class:febuxostat & dx:established_cardiovascular_disease`
- Uloric label, Boxed Warning: "Gout patients with established cardiovascular (CV) disease treated with ULORIC had a higher rate of CV death compared to those treated with allopurinol in a CV outcomes study." and "ULORIC should only be used in patients who have an inadequate response to a maximally titrated dose of allopurinol, who are intolerant to allopurinol, or for whom treatment with allopurinol is not advisable."

**febuxostat_crcl_lt_30_dose_gt_40**: `rx_class:febuxostat & lab:crcl_lt_30 & dose:febuxostat_daily_mg_gt_40`
- Uloric label 8.6: "For patients with severe renal impairment (Clcr 15 to 29 mL/min), the recommended dosage of ULORIC is limited to 40 mg once daily".

### Inhaled LABA, ICS/LABA, and LAMA

**laba_monotherapy_asthma**: `rx_class:laba_monotherapy & dx:asthma`
- Serevent Diskus label 4: "Use of SEREVENT DISKUS for the treatment of asthma without concomitant use of an ICS is contraindicated".
- Reviewer note: the gate cannot test "no ICS" (no negation), so the rule fires on every salmeterol refill for a person with asthma. The pharmacist resolves it with a coded override when an ICS is active.

**asthma_controller_increasing_saba_use**: `[rx_class:ics_laba | rx_class:laba_monotherapy] & dx:asthma & hx:increasing_saba_use` (out_of_lane)
- Advair HFA label 5.2 and Serevent Diskus label 5.2: "Increasing use of inhaled, short-acting beta2-agonists is a marker of deteriorating asthma. In this situation, the patient requires immediate reevaluation with reassessment of the treatment regimen".

**tiotropium_ipratropium_allergy**: `rx_class:tiotropium & allergy_class:tiotropium_or_ipratropium`
- Spiriva HandiHaler label 4: "SPIRIVA HANDIHALER is contraindicated in patients with a hypersensitivity to tiotropium, ipratropium, or any components of this product".

### Montelukast

**montelukast_neuropsychiatric_symptoms**: `rx_class:montelukast & sx:new_neuropsychiatric_symptoms` (out_of_lane)
- Singulair label, Boxed Warning: "Serious neuropsychiatric (NP) events have been reported with the use of SINGULAIR." and "If changes in behavior are observed, or if new NP symptoms or suicidal thoughts and/or behavior occur, advise patients to discontinue SINGULAIR and contact a healthcare provider immediately".

### Antidepressants (SSRIs, SNRIs, mirtazapine, trazodone)

**serotonergic_or_bupropion_with_maoi**: `[ssri | snri | mirtazapine | trazodone | bupropion] & med:maoi_within_14_days`
- Zoloft label 4: "Taking, or within 14 days of stopping, MAOIs, (including the MAOIs linezolid and intravenous methylene blue) because of an increased risk of serotonin syndrome".
- Lexapro label: "Do not use MAOIs intended to treat psychiatric disorders with Lexapro or within 14 days of stopping treatment with Lexapro. Do not use Lexapro within 14 days of stopping an MAOI intended to treat psychiatric disorders."
- Celexa label 4: "taking, or within 14 days of stopping, MAOIs (including MAOIs such as linezolid or intravenous methylene blue) because of an increased risk of serotonin syndrome".
- Prozac label: "The use of PROZAC within 14 days of stopping an MAOI intended to treat psychiatric disorders is also contraindicated".
- Paxil CR label 4: "Taking, or within 14 days of stopping, MAOIs (including the MAOIs linezolid and intravenous methylene blue) because of an increased risk of serotonin syndrome".
- Duloxetine DR label: "The use of MAOIs intended to treat psychiatric disorders with duloxetine delayed-release capsules or within 5 days of stopping treatment with duloxetine delayed-release capsules are contraindicated because of an increased risk of serotonin syndrome."
- Venlafaxine ER label 4: "taking, or within 14 days of stopping, MAOIs (including the MAOIs linezolid and intravenous methylene blue) because of increased risk of serotonin syndrome".
- Remeron label 4: "Taking, or within 14 days of stopping, MAOIs (including the MAOIs linezolid and intravenous methylene blue) because of an increased risk of serotonin syndrome".
- Trazodone label 4: "Patients taking, or within 14 days of stopping, monoamine oxidase inhibitors (MAOIs), including MAOIs such as linezolid or intravenous methylene blue, because of an increased risk of serotonin syndrome".
- Wellbutrin XL label 4: "The use of MAOIs (intended to treat psychiatric disorders) concomitantly with Wellbutrin XL or within 14 days of discontinuing treatment with Wellbutrin XL is contraindicated. There is an increased risk of hypertensive reactions when Wellbutrin XL is used concomitantly with MAOIs."

**ssri_snri_with_anticoagulant**: `[ssri | snri] & med:anticoagulant`
- Zoloft label 5.3: "Drugs that interfere with serotonin reuptake inhibition, including ZOLOFT, increase the risk of bleeding events. Concomitant use of aspirin, nonsteroidal anti-inflammatory drugs (NSAIDs), other antiplatelet drugs, warfarin, and other anticoagulants may add to this risk."
- Venlafaxine ER label (Highlights, 5.4): "Concomitant use of aspirin, NSAIDs, other antiplatelet drugs, warfarin, and other anticoagulants may increase risk (5.4)."
- BEERS23, Table 5: object drug "Warfarin", interacting drugs include "SSRIs", recommendation "Avoid when possible; if used together, monitor INR closely."
- Reviewer note: the labels also name aspirin, NSAIDs, and antiplatelet drugs. This draft limits the rule to anticoagulants, as requested. Adding `med:antiplatelet` and `med:nsaid` is a one-line change.

**antidepressant_low_sodium_age_ge_65**: `[ssri | snri | mirtazapine | carbamazepine] & age_ge_65 & ref:sodium_below_lln`
- BEERS23, Table 4: "Antidepressants (selected) Mirtazipine SNRIs SSRIs TCAs Antiepileptics (selected) Carbamazepine Oxcarbazepine" with rationale "May exacerbate or cause SIADH or hyponatremia; monitor sodium levels closely when starting or changing dosages in older adults." and recommendation "Use with caution".
- Zoloft label 5.8: "Elderly patients, patients taking diuretics, and those who are volume-depleted may be at greater risk of developing hyponatremia with SSRIs and SNRIs".
- Venlafaxine ER label 5.9: "Elderly patients may be at greater risk of developing hyponatremia with SSRIs and SNRIs."
- Remeron label (Highlights, 5.12): "Hyponatremia: May occur as a result of treatment with serotonergic antidepressants, including REMERON/REMERONSolTab. (5.12)"
- Reviewer note: no source gives a sodium number for a stable refill. The predicate uses the reporting laboratory's lower reference limit, which avoids an invented threshold.

**citalopram_age_gt_60_dose_gt_20**: `rx_class:citalopram & age_gt_60 & dose:citalopram_daily_mg_gt_20`
- Celexa label 2: "The maximum recommended dosage of CELEXA for patients who are greater than 60 years of age, patients with hepatic impairment, and for CYP2C19 poor metabolizers is 20 mg once daily".

**duloxetine_crcl_lt_30**: `rx_class:duloxetine & lab:crcl_lt_30`
- Duloxetine DR label 8.10: "Severe Renal Impairment — Avoid use in patients with severe renal impairment, GFR <30 mL/min".
- BEERS23, Table 6: "Duloxetine | <30 | Increased GI adverse effects (nausea, diarrhea) | Avoid".

**anticholinergic_antidepressant_age_ge_65**: `rx_class:anticholinergic_antidepressant & age_ge_65`
- BEERS23, Table 2: "Antidepressants with strong anticholinergic activity, alone or in combination Amitriptyline Amoxapine Clomipramine Desipramine Doxepin >6 mg/day Imipramine Nortriptyline Paroxetine" with recommendation "Avoid".

### Bupropion

**bupropion_seizure_disorder**, **bupropion_eating_disorder**
- Wellbutrin XL label 4: "Wellbutrin XL is contraindicated in patients with seizure disorder." and "Wellbutrin XL is contraindicated in patients with a current or prior diagnosis of bulimia or anorexia nervosa as a higher incidence of seizures was observed in such patients treated with Wellbutrin XL".

**bupropion_dose_gt_450**
- Wellbutrin XL label (Highlights): "Seizure Risk: The risk is dose-related. Can minimize risk by limiting daily dose to 450 mg and gradually increasing the dose." Label 5.3: "The risk of seizure can be reduced if the Wellbutrin XL dose does not exceed 450 mg once daily and the titration rate is gradual."

### Gabapentinoids

**gabapentin_crcl_lt_60**: `rx_class:gabapentin & lab:crcl_lt_60`
- Neurontin label 2, Table 1 (Dosage Based on Renal Function): "≥ 60" mL/min → "900 to 3600" mg/day; ">30 to 59" → "400 to 1400"; ">15 to 29" → "200 to 700"; and "For patients with creatinine clearance <15 mL/min, reduce daily dose in proportion to creatinine clearance".
- BEERS23, Table 6: "Gabapentin | <60 | CNS adverse effects | Reduce dose".

**gabapentinoid_with_opioid**: `[gabapentin | pregabalin] & med:opioid`
- Neurontin label (Highlights, 5.8): "Respiratory Depression: May occur with NEURONTIN when used with concomitant central nervous system (CNS) depressants, including opioids, or in the setting of underlying respiratory impairment."
- BEERS23, Table 5: "Opioids | Gabapentin Pregabalin | Increased risk of severe sedation-related adverse events, including respiratory depression and death. | Avoid".

**Pregabalin**: no separate refill rule. Pregabalin label 9.1: "Pregabalin is a Schedule V controlled substance." Every pregabalin refill fires `controlled_substance_out_of_lane` (kind `out_of_lane`).

### First-generation antihistamines and strong anticholinergics (age ≥65)

**first_gen_antihistamine_age_ge_65**: `rx_class:first_generation_antihistamine & age_ge_65`
- BEERS23, Table 2: "First-generation antihistamines Brompheniramine Chlorpheniramine Cyproheptadine Dimenhydrinate Diphenhydramine (oral) Doxylamine Hydroxyzine Meclizine Promethazine Triprolidine", recommendation "Avoid", quality "Moderate", strength "Strong".

**strong_anticholinergic_dementia_or_delirium**: `rx_class:strong_anticholinergic & age_ge_65 & [dx:dementia_or_cognitive_impairment | dx:delirium_or_high_delirium_risk]`
- BEERS23, Table 3, Delirium: "Anticholinergics (see Table 7)" with "Avoid in older adults with or at high risk of delirium because of the potential of inducing or worsening delirium." Dementia or cognitive impairment: "Anticholinergics (see Table 7)" with "Avoid because of adverse CNS effects."
- BEERS23, Table 7 lists the drugs: antidepressants (amitriptyline, amoxapine, clomipramine, desipramine, doxepin >6 mg/day, imipramine, nortriptyline, paroxetine), antiemetics (prochlorperazine, promethazine), first-generation antihistamines, antimuscarinics for urinary incontinence (darifenacin, fesoterodine, flavoxate, oxybutynin, solifenacin, tolterodine, trospium), and antiparkinsonian agents (benztropine). `rx_class:strong_anticholinergic` means a drug on this list.

**strong_anticholinergic_combination_age_ge_65**: `rx_class:strong_anticholinergic & age_ge_65 & med:strong_anticholinergic`
- BEERS23, Table 5: "Anticholinergic | Anticholinergic | Use of more than one medication with anticholinergic properties increases the risk of cognitive decline, delirium, and falls or fractures. | Avoid; minimize the number of anticholinergic drugs (Table 7)."

### Acid suppression

**ppi_scheduled_gt_8_weeks_age_ge_65**: `rx_class:ppi & age_ge_65 & therapy:scheduled_use_gt_8_weeks`
- BEERS23, Table 2, Proton-pump inhibitors: "Avoid scheduled use for >8 weeks unless for high-risk patients (e.g., oral corticosteroids or chronic NSAID use), erosive esophagitis, Barrett’s esophagitis, pathologic hypersecretory condition, or demonstrated need for maintenance treatment".
- Reviewer note: the exceptions cannot be expressed (no negation), so the pharmacist resolves them with a coded override.

**famotidine_crcl_lt_60**: `rx_class:famotidine & lab:crcl_lt_60`
- Famotidine label 2.2: "Dosage adjustments of famotidine tablets are recommended for patients with moderate to severe renal impairment (creatinine clearance less than 60 mL/min)". The label table gives maximum dosages for "Creatinine clearance 30 to 60 mL/minute" and "Creatinine clearance less than 30 mL/minute".
- BEERS23, Table 6: "Famotidine | <50 | Mental status changes | Reduce dose". The rule uses the label value (60), which is the stricter of the two.

### Oral bisphosphonates

**alendronate_crcl_lt_35**
- Alendronate label 5.6 and 8.6: "Alendronate sodium is not recommended for patients with creatinine clearance less than 35 mL/min."

**risedronate_crcl_lt_30**
- Risedronate DR label 8.6: "Risedronate sodium delayed-release is not recommended for use in patients with severe renal impairment (creatinine clearance less than 30 mL/min) because of lack of clinical experience."

**oral_bisphosphonate_contraindication**: `[alendronate | risedronate] & [ref:calcium_below_lln | sx:cannot_stay_upright_30_min]`
- Alendronate label 4 and risedronate DR label 4 both list "Inability to stand or sit upright for at least 30 minutes" and "Hypocalcemia".

### Tamsulosin and finasteride

**tamsulosin_strong_cyp3a4_inhibitor**
- Flomax label 5.2: "FLOMAX capsules 0.4 mg should not be used in combination with strong inhibitors of CYP3A4 (e.g., ketoconazole)".

**tamsulosin_sulfa_allergy** (kind allergy)
- Flomax label 5.6: "In patients with sulfa allergy, allergic reaction to FLOMAX capsules has been rarely reported. If a patient reports a serious or life-threatening sulfa allergy, caution is warranted when administering FLOMAX capsules."

**finasteride_pregnancy_possible**
- Proscar label 4: "Pregnancy. Finasteride use is contraindicated in females when they are or may potentially be pregnant."

### Antiepileptics

**carbamazepine_pregnancy_possible**
- Tegretol label, Warnings (Usage in Pregnancy): "Carbamazepine can cause fetal harm when administered to a pregnant woman." and "Epidemiological data suggest that there may be an association between the use of carbamazepine during pregnancy and congenital malformations, including spina bifida."

**carbamazepine_nefazodone_or_maoi**
- Tegretol label, Contraindications: "Coadministration of carbamazepine with nefazodone is contraindicated." and "Before administration of Tegretol, MAO inhibitors should be discontinued for a minimum of 14 days, or longer if the clinical situation permits."

**lamotrigine_new_rash** (out_of_lane)
- Lamictal label (Highlights): "Life-threatening serious rash and/or rash-related death: Discontinue at the first sign of rash, unless the rash is clearly not drug related. (Boxed Warning, 5.1)"

**lamotrigine_supply_lapsed**
- Lamictal label 2.1: "If a patient has discontinued lamotrigine for a period of more than 5 half-lives, it is recommended that initial dosing recommendations and guidelines be followed."
- Reviewer note: the half-life depends on co-medication (valproate and enzyme inducers), so the lane does not compute "5 half-lives". Any lapse fires the rule, and the pharmacist decides.

**levetiracetam_crcl_le_80**
- Keppra label 2, Table 1: "Mild | 50 – 80 | 500 to 1,000 | Every 12 hours", "Moderate | 30 – 50 | 250 to 750", "Severe | < 30 | 250 to 500" (CrCl in mL/min/1.73 m2).
- BEERS23, Table 6: "Levetiracetam | ≤80 | CNS adverse effects | Reduce dose".

Carbamazepine also appears in `antidepressant_low_sodium_age_ge_65` (Beers Table 4).

### Amiodarone

**amiodarone_alt_gt_3x_uln**: `rx_class:amiodarone & ref:alt_gt_3x_uln`
- Amiodarone label, Boxed Warning: "Obtain baseline and periodic liver transaminases and discontinue or reduce dose if the increase exceeds three times normal, or doubles in a patient with an elevated baseline."
- Reviewer note: the second arm of the boxed warning (a doubling from an elevated baseline) is not encoded. It needs a baseline-relative predicate.

**amiodarone_warfarin_age_ge_65**
- BEERS23, Table 5: object drug "Warfarin", interacting drugs include "Amiodarone", rationale "Increased risk of bleeding.", recommendation "Avoid when possible; if used together, monitor INR closely."

Amiodarone also appears in `av_nodal_agent_conduction_disease`.

### Digoxin

**digoxin_level_gt_2**: `rx_class:digoxin & lab:digoxin_gt_2`
- Digoxin tablet label 2.5: "Serum digoxin levels less than 0.5 ng/mL have been associated with diminished efficacy, while levels above 2 ng/mL have been associated with increased toxicity without increased benefit."

**digoxin_dose_gt_0_125_age_ge_65**
- BEERS23, Table 2: "If used for atrial fibrillation or heart failure, avoid dosages >0.125 mg/day."

### Lithium toxic level

**lithium_level_ge_1_5**: `rx_class:lithium & lab:lithium_ge_1_5` (out_of_lane)
- Lithium label, Warnings: "The toxic concentrations for lithium (≥1.5 mEq/L) are close to the therapeutic range (0.8 to 1.2 mEq/L)." The rule uses `ge` to match "≥1.5".

## Lab-recency rules (`refill.yaml` → `lab_recency`)

| id | Class | LOINC | Days | Statement |
|---|---|---|---|---|
| metformin_egfr_annual | metformin | 2160-0, 98979-8, 62238-1, 33914-3 | 365 | Metformin label 5.1: "Obtain an eGFR at least annually in all patients taking metformin". |
| levothyroxine_tsh | levothyroxine | 3016-3 | 365 | Levothyroxine label 2.4: "In patients on a stable and appropriate replacement dosage, evaluate clinical and biochemical response every 6 to 12 months". The rule uses the upper end of the range. |
| lithium_level | lithium | 14334-7 | 60 | Lithium label, Dosage and Administration: "Serum lithium concentrations in uncomplicated cases receiving maintenance therapy during remission should be monitored at least every two months." |
| lithium_tsh | lithium | 3016-3 | 183 | NICE185 1.10.21: "arrange tests for urea and electrolytes including calcium, estimated glomerular filtration rate (eGFR) and thyroid function every 6 months". |
| lithium_egfr | lithium | 2160-0, 98979-8, 62238-1, 33914-3 | 183 | NICE185 1.10.21 (same statement). |
| warfarin_inr | warfarin | 6301-6 | 28 | Warfarin label 2.4: "generally acceptable intervals for INR determinations are 1 to 4 weeks." |
| spironolactone_potassium | spironolactone | 2823-3 | 120 | KDIGO24 Figure 26: "Monitor K+ every 4 months"; "This algorithm could be used for steroidal MRA." |
| sga_hba1c_annual | second_generation_antipsychotic | 4548-4, 17856-6, 4549-2, 1558-6 | 365 | ADA25-S2, Recommendation 2.15b: "In people who are prescribed second-generation antipsychotic medications, screen for prediabetes and diabetes at baseline and repeat 12–16 weeks after medication initiation or sooner, if clinically indicated, and annually thereafter." APA-PIP Table 1: "Fasting blood glucose or HbA1c four months after initiating a new treatment and at least annually thereafter". |
| sga_lipids_annual | second_generation_antipsychotic | 2093-3 | 365 | APA-PIP Table 1: "Lipid panel four months after initiating a new antipsychotic medication and at least annually thereafter" (secondary source; see the Sources table). |

We converted month intervals to days: 2 months = 60, 4 months = 120, 6 months = 183, 12 months = 365, 4 weeks = 28.

### LOINC verification

We checked each code against the NLM Clinical Tables LOINC service (https://clinicaltables.nlm.nih.gov/api/loinc_items/v3/search) on 2026-10-27. The loinc.org pages were behind a bot challenge and could not be read directly.

| LOINC | Long common name |
|---|---|
| 2823-3 | Potassium [Moles/volume] in Serum or Plasma |
| 2951-2 | Sodium [Moles/volume] in Serum or Plasma (`ref:sodium_below_lln`) |
| 2160-0 | Creatinine [Mass/volume] in Serum or Plasma |
| 98979-8 | Glomerular filtration rate ... by Creatinine-based formula (CKD-EPI 2021)/1.73 sq M |
| 62238-1 | Glomerular filtration rate ... by Creatinine-based formula (CKD-EPI)/1.73 sq M |
| 33914-3 | Glomerular filtration rate ... by Creatinine-based formula (MDRD)/1.73 sq M |
| 3016-3 | Thyrotropin [Units/volume] in Serum or Plasma |
| 14334-7 | Lithium [Moles/volume] in Serum or Plasma |
| 6301-6 | INR in Platelet poor plasma by Coagulation assay |
| 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood |
| 17856-6 | Hemoglobin A1c/Hemoglobin.total in Blood by HPLC |
| 4549-2 | Hemoglobin A1c/Hemoglobin.total in Blood by Electrophoresis |
| 10535-3 | Digoxin [Mass/volume] in Serum or Plasma |
| 17861-6 | Calcium [Mass/volume] in Serum or Plasma (`ref:calcium_below_lln`) |
| 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma (`ref:alt_gt_3x_uln`) |
| 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma |
| 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma |

The eGFR recency rules accept creatinine 2160-0 or any of the three reported-eGFR codes, because every eGFR result is computed from a creatinine result. The antipsychotic glucose screen accepts any HbA1c method or a fasting glucose, because ADA25-S2 allows either test for diabetes screening.

## Monitoring contracts (`refill_monitoring.yaml`)

| id | Window (days) | Checks | Statement |
|---|---|---|---|
| ace_inhibitor_start_or_dose_change, arb_start_or_dose_change | 14–28 | creatinine rel. rise ≥ 0.30; potassium > 5.5 (`high: 5.5`) | KDIGO24 PP 3.6.2: "Changes in BP, serum creatinine, and serum potassium should be checked within 2–4 weeks of initiation or increase in the dose of a RASi". PP 3.6.4: "Continue ACEi or ARB therapy unless serum creatinine rises by more than 30% within 4 weeks following initiation of treatment or an increase in dose." |
| spironolactone_start_or_titration | 0–7 | potassium > 5.5 (`high: 5.5`) | Spironolactone label 5.1: "Monitor serum potassium within 1 week of initiation or titration". |
| thiazide_start_or_dose_change, loop_diuretic_start_or_dose_change | 7–14 | potassium drawn | ADA25-S10, Recommendation 10.12: "Monitor ... for hypokalemia when diuretics are used at routine visits, and 7–14 days after initiation or after a dose change." |
| lithium_start_or_dose_change | 7–7 | lithium drawn | NICE185 1.10.15: "Measure plasma lithium levels 1 week after starting lithium and 1 week after every dose change, and weekly until the levels are stable." |
| levothyroxine_dose_change | 42–56 | TSH drawn | Levothyroxine label 2.4: "monitor serum TSH levels after an interval of 6 to 8 weeks after any change in dosage." |

The potassium ceiling on the RAS and spironolactone contracts uses KDIGO24 Figure 32 ("potassium >5.5 mmol/l") and Figure 26 ("K+ >5.5 mmol/l ... Hold finerenone"; "This algorithm could be used for steroidal MRA."). `Check.high` breaches only above 5.5, which matches the strict ">" in both figures.

Reviewer note: KDIGO24 PP 3.6.2 gives 2 to 4 weeks for RAS inhibitors, and ADA25-S10 10.12 gives 7 to 14 days. The contracts use the KDIGO window because KDIGO also supplies the 30% creatinine threshold. Choose one window at sign-off.

## Omitted items

- **Thiazide and loop diuretic sodium and potassium thresholds** [UNVERIFIED — omitted]. The hydrochlorothiazide and furosemide labels name hyponatremia and hypokalemia but give no numeric cut points. ADA25-S10 10.12 gives no number either. We could not open the European hyponatraemia guideline (Spasovski 2014, doi:10.1530/EJE-13-1020), which returned a bot challenge. The `ref:<analyte>_below_lln` predicate (reporting laboratory's own range) is now available if sign-off wants a rule on the laboratory flag.
- **Recency interval for potassium and creatinine on a stable ACE inhibitor, ARB, or diuretic** [UNVERIFIED — omitted]. ADA25-S10 10.12 says "at routine visits", and the labels say "periodically". The 365-day lab-predicate window in `refill.yaml` is lane policy and has no source.
- **Valproate liver test recency** [UNVERIFIED — omitted]. The label says "perform serum liver testing prior to therapy and at frequent intervals thereafter" and gives no interval.
- **Lithium eGFR threshold** [UNVERIFIED — omitted]. The label requires kidney function assessment but gives no cut point.
- **Sulfonylurea eGFR threshold** [UNVERIFIED — omitted]. The glipizide and glyburide labels and ADA 2025 Section 9 are qualitative.
- **NSAID eGFR threshold for adults under 65** [UNVERIFIED — omitted]. The labels say "advanced renal disease" without a number. Beers Table 6 (CrCl < 30) applies only to adults aged 65 or older.
- **ADA/APA 2004 antipsychotic consensus statement** (Diabetes Care 2004;27:596) [UNVERIFIED — omitted]. The server returned HTTP 403. We did not read the primary text of the APA 2020 schizophrenia guideline; the lipid and HbA1c rules cite it through APA-PIP.
- **NSAIDs at 20 weeks of gestation or later.** The rule needs a gestational-age predicate, which the convention does not have.
- **Carbamazepine HLA-B\*1502.** The label requires screening before initiation, so it is not a refill rule.
- **Beta-blocker or non-DHP CCB heart-rate threshold** [UNVERIFIED — omitted]. The labels say "severe bradycardia" or "sinus bradycardia" without a number.
- **Amiodarone TSH and liver test recency** [UNVERIFIED — omitted]. The label says "Obtain baseline and periodic liver transaminases" and "Monitor thyroid function prior to treatment and periodically thereafter" without an interval. The HRS practical guide (Goldschlager 2007, doi:10.1016/j.hrthm.2007.07.020) returned HTTP 403, and the 2023 ACC/AHA/ACCP/HRS atrial fibrillation guideline could not be opened (publisher bot challenge).
- **Digoxin level recency and potassium floor** [UNVERIFIED — omitted]. The label gives no monitoring interval. The potassium range "between 4.0 and 5.5" appears only in the overdose section, so we did not use it as a refill rule.
- **Hydralazine CBC and ANA recency** [UNVERIFIED — omitted]. The label asks for these "periodically" without an interval.
- **Allopurinol renal dosing** (omitted, not a refill rule). The label renal guidance is for the starting dose and titration to a uric acid goal.
- **Lamotrigine renal threshold** [UNVERIFIED — omitted]. The label says "reduced maintenance doses may be effective for patients with significant renal impairment" without a number.
- **Pregabalin renal rule** (not needed). Pregabalin is Schedule V, so every pregabalin refill leaves the lane through `controlled_substance_out_of_lane`.
- **Pioglitazone ALT threshold** (omitted). The label's "ALT greater than 3 times the upper limit" applies only after a patient reports liver symptoms, which needs a symptom-plus-lab rule we did not draft.
- **Inhaled corticosteroid (single agent), DHP CCB (amlodipine), linagliptin, escitalopram renal, and SNRI renal other than duloxetine.** We read these labels and found no refill-time contraindication or numeric threshold beyond allergy, so the gate has no rule for them.
- **Mirtazapine, trazodone, montelukast lab monitoring.** The labels give no monitoring interval.

## Schema limitations

The current `gate.py` and `monitoring.py` resolve four limitations listed in the first draft: `lab_bounds` now has `ge` and `le`; `FindingKind.OUT_OF_LANE` routes to the ordering clinician; `LabRecencyRule.loinc` accepts a list; and `Check` has `max_abs_fall`, `low`, and `high`. The rules now use all four. The remaining limitations are:

1. **GateRule has no field for the lab freshness window.** The `max_age_days` value that `lab_bounds` needs is in a comment block in `refill.yaml`. The predicate builder must read it from there, and nothing enforces it.
2. **The rules have no negation.** "Unless the patient can take a gastroprotective agent" (Beers NSAID), "unless the indication is heart failure or CKD" (SGLT2), "without concomitant use of an ICS" (salmeterol), and the Beers PPI exceptions cannot be expressed. These rules fire, and the pharmacist resolves each one with a coded override.
3. **`LabRecencyRule` has no condition.** For example, NICE asks for lithium levels every 3 months in the first year and for older adults. The rule cannot vary by age or by time on therapy.
4. **The closed world now covers more prefixes.** The builder must set every `rx_class` that was not requested to FALSE, and must also set `controlled_substance`. For `dx:`, `hx:`, `sx:`, `med:`, `indication:`, `therapy:`, `adherence:`, and `allergy_class:` predicates, the builder sets FALSE only when the record is reconciled; otherwise each unknown predicate holds its rule and becomes a question. A refill of a common drug (for example an SSRI in an adult aged 65 or older) can generate several questions.
5. **CrCl has no LOINC code, and two labels use a different unit.** The builder must compute Cockcroft-Gault from creatinine and actual body weight. The Xarelto label says: "Calculate CrCl based on actual weight". The Tenormin and Keppra tables give CrCl in mL/min/1.73 m2, so `atenolol_crcl_le_35` and `levetiracetam_crcl_le_80` need a BSA-normalized value.
6. **Monitoring contracts start at initiation or a dose change.** A pure refill does not start one.
7. **Predicates that are not `lab_bounds`.** `ref:<analyte>_below_lln` and `ref:alt_gt_3x_uln` need the reporting laboratory's reference interval on each result. `dose:` predicates need the structured daily dose. Nothing in `gate.py` builds these; the predicate builder must.
8. **`Check.high` and `Check.low` compare the latest value only.** A contract cannot require two consecutive values above 5.5 before it breaches.
