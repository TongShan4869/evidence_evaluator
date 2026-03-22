# Evidence Evaluation Report

**Paper:** Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction
**Authors:** McMurray JJV, Solomon SD, Inzucchi SE, Kober L, Kosiborod MN, Martinez FA, Ponikowski P, Sabatine MS, et al.
**Journal:** New England Journal of Medicine · **Year:** 2019 · **DOI:** 10.1056/NEJMoa1911303
**PMID:** 31535829
**Study type:** RCT_intervention · **Routing confidence:** 99%
**Generated:** 2026-03-21 · **Pipeline:** SciSpark Evidence Evaluator

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
| Population | Adults with heart failure and reduced ejection fraction (LVEF ≤ 40%), NYHA class II–IV, with or without type 2 diabetes, on stable guideline-directed medical therapy |
| Intervention | Dapagliflozin 10 mg once daily |
| Comparator | Matching placebo |
| Outcome | Composite of worsening heart failure (hospitalization or urgent visit requiring IV therapy) or cardiovascular death, median follow-up 18.2 months |

---

## Section 2 — Statistical Robustness

| Metric | Value | Threshold | Flag |
|---|---|---|---|
| Fragility Index (FI) | 62 | ≤ 2 = extreme fragile; > 10 = robust | 🟢 robust |
| Fragility Quotient (FQ) | 0.0131 | < 0.01 | 🟢 above threshold |
| Post-hoc Power | 40.4% | ≥ 80% | 🔴 underpowered (at MCID = ARR 2%) |
| LTFU count | 10 | Must be ≤ FI | 🟢 safe (LTFU 10 ≤ FI 62) |
| NNT | 20.4 | Domain threshold: 50 (CV secondary prevention) | 🟢 favorable |

### Computation Traces

**Fragility Index (FI):**
```
Inputs: events_i=386, events_c=502, n_i=2373, n_c=2371, initial_p<0.001
Iteration 1:  events_i=387 → Fisher P=0.000019
Iteration 5:  events_i=391 → Fisher P=0.000037
Iteration 10: events_i=396 → Fisher P=0.000085
Iteration 20: events_i=406 → Fisher P=0.000393
Iteration 30: events_i=416 → Fisher P=0.001569
Iteration 40: events_i=426 → Fisher P=0.005401
Iteration 50: events_i=436 → Fisher P=0.016128
Iteration 55: events_i=441 → Fisher P=0.026475
Iteration 60: events_i=446 → Fisher P=0.042038
Iteration 62: events_i=448 → Fisher P=0.050119 ✓ (crossed 0.05)
FI = 62 → ROBUST (FI > 10)
Delta: +0.5 grade
Reasoning: 62 outcome event changes would be needed to render the result
non-significant. This is an exceptionally robust finding.
```

**NNT Computation:**
```
CER = 502 / 2371 = 0.2117 (21.2%)
IER = 386 / 2373 = 0.1627 (16.3%)
ARR = 0.2117 − 0.1627 = 0.0491 (4.9%)
NNT = 1 / 0.0491 = 20.4 (benefit)
Domain threshold (CV secondary prevention): 50
NNT 20.4 ≤ 50 → favorable
Delta: 0
```

**LTFU-FI Comparison:**
```
LTFU = 10 (vital status unknown at end of follow-up)
FI = 62
LTFU (10) ≤ FI (62) → safe
Hard attrition rule NOT triggered.
Delta: 0
```

**Post-hoc Power:**
```
Target effect: MCID = ARR 0.02 (2% absolute risk reduction)
Control event rate (CER): 0.2117
Intervention rate at MCID: CER − MCID = 0.2117 − 0.02 = 0.1917
Cohen's h = proportion_effectsize(0.1917, 0.2117) = 0.0499
Power = NormalIndPower().solve_power(h=0.0499, nobs1=2373, ratio=1.0, alpha=0.05)
Power = 40.4% (< 80%) → underpowered to detect MCID
Delta: −1 grade

Note: The observed ARR of 4.9% far exceeds the MCID of 2%. The low post-hoc
power reflects that the trial was not designed to detect an effect as small as
the MCID threshold — it was powered for a larger, clinically important effect
and achieved it convincingly (P < 0.001). This deduction reflects the
conservative nature of the scoring framework.
```

**Fragility Quotient (FQ):**
```
FQ = FI / N_total = 62 / 4744 = 0.0131
FQ 0.0131 ≥ 0.01 threshold → acceptable
Delta: 0
```

**De-duplication (Statistical Stability Dimension):**
```
Candidates: {power < 0.80}
Only one candidate active → no suppression needed.
Applied: power −1
```

---

## Section 3 — Clinical Benchmarking

| Field | Value |
|---|---|
| MCID | ARR 2.0% (0.02) |
| Source | AHA/ESC heart failure guidelines — consensus threshold for binary composite endpoints in HFrEF trials |
| Source tier | Tier 3 |
| Observed effect | ARR 4.9% (HR 0.74, 95% CI 0.65–0.85) |
| Effect vs. MCID | 🟢 exceeds (observed ARR 4.9% > MCID 2.0%) |

**Benchmarking rationale:** For the composite of worsening heart failure or cardiovascular death, no formal MCID has been registered with COMET or OMERACT (Tier 1 sources not available). The ARR threshold of 2% is derived from AHA/ACC/ESC clinical practice guidelines for heart failure, which consider absolute risk reductions of ≥2% for major cardiovascular events as clinically meaningful in the context of HFrEF treatment (Tier 3). This is consistent with thresholds used in prior landmark HF trials (PARADIGM-HF: ARR 4.7%; EMPEROR-Reduced: ARR 3.5%). The observed ARR of 4.9% substantially exceeds this benchmark.

**Domain N standard:** 4,000 patients. The DAPA-HF trial enrolled 4,744, exceeding the domain standard. No deduction for sample size.

**NNT vs. domain threshold:** NNT 20.4 is well within the acceptable range for cardiovascular secondary prevention (10–50). No deduction.

---

## Section 4 — Bias Risk Assessment

**Tool:** RoB 2.0
**Overall concern:** 🟢 low

### Per-Domain Findings

| Domain | Judgment | Delta | Evidence |
|---|---|---|---|
| Randomization process | 🟢 low | 0 | Computer-generated randomization with stratification by diabetes status. Allocation concealment via interactive web-based response system (IWRS). 1:1 randomization with balanced baseline characteristics across arms (Table 1). |
| Deviations from intended interventions | 🟢 low | 0 | Double-blind, placebo-controlled design. Drug and placebo were identical in appearance. Intention-to-treat analysis. No significant crossover or co-intervention imbalances reported. Protocol adherence was monitored. |
| Missing outcome data | 🟢 low | 0 | Vital status was known for 99.7% of patients at end of trial. Primary endpoint data were available for the full ITT population. Minimal missing data with no differential missingness between arms. |
| Measurement of the outcome | 🟢 low | 0 | Primary endpoint components are hard clinical endpoints (hospitalization, urgent IV therapy visit, cardiovascular death) — objective and adjudicated by an independent blinded clinical events committee. Not susceptible to observer bias. |
| Selection of the reported result | 🟢 low | 0 | Trial was pre-registered (ClinicalTrials.gov NCT03036124). Primary composite endpoint matched registration. Statistical analysis plan was finalized before database lock. Pre-specified subgroup analyses. No evidence of selective reporting — all pre-specified endpoints reported. |

**Additional checks**

| Check | Finding | Delta |
|---|---|---|
| Surrogate endpoint | 🟢 no — primary outcome is a hard clinical composite (HF hospitalization/urgent visit + CV death) | 0 |
| Meta-analysis I² | n/a (single trial) | 0 |

---

## Narrative Summary

The DAPA-HF trial was a large, multicenter, randomized, double-blind, placebo-controlled Phase III trial that enrolled 4,744 patients with heart failure and reduced ejection fraction (LVEF ≤ 40%) across 410 sites in 20 countries. Patients were randomized to receive dapagliflozin 10 mg daily or placebo on top of standard guideline-directed medical therapy, regardless of diabetes status. The trial was sponsored by AstraZeneca and conducted between February 2017 and June 2019 with a median follow-up of 18.2 months.

The statistical robustness of the primary finding is exceptional. The Fragility Index of 62 indicates that 62 individual outcome events in the dapagliflozin arm would need to be reversed before the primary result would lose statistical significance — this places DAPA-HF among the most statistically robust cardiovascular trials in the literature. The Fragility Quotient of 0.0131 is above the 0.01 threshold, confirming that the high FI is not merely an artifact of the large sample size. The LTFU-to-FI comparison is strongly favorable: only approximately 10 patients had unknown vital status, far below the FI of 62, meaning that even if every single missing patient had an adverse outcome in the dapagliflozin arm, the finding would remain significant.

The post-hoc power calculation warrants contextual interpretation. When assessed against a conservative MCID of ARR 2%, the study achieves only 40.4% power — a technical flag in the scoring framework. However, the observed absolute risk reduction of 4.9% is 2.5 times the MCID, and the P-value was far below 0.001. The trial was prospectively powered to detect an HR of approximately 0.80 at 90% power and achieved an HR of 0.74. The low post-hoc power at the MCID reflects the mathematical reality that detecting a very small effect (2% ARR) would require substantially more patients, not a deficiency in the trial's design.

The NNT of 20.4 over median 18.2 months of follow-up is clinically favorable. In the context of cardiovascular secondary prevention, where NNT thresholds of 10–50 are considered acceptable, this represents a meaningful treatment effect. For every 21 patients with HFrEF treated with dapagliflozin for approximately 18 months, one additional patient would avoid a worsening heart failure event or cardiovascular death compared to placebo.

Bias risk assessment using the RoB 2.0 framework finds low concern across all five domains. Randomization was computer-generated with concealed allocation. The double-blind design with identical drug and placebo appearance minimized performance and detection bias. Outcome adjudication was performed by an independent blinded committee evaluating hard clinical endpoints. Missing data were minimal, with vital status known for 99.7% of participants. The trial was pre-registered with a clearly defined primary endpoint that matched the published analysis.

Key strengths of the trial include its large multinational design, the use of hard clinical endpoints, minimal loss to follow-up, and the inclusion of patients with and without type 2 diabetes — broadening the generalizability of the findings. A limitation relevant to interpretation is that the composite endpoint combines events of different clinical severity (urgent IV visit vs. cardiovascular death), though both components individually showed benefit (HR 0.70 for worsening HF; HR 0.82 for CV death).

Clinicians interpreting these findings should consider that the evidence is supported by strong statistical robustness, clinically meaningful effect sizes that substantially exceed consensus MCID thresholds, low bias risk, and results that are internally consistent across primary and secondary endpoints. The post-hoc power flag is a technical artifact of the conservative MCID benchmark rather than a meaningful limitation of this particular trial.

---

## Suggested Score *(optional — heuristic)*

> This score is generated by a deterministic rule engine. Design choices are pending expert calibration. Do not use as a validated clinical instrument.

**Score: 4 ★★★★☆ — Good**

### Score Path

| Step | Detail | Delta |
|---|---|---|
| Initial grade | Grade 5 — Large multicenter double-blind RCT, Phase III, N > 1000 | 5 (base) |
| Stage 2 | Effect exceeds MCID; N exceeds domain standard; NNT within threshold — no deductions | 0 |
| Stage 3 | FI robust (+0.5); Post-hoc power 40.4% at MCID (−1) | −0.5 |
| Stage 4 | RoB 2.0 all domains low; no surrogate; no heterogeneity — no deductions | 0 |
| De-duplication | Power is sole statistical stability deduction — no suppression needed | — |
| Boundary enforcement | Raw score 4.5 → rounds to 4; within Grade 5 bounds (floor 3, ceiling 5) | — |
| Score 5 prerequisites | Power < 80% blocks Score 5 | — |
| **Final score** | | **4** |

---

*Generated by SciSpark Evidence Evaluator · [scispark.ai](https://scispark.ai) · team@scispark.ai*
