# Evidence Evaluation Report

**Paper:** Rosuvastatin to Prevent Vascular Events in Men and Women with Elevated C-Reactive Protein
**Authors:** Ridker PM, Danielson E, Fonseca FAH, Genest J, Gotto AM Jr, Kastelein JJP, et al.
**Journal:** New England Journal of Medicine · **Year:** 2008 · **PMID:** 18997196
**Study type:** preventive · **Routing confidence:** 99%
**Generated:** 2026-03-21 · **Pipeline:** SciSpark Evidence Evaluator

---

## Section 1 — Study Design & Population

| Field | Value |
|---|---|
| Study type | preventive |
| Phase | III |
| N (intervention) | 8,901 |
| N (control) | 8,901 |
| Blinding | double_blind |
| Randomization | randomized |
| Multicenter | yes |

**PICO**

| Element | Value |
|---|---|
| Population | Apparently healthy men (>=50 y) and women (>=60 y) with LDL cholesterol <130 mg/dL and hsCRP >=2.0 mg/L |
| Intervention | Rosuvastatin 20 mg daily |
| Comparator | Matching placebo |
| Outcome | First major cardiovascular event (composite: MI, stroke, arterial revascularization, hospitalization for unstable angina, cardiovascular death) |

---

## Section 2 — Statistical Robustness

| Metric | Value | Threshold | Flag |
|---|---|---|---|
| Fragility Index (FI) | 67 | > 10 = robust | 🟢 robust |
| Fragility Quotient (FQ) | 0.0038 | < 0.01 | 🔴 below threshold |
| Post-hoc Power | 99.4% | >= 80% | 🟢 adequate |
| LTFU count | 25 | Must be <= FI (67) | 🟢 safe |
| NNT | 81.7 | Domain threshold: 200 | 🟢 favorable |

**Stage 3 computation trace:**

```
Fragility Index (FI):
  Inputs: events_i=142, events_c=251, n_i=8901, n_c=8901, initial_p<0.00001
  67 iterations required to cross P >= 0.05 (final: events_i=209, Fisher P=0.0527)
  FI = 67 → ROBUST (FI > 10)
  Delta: +0.5 grade
  Reasoning: Result is robust to multiple outcome changes.

LTFU-FI Attrition Rule:
  LTFU (25) <= FI (67): attrition does not threaten significance.
  Delta: 0

Fragility Quotient (FQ):
  FQ = 67 / 17,802 = 0.0038 (< 0.01)
  Delta: -0.5 grade
  Reasoning: Low FI relative to sample size — in a trial of 17,802, even FI=67 represents
  a small proportion of the total sample.

NNT:
  CER = 251/8901 = 0.0282
  IER = 142/8901 = 0.0160
  ARR = 0.0282 - 0.0160 = 0.0122
  NNT = 1/0.0122 = 81.7 (benefit)
  Domain threshold (CV primary prevention, low-risk): 200
  NNT (81.7) <= threshold (200): acceptable
  Delta: 0

Post-hoc Power:
  MCID = 0.01 (ARR); p_control = 0.0282; p_intervention_at_mcid = 0.0182
  Cohen's h = 0.0668
  Power = 99.37% (>= 80%): adequately powered at MCID
  Delta: 0
```

---

## Section 3 — Clinical Benchmarking

| Field | Value |
|---|---|
| MCID | 0.01 ARR |
| Source | AHA/ESC cardiovascular prevention guidelines — NNT threshold tables |
| Source tier | Tier 3 |
| Observed effect | ARR = 0.0122 (HR 0.56, 95% CI 0.46–0.69) |
| Effect vs. MCID | 🟢 exceeds |

**MCID rationale:** For cardiovascular primary prevention in low-risk populations, the AHA/ACC/ESC guidelines establish acceptable NNT ranges of 50–200, corresponding to an ARR of 0.5–2.0%. An ARR of 1.0% (NNT = 100) was used as the MCID benchmark. The observed ARR of 1.22% exceeds this threshold, and the NNT of 81.7 falls within the acceptable range.

---

## Section 4 — Bias Risk Assessment

**Tool:** RoB 2.0
**Overall concern:** 🟡 some_concerns

### Per-Domain Findings

| Domain | Judgment | Delta | Evidence |
|---|---|---|---|
| Randomization process | low | 0 | Computer-generated randomization with concealed allocation via interactive voice-response system. 1:1 ratio, stratified by center. |
| Deviations from intervention | low | 0 | Double-blind with matched placebo. Protocol adherence monitored centrally. Low crossover rate. |
| Missing outcome data | low | 0 | Vital status known for >97% of participants at trial termination. Primary endpoint ascertainment near-complete through national registry linkage. Estimated 25 patients with truly unknown primary endpoint status. |
| Measurement of outcome | low | 0 | Hard clinical endpoints (MI, stroke, cardiovascular death, revascularization) adjudicated by a blinded independent endpoint committee. Objective outcomes not susceptible to assessor bias. |
| Selection of reported results | some_concerns | 0 | Trial stopped early by independent DSMB after median 1.9 years of planned 5 years, based on exceeding pre-specified stopping boundary (Haybittle-Peto threshold). Early stopping may overestimate treatment effects. Primary endpoint was pre-specified and registered (NCT00239681). Classified as "some_concerns" rather than "high" because stopping followed a pre-specified rule and the primary endpoint was not changed. |

**Additional checks**

| Check | Finding | Delta |
|---|---|---|
| Surrogate endpoint | no — composite of hard clinical events | 0 |
| Meta-analysis I² | n/a | 0 |

---

## Narrative Summary

The JUPITER trial (Justification for the Use of Statins in Prevention: an Intervention Trial Evaluating Rosuvastatin) was a large, multinational, double-blind, randomized, placebo-controlled Phase III trial enrolling 17,802 apparently healthy men and women with low LDL cholesterol but elevated high-sensitivity C-reactive protein. Participants were randomized 1:1 to rosuvastatin 20 mg daily or placebo, with the primary endpoint being a composite of first major cardiovascular event.

The statistical robustness of this trial is notable. The Fragility Index of 67 indicates that 67 outcome events would need to change classification before the primary result would lose significance — a highly robust finding that places JUPITER among the most statistically resilient cardiovascular prevention trials. The LTFU-FI attrition check confirms safety: only approximately 25 patients had unknown primary endpoint status, well below the FI of 67. Post-hoc power exceeded 99% at the pre-specified MCID, confirming the trial was substantially overpowered for the clinically meaningful effect size. However, the Fragility Quotient (0.0038) falls below the 0.01 threshold, reflecting that even an FI of 67 represents a small fraction of the 17,802-patient sample.

From a clinical benchmarking perspective, the observed absolute risk reduction of 1.22% (HR 0.56, 95% CI 0.46–0.69, P < 0.00001) exceeds the MCID benchmark of 1.0% ARR derived from AHA/ESC guideline NNT thresholds for cardiovascular primary prevention. The NNT of 81.7 falls well within the acceptable 50–200 range for low-risk primary prevention populations, suggesting clinically meaningful benefit at a population level.

The bias risk assessment using RoB 2.0 identified low risk across four of five domains. The single domain rated "some concerns" is selection of reported results, driven by the trial's early termination. The independent DSMB stopped JUPITER after a median follow-up of only 1.9 years out of a planned 5 years. While the stopping followed a pre-specified Haybittle-Peto boundary and the primary endpoint was registered, early stopping is known to overestimate treatment effects — a widely discussed limitation in the subsequent literature. The magnitude of this potential overestimation is uncertain but should be weighed when interpreting the hazard ratio of 0.56.

Key strengths of the trial include its large sample size, rigorous double-blind design, use of hard clinical endpoints adjudicated by an independent blinded committee, near-complete follow-up, and highly significant results with a very low P-value. Key limitations include early stopping (with potential effect overestimation), the highly selected population (elevated CRP as an enrollment criterion limits generalizability), and the relatively short follow-up that leaves long-term benefit-risk balance uncertain. The trial also identified a higher incidence of physician-reported diabetes in the rosuvastatin group, a finding that requires consideration in benefit-risk discussions.

Clinicians interpreting this evidence should weigh the strong statistical robustness and favorable NNT against the uncertainty introduced by early stopping and the selected population. The results provide robust evidence for the efficacy of rosuvastatin in reducing cardiovascular events in this specific population, while the generalizability to broader primary prevention populations and the long-term safety profile merit ongoing evaluation.

---

## Suggested Score *(optional — heuristic)*

> This score is generated by a deterministic rule engine. Design choices are pending expert calibration. Do not use as a validated clinical instrument.

**Score: 5 ★★★★★ — Excellent**

### Score Path

| Step | Detail | Delta |
|---|---|---|
| Initial grade | Large multi-center double-blind Phase III RCT (N > 1,000) | 5 (base) |
| Stage 2 | Effect exceeds MCID; N > domain standard; NNT within threshold | 0 |
| Stage 3 | FI: +0.5 (robust); FQ: -0.5 (below threshold); net zero | 0 |
| Stage 4 | All RoB 2.0 domains low or some_concerns (no deduction-level findings) | 0 |
| De-duplication | No overlapping deductions to resolve | — |
| Boundary enforcement | None required (raw score = 5, within [3, 5] range) | — |
| **Final score** | | **5** |

**Score 5 prerequisites check:**
- Initial grade = 5: yes
- FI > 10: yes (67)
- FI > LTFU: yes (67 > 25)
- P < 0.001: yes (P < 0.00001)
- Power >= 0.80: yes (99.4%)
- Low bias (no high/critical domains): yes
- Hard endpoints (not surrogate): yes

---

*Generated by SciSpark Evidence Evaluator · [scispark.ai](https://scispark.ai) · team@scispark.ai*
