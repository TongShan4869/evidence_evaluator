# Pilot Paper Selection for Evidence Evaluator Validation

Five well-known clinical/biomedical papers selected for pilot evaluation, one per study type.
Each primary candidate has a fallback alternative.

## Selection Criteria

- Publicly available abstracts
- Published appraisal data available for external validation where possible
- Highly cited / well-known in their domain
- Coverage of all 5 study types supported by the Evidence Evaluator pipeline

---

## Primary Candidates

| # | Study Type | Title | Authors | Year | Journal | PMID | Why Selected |
|---|-----------|-------|---------|------|---------|------|-------------|
| 1 | **RCT (intervention)** | Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction (DAPA-HF) | McMurray JJV et al. | 2019 | N Engl J Med | [31535829](https://pubmed.ncbi.nlm.nih.gov/31535829/) | Large Phase III RCT (N=4744), clear primary endpoint (HR 0.74), published Fragility Index analyses available, well-suited for full Stage 2-3 math audit |
| 2 | **Diagnostic** | Accuracy of Fecal Immunochemical Tests for Colorectal Cancer: Systematic Review and Meta-analysis | Lee JK et al. | 2014 | Ann Intern Med | [24658694](https://pubmed.ncbi.nlm.nih.gov/24658694/) | Pooled diagnostic accuracy (sensitivity 0.79, specificity 0.94, DOR ~55), 19 studies, ideal for QUADAS-2 framework and DOR computation in Stage 3 |
| 3 | **Preventive** | Rosuvastatin to Prevent Vascular Events in Men and Women with Elevated C-Reactive Protein (JUPITER) | Ridker PM et al. | 2008 | N Engl J Med | [18997196](https://pubmed.ncbi.nlm.nih.gov/18997196/) | Large preventive trial (N=17,802), published NNT (95 at 2 yr, 31 at 4 yr), HR 0.56, stopped early -- exercises the NNT and early-stopping penalty logic in Stage 3/5 |
| 4 | **Observational** | Smoking and Carcinoma of the Lung: Preliminary Report | Doll R, Hill AB | 1950 | Br Med J | [14772469](https://pubmed.ncbi.nlm.nih.gov/14772469/) | Landmark case-control study (649 cases, 649 controls), very large effect size (OR >>2.0), foundational epidemiological study with extensive published reappraisals, tests observational pathway |
| 5 | **Phase 0/I** | Safety, Activity, and Immune Correlates of Anti-PD-1 Antibody in Cancer | Topalian SL et al. | 2012 | N Engl J Med | [22658127](https://pubmed.ncbi.nlm.nih.gov/22658127/) | First-in-human Phase I dose-escalation of nivolumab (N=296), multiple tumor types, no MTD reached, 14% grade 3-4 AEs -- tests the phase_0_1 routing (Stages 2+3 skipped, score locked 1-2) |

---

## Fallback Candidates

| # | Study Type | Title | Authors | Year | Journal | PMID | Why Selected as Fallback |
|---|-----------|-------|---------|------|---------|------|------------------------|
| 1 | **RCT (intervention)** | Angiotensin-Neprilysin Inhibition versus Enalapril in Heart Failure (PARADIGM-HF) | McMurray JJV et al. | 2014 | N Engl J Med | [25176015](https://pubmed.ncbi.nlm.nih.gov/25176015/) | Large RCT (N=8442), HR 0.80, stopped early, similar domain to DAPA-HF, well-characterized Fragility Index |
| 2 | **Diagnostic** | Early Diagnosis of Myocardial Infarction with Sensitive Cardiac Troponin Assays | Reichlin T et al. | 2009 | N Engl J Med | [19710484](https://pubmed.ncbi.nlm.nih.gov/19710484/) | Diagnostic accuracy study (N=718), AUC 0.95-0.96 for hs-troponin, clear 2x2 data extractable, published in high-impact journal |
| 3 | **Preventive** | Prevention of Coronary Heart Disease with Pravastatin in Men with Hypercholesterolemia (WOSCOPS) | Shepherd J et al. | 1995 | N Engl J Med | [7566020](https://pubmed.ncbi.nlm.nih.gov/7566020/) | Large primary prevention trial (N=6595), NNT 33 at 5 yr, 31% RRR, 20-yr follow-up data available for legacy effect validation |
| 4 | **Observational** | Red Meat Consumption and Mortality: Results from 2 Prospective Cohort Studies | Pan A et al. | 2012 | Arch Intern Med | [22412075](https://pubmed.ncbi.nlm.nih.gov/22412075/) | Large prospective cohort (N=121,342; Nurses' Health Study + HPFS), HR 1.13-1.20 per serving/day, 2.96M person-years, tests observational pathway with moderate effect size |
| 5 | **Phase 0/I** | Safety and Tumor Responses with Lambrolizumab (Anti-PD-1) in Melanoma (KEYNOTE-001) | Hamid O et al. | 2013 | N Engl J Med | [23724846](https://pubmed.ncbi.nlm.nih.gov/23724846/) | Phase I dose-escalation of pembrolizumab (N=135), 38% ORR in melanoma, no MTD, complements Topalian study as second checkpoint inhibitor Phase I |

---

## Notes

- **External validation anchors**: DAPA-HF and JUPITER have published Fragility Index values; WOSCOPS has a well-established NNT; Lee 2014 FIT meta-analysis reports pooled DOR; Doll & Hill 1950 has extensive published reappraisals.
- **Pipeline coverage**: The 5 primary papers exercise all study-type routing paths in the Evidence Evaluator pipeline, including the phase_0_1 lock (score 1-2), diagnostic DOR/QUADAS-2 pathway, preventive NNT logic, observational RR pathway, and full RCT math audit.
- **Results directory**: `paper/pilot_results/` created for storing pipeline output from each evaluation run.
