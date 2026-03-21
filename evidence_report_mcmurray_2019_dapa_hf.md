# Evidence Evaluation Report

**Paper:** Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction
**Journal:** New England Journal of Medicine · **Year:** 2019 · **DOI:** 10.1056/NEJMoa1911303
**Study type:** RCT_intervention · **Routing confidence:** 99%
**Generated:** 2026-03-20 · **Pipeline:** SciSpark EvidenceScore v2

---

## Section 1 — Study Design & Population

| Field | Value |
|---|---|
| Study type | RCT_intervention |
| Phase | III |
| N (intervention) | 2,373 |
| N (control) | 2,371 |
| Blinding | double_blind |
| Randomization | randomized |
| Multicenter | yes |

**PICO**

| Element | Value |
|---|---|
| Population | Adults with NYHA class II–IV heart failure and ejection fraction ≤40%, with or without type 2 diabetes |
| Intervention | Dapagliflozin 10 mg once daily |
| Comparator | Matching placebo |
| Outcome | Composite of worsening heart failure (hospitalization or urgent visit requiring IV therapy) or cardiovascular death; median follow-up 18.2 months |

---

## Section 2 — Statistical Robustness

| Metric | Value | Threshold | Flag |
|---|---|---|---|
| Fragility Index (FI) | 62 | ≤ 2 = extreme fragile; > 10 = robust | 🟢 robust |
| Fragility Quotient (FQ) | 0.0131 | < 0.01 | 🟢 above threshold |
| Post-hoc Power | 95.8% | ≥ 80% | 🟢 adequate |
| LTFU count | 14 | Must be ≤ FI (62) | 🟢 safe |
| NNT | 20.4 | Domain threshold: 50 | 🟢 favorable |

---

## Section 3 — Clinical Benchmarking

| Field | Value |
|---|---|
| MCID | 0.042 ARR (corresponding to HR 0.80) |
| Source | ESC/AHA Heart Failure Trial Design Guidelines |
| Source tier | Tier 3 |
| Observed effect | HR 0.74 (95% CI 0.65–0.85); ARR 4.9% |
| Effect vs. MCID | 🟢 exceeds |

---

## Section 4 — Bias Risk Assessment

**Tool:** RoB 2.0
**Overall concern:** 🟢 low

### Per-Domain Findings

| Domain | Judgment | Delta | Evidence |
|---|---|---|---|
| Randomization process | low | 0 | Computer-generated randomization with stratification by diabetes status; allocation concealment via IWRS |
| Deviations from intervention | low | 0 | Double-blind, matched placebo. Discontinuation balanced (dapa 10.9% vs placebo 12.5%) |
| Missing outcome data | low | 0 | Vital status obtained for 99.7% of patients |
| Measurement of outcome | low | 0 | Hard clinical endpoints (hospitalization, death) with blinded independent adjudication committee |
| Selection of reported results | low | 0 | Pre-registered NCT03036124; primary endpoint matches registration; SAP published before unblinding |

**Additional checks**

| Check | Finding | Delta |
|---|---|---|
| Surrogate endpoint | no — composite of hospitalization/death are hard clinical endpoints | 0 |
| Meta-analysis I² | n/a | 0 |

---

## Narrative Summary

The DAPA-HF trial (McMurray et al., NEJM 2019) was a Phase III, multi-center, double-blind, placebo-controlled randomized trial evaluating dapagliflozin 10 mg daily versus placebo in 4,744 patients with heart failure and reduced ejection fraction (NYHA class II–IV, EF ≤40%), regardless of diabetes status. The trial was conducted across 410 sites in 20 countries, funded by AstraZeneca, and registered on ClinicalTrials.gov (NCT03036124).

The primary composite endpoint of worsening heart failure or cardiovascular death occurred in 386 of 2,373 patients (16.3%) in the dapagliflozin group versus 502 of 2,371 patients (21.2%) in the placebo group (HR 0.74; 95% CI 0.65–0.85; p < 0.001). This translates to an absolute risk reduction of 4.9% and a number needed to treat of approximately 20 patients over 18.2 months of follow-up. Both components of the composite favored dapagliflozin: worsening heart failure events occurred in 10.0% versus 13.7% (HR 0.70; 95% CI 0.59–0.83) and cardiovascular death in 9.6% versus 11.5% (HR 0.82; 95% CI 0.69–0.98). All-cause mortality was also lower with dapagliflozin (11.6% vs. 13.9%; HR 0.83; 95% CI 0.71–0.97).

Statistical robustness analysis reveals a Fragility Index of 62, meaning 62 outcome events in the intervention arm would need to be switched before the primary result lost statistical significance. This places the trial firmly in the "robust" category. The Fragility Quotient (FQ = 0.013) exceeds the 0.01 threshold, confirming that the result is not disproportionately fragile relative to sample size. Estimated lost-to-follow-up of approximately 14 patients (based on 99.7% vital status ascertainment) is well below the FI of 62, so the LTFU-FI attrition rule is not triggered. Post-hoc power at the MCID threshold is 95.8%, confirming the trial was well-powered to detect a clinically meaningful difference.

The NNT of 20.4 falls well within the favorable range for cardiovascular secondary prevention in high-risk populations (domain threshold: 10–50). The observed effect (ARR 4.9%, HR 0.74) exceeds the clinical significance benchmark (ARR 4.2%, HR 0.80) derived from ESC/AHA heart failure trial design guidelines, though this is a Tier 3 source — no Tier 1 or Tier 2 MCID specific to this composite endpoint was identified through COMET, OMERACT, or systematic review sources.

Bias risk assessment using the Cochrane RoB 2.0 framework found low risk across all five domains. Randomization was computer-generated with stratified allocation and concealment via interactive web/voice response system. The double-blind design with matched placebo tablets minimized performance and detection bias. Follow-up was near-complete (99.7%). The primary outcome comprised hard clinical endpoints (hospitalization and death) adjudicated by a blinded independent committee. The trial was pre-registered with a published statistical analysis plan, and the reported primary endpoint is consistent with the registration.

Notable strengths include the large sample size, multi-center international design, inclusion of patients both with and without diabetes (broadening generalizability), hard clinical endpoints, near-complete follow-up, and consistent treatment effects across pre-specified subgroups. The primary limitation relevant to evidence quality assessment is that the MCID benchmark derives from Tier 3 guideline sources rather than formal MCID determination studies specific to this composite endpoint. The trial was industry-funded (AstraZeneca), though the rigorous design and execution mitigate typical industry-bias concerns.

---

## Suggested Score *(heuristic)*

> This score is generated by a deterministic rule engine. Design choices are pending expert calibration (Appendix B, SciSpark EvidenceScore PRD v2). Do not use as a validated clinical instrument.

**Score: 5 ★★★★★ — Excellent**

### Score Path

| Step | Detail | Delta |
|---|---|---|
| Initial grade | Large multi-center double-blind RCT (Phase III, N > 1000) | 5 |
| Stage 2 | No deductions — effect exceeds MCID, N exceeds domain standard, NNT within threshold | 0 |
| Stage 3 | FI = 62 (robust, +0.5); LTFU safe; FQ acceptable; power adequate; NNT favorable | +0.5 |
| Stage 4 | All RoB 2.0 domains low; no surrogate endpoint | 0 |
| De-duplication | No deductions to de-duplicate | — |
| Boundary enforcement | Ceiling 5 applied (raw 5.5 capped) | −0.5 |
| **Final score** | | **5** |

---

*Generated by SciSpark EvidenceScore v2 · [scispark.ai](https://scispark.ai) · team@scispark.ai*
