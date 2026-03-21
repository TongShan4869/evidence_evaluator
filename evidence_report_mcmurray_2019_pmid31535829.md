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
| Population | Patients with NYHA class II–IV heart failure and LVEF ≤ 40% |
| Intervention | Dapagliflozin 10 mg once daily + standard therapy |
| Comparator | Placebo + standard therapy |
| Outcome | Composite of worsening HF (hospitalization or urgent IV therapy) or cardiovascular death |

---

## Section 2 — Statistical Robustness

| Metric | Value | Threshold | Flag |
|---|---|---|---|
| Fragility Index (FI) | 62 | ≤ 2 = extreme fragile; > 10 = robust | 🟢 robust |
| Fragility Quotient (FQ) | 0.0131 | < 0.01 | 🟢 above threshold |
| Post-hoc Power | 99.1% | ≥ 80% | 🟢 adequate |
| LTFU count | 21 | Must be ≤ FI (62) | 🟢 safe |
| NNT | 20.4 | Domain threshold: 50 | 🟢 favorable |

### Fragility Index Computation Trace

```
Inputs: events_i=386, events_c=502, n_i=2373, n_c=2371, initial_p<0.001
Iteration 1:  events_i=387 → Fisher P=0.000019
Iteration 10: events_i=396 → Fisher P=0.000085
Iteration 20: events_i=406 → Fisher P=0.000393
Iteration 30: events_i=416 → Fisher P=0.001569
Iteration 40: events_i=426 → Fisher P=0.005401
Iteration 50: events_i=436 → Fisher P=0.016128
Iteration 60: events_i=446 → Fisher P=0.042038
Iteration 62: events_i=448 → Fisher P=0.050119 ✓ (crossed 0.05)
FI = 62 → ROBUST (FI > 10)
Delta: +0.5 grade
```

### NNT Computation Trace

```
CER = 502/2371 = 0.2117
IER = 386/2373 = 0.1627
ARR = 0.2117 − 0.1627 = 0.0491
NNT = 1/0.0491 = 20.4 (benefit)
Domain threshold: 50 (cardiovascular secondary prevention)
NNT (20.4) ≤ threshold (50): favorable
Delta: 0
```

### LTFU-FI Attrition Rule

```
LTFU = 21, FI = 62
LTFU (21) ≤ FI (62): attrition does not threaten significance.
Hard rule NOT triggered.
Delta: 0
```

---

## Section 3 — Clinical Benchmarking

| Field | Value |
|---|---|
| MCID | ~4.9% ARR for HF composite |
| Source | AHA/ESC Heart Failure Guidelines |
| Source tier | Tier 3 |
| Observed effect | HR 0.74 (95% CI: 0.65–0.85; P < 0.001); ARR 4.9% |
| Effect vs. MCID | 🟢 meets threshold |

### Primary and Secondary Outcomes

| Endpoint | Dapagliflozin | Placebo | HR (95% CI) |
|---|---|---|---|
| **Primary composite** (worsening HF or CV death) | 386/2,373 (16.3%) | 502/2,371 (21.2%) | **0.74** (0.65–0.85); P < 0.001 |
| Worsening HF event | 237/2,373 (10.0%) | 326/2,371 (13.7%) | **0.70** (0.59–0.83) |
| Cardiovascular death | 227/2,373 (9.6%) | 273/2,371 (11.5%) | **0.82** (0.69–0.98) |
| All-cause mortality | 276/2,373 (11.6%) | 329/2,371 (13.9%) | **0.83** (0.71–0.97) |

---

## Section 4 — Bias Risk Assessment

**Tool:** RoB 2.0
**Overall concern:** 🟢 low

### Per-Domain Findings

| Domain | Judgment | Delta | Evidence |
|---|---|---|---|
| Randomization process | 🟢 low | 0 | Computer-generated randomization with stratification by diabetes status; concealed allocation via IVRS |
| Deviations from intervention | 🟢 low | 0 | Double-blind placebo-controlled; adherence > 90% in both arms |
| Missing outcome data | 🟢 low | 0 | Vital status obtained for > 99.7% of patients; minimal LTFU |
| Measurement of outcome | 🟢 low | 0 | Hard clinical endpoints (death, hospitalization); blinded adjudication committee |
| Selection of reported results | 🟢 low | 0 | Pre-registered on ClinicalTrials.gov; primary endpoint matches registration |

**Additional checks**

| Check | Finding | Delta |
|---|---|---|
| Surrogate endpoint | No — hard clinical endpoints used | 0 |
| Meta-analysis I² | n/a | 0 |

---

## Narrative Summary

The DAPA-HF trial is a large, international, Phase III, double-blind, placebo-controlled randomized trial evaluating dapagliflozin 10 mg daily in 4,744 patients with heart failure and reduced ejection fraction (LVEF ≤ 40%), irrespective of diabetes status. The study was published in the New England Journal of Medicine in 2019 and represents a landmark trial in the SGLT2 inhibitor class for heart failure.

From a statistical robustness standpoint, the findings are exceptionally strong. The Fragility Index of 62 places this trial among the most robust cardiovascular outcomes trials — it would take 62 additional primary events in the treatment arm to nullify statistical significance. The post-hoc power exceeds 99%, confirming the trial was more than adequately powered. The number needed to treat (NNT) of approximately 20 patients over 18.2 months is clinically actionable and well within accepted thresholds for cardiovascular secondary prevention (domain threshold: 50). Lost to follow-up was minimal (~21 patients, with vital status obtained for > 99.7%), placing LTFU well below the Fragility Index and posing no attrition concern.

Clinically, the observed absolute risk reduction of 4.9% for the primary composite endpoint (worsening heart failure or cardiovascular death) meets the minimum clinically important difference threshold for heart failure trials. The hazard ratio of 0.74 (95% CI: 0.65–0.85; P < 0.001) demonstrates a 26% relative risk reduction, with consistent benefit across secondary endpoints including cardiovascular death (HR 0.82), worsening heart failure events (HR 0.70), and all-cause mortality (HR 0.83).

The bias risk assessment using RoB 2.0 identifies low risk across all five domains. Randomization was computer-generated with stratification and concealed allocation. The double-blind design with placebo control minimizes performance bias. Hard clinical endpoints (death and hospitalization) adjudicated by a blinded committee eliminate measurement bias concerns. The pre-registered protocol matches published endpoints.

Notable strengths include the large sample size, international multi-center design, hard clinical endpoints, and the inclusion of patients with and without diabetes — extending the evidence base beyond the diabetic population. The primary limitation from a Tier 1 assessment perspective is the industry sponsorship by AstraZeneca, though this does not trigger a formal deduction in the framework. The median follow-up of 18.2 months may limit assessment of very long-term outcomes.

---

## Suggested Score *(heuristic)*

> This score is generated by a deterministic rule engine. Design choices are pending expert calibration (Appendix B, SciSpark EvidenceScore PRD v2). Do not use as a validated clinical instrument.

**Score: 5 ★★★★★ — Excellent**

### Score Path

| Step | Detail | Delta |
|---|---|---|
| Initial grade | Large multi-center double-blind RCT (Phase III, N > 1000) | 5 |
| Stage 2 | No deductions (effect meets MCID, N exceeds domain standard, NNT within threshold) | 0 |
| Stage 3 | FI = 62 (robust +0.5); LTFU safe; FQ acceptable; power adequate; NNT favorable | +0.5 |
| Stage 4 | All RoB 2.0 domains low risk; no surrogate endpoint | 0 |
| De-duplication | No deductions to de-duplicate | — |
| Boundary enforcement | Ceiling at 5 applied (raw 5.5) | −0.5 |
| **Final score** | | **5** |

---

*Generated by SciSpark EvidenceScore v2 · [scispark.ai](https://scispark.ai) · team@scispark.ai*
