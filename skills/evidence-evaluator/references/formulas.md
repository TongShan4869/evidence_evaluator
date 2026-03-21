# Key Formulas Reference

All formulas used in Stage 3 and Stage 5 of the Evidence Evaluator pipeline.

## Basic Event Rate Computations

| Metric | Formula | Notes |
|---|---|---|
| Control Event Rate (CER) | `CER = Ec / Nc` | Events in control arm / N control |
| Intervention Event Rate (IER) | `IER = Eᵢ / Nᵢ` | Events in intervention arm / N intervention |
| Absolute Risk Reduction (ARR) | `ARR = CER − IER` | Positive = benefit; negative = harm; zero = no difference |
| Absolute Risk Increase (ARI) | `ARI = IER − CER` | Used when ARR < 0 (harm direction) |

## NNT / NNH

| Scenario | Formula | Interpretation |
|---|---|---|
| ARR > 0 (benefit) | `NNT = 1 / ARR` | Patients needed to treat for one additional benefit |
| ARR < 0 (harm) | `NNH = 1 / ARI` | Informational only; no automatic deduction |
| ARR = 0 (neutral) | NNT = ∞ | Treat as exceeding any domain threshold → −1 |
| NNT 95% CI | Wilson CI on ARR → `NNT_CI = [1/ARR_upper, 1/ARR_lower]` | Report alongside point estimate |
| NNH 95% CI | Wilson CI on ARI → `NNH_CI = [1/ARI_upper, 1/ARI_lower]` | Informational |

## Fragility Index (FI)

**Algorithm:**
1. Compute initial Fisher exact test P-value from 2×2 contingency table
2. If P ≥ 0.05: FI = 0 (not computable / not significant)
3. If P < 0.05: increment `events_intervention` by 1, recompute P
4. Repeat until P ≥ 0.05
5. FI = total number of increments

**Interpretation:**
- FI ≤ 2 → extreme fragility → −1 grade
- FI 3–10 → moderate fragility → no delta
- FI > 10 → robust → +0.5 grade (other conditions must also be met)

**Always show:** iteration log with flip_count and Fisher P at each step.

## LTFU-FI Attrition Rule

```
If LTFU_count > FI:
  → Apply −2 grade (HARD RULE — highest priority, never deduplicated)
```

**Rationale:** More patients dropped out than it takes to flip the result. The observed effect is fragile relative to its own missing data.

## Fragility Quotient (FQ)

```
FQ = FI / (Nᵢ + Nc)   [i.e., FI / N_total]
```

**Threshold:** FQ < 0.01 → −0.5 grade

**Intuition:** FI normalized by sample size. Small FI in a large trial is less concerning than in a small trial.

## Post-hoc Power

Computed using MCID from Stage 2 as the target effect size. Python equivalents:

| Effect type | Computation |
|---|---|
| Binary (RR/OR) | `h = proportion_effectsize(p1, p2)`; then `NormalIndPower().solve_power(effect_size=h, nobs1=n1, ratio=n2/n1, alpha=alpha)` |
| Continuous (SMD/MD) | `TTestIndPower().solve_power(effect_size=SMD, nobs1=n1, ratio=n2/n1, alpha=alpha)` |
| HR (time-to-event) | `NormalIndPower().solve_power(effect_size=log_HR/SE, nobs1=n_events, ...)` |

**Threshold:** Power < 0.80 → −1 grade

## Diagnostic Metrics

| Metric | Formula |
|---|---|
| Sensitivity | `TP / (TP + FN)` |
| Specificity | `TN / (TN + FP)` |
| Positive Likelihood Ratio (LR+) | `Sensitivity / (1 − Specificity)` |
| Negative Likelihood Ratio (LR−) | `(1 − Sensitivity) / Specificity` |
| Diagnostic Odds Ratio (DOR) | `(TP × TN) / (FP × FN)` = `LR+ / LR−` |
| DOR 95% CI | `exp(log(DOR) ± 1.96 × SE)` where `SE = sqrt(1/TP + 1/FP + 1/TN + 1/FN)` |

**DOR thresholds:**
- DOR < 5 → poor discrimination → −1 grade
- DOR > 20 (Grade 3/4 only) → high discrimination → +0.5 grade
- CI crosses 1 → result unstable → −1 grade

## 2×2 Contingency Table Reference

```
                 Event    No Event
Intervention:     Eᵢ       Nᵢ − Eᵢ
Control:          Ec       Nc − Ec
```

Fisher exact test uses this table directly.
