# Stage 4: Bias Risk & Evidence Certainty Audit

## Purpose
Structured assessment of bias risk and evidence certainty using the appropriate validated tool for the study type. The LLM reads the paper using tiered context strategy and produces per-domain judgments with explicit evidence citations.

## Tool Selection by Study Type

| Study Type | Tool |
|---|---|
| `RCT_intervention` / `meta_analysis` / `preventive` | **RoB 2.0** (5 domains) |
| `diagnostic` | **QUADAS-2** (4 domains, capped at −2 total) |
| `observational` | **GRADE upgrading** (3 factors, capped at +1 total) |
| `phase_0_1` | **RoB 2.0 — limited** (randomization + selective reporting domains only) |

## Tiered Context Strategy
Use Tier 1 (abstract + methods + conclusion) first. For most RoB 2.0 domains (randomisation, blinding, LTFU, selective reporting), Tier 1 is sufficient — the relevant information is in methods. Signal `needs_full_paper: true` if trial registration details or supplementary protocols are required.

---

## RoB 2.0 — for RCT / meta-analysis / preventive

| Domain | What to Look For | Deduction |
|---|---|---|
| Randomization process | Allocation concealment details, sequence generation method | High risk: −1; Critical (unblinded + subjective outcome): −2 |
| Deviations from intervention | Protocol adherence, crossover rates, co-interventions | High risk: −1 |
| Missing outcome data | LTFU rates, imputation method (LOCF, MCAR, MNAR) | High risk: −1 |
| Measurement of outcome | Blinding of outcome assessors, objective vs. subjective outcome | Subjective + unblinded: −2 |
| Selection of reported results | Trial registration match, pre-specified vs. exploratory outcomes | High risk: −1 |

**For Phase 0/I:** Run ONLY randomization process + selection of reported results. Skip all others.

Judgment levels: `low | some_concerns | high | critical`

---

## QUADAS-2 — for diagnostic studies

| Domain | High-Risk Trigger | Deduction |
|---|---|---|
| Patient selection | Case-control design OR non-consecutive enrollment | −1 |
| Index test | Reference standard known during index test interpretation (verification bias) | −1 |
| Reference standard | Not independently validated as gold standard | −1 |
| Flow and timing | Long interval between index test and reference standard | −0.5 |

**QUADAS-2 cap:** Maximum −2 total regardless of raw sum.

**De-duplication with Stage 2:** Case-control spectrum bias deducted in Stage 2 + QUADAS-2 patient selection domain are the same bias — apply only once in Stage 5.

---

## GRADE Upgrading — for observational studies

| Factor | Trigger Conditions | Effect |
|---|---|---|
| Large effect size | RR > 2.0 or RR < 0.5; CI does not cross 1; P < 0.01 | +1 grade |
| Dose-response gradient | P_trend < 0.05; ≥ 3 dose levels; monotonic relationship | +1 grade |
| Plausible confounding | Bias direction favors null but result still significant | +1 grade |

**Upgrade cap:** Maximum +1 total even if multiple factors met.
**Grade ceiling:** Grade 3 → max 4; Grade 2 → max 3. Score 5 is reserved for Grade 5 starting studies only.

**When upgrades do NOT trigger:**
- **Large effect size:** Does NOT trigger if the CI is wide (imprecise estimate) or N < 30 (small sample inflates effect).
- **Dose-response gradient:** Does NOT trigger if only 2 dose groups (need ≥ 3) or if the dose-response curve is J-shaped or U-shaped (non-monotonic).
- **Plausible confounding:** Does NOT trigger if the confounding direction is unclear, or if the claim is based solely on authors' assertion without supporting data (unadjusted crude effect must be smaller than adjusted effect).

---

## Additional Checks (all study types)

### Surrogate Endpoint
If the primary outcome is a biomarker proxy rather than a hard clinical endpoint (e.g., HbA1c instead of cardiovascular events, tumor response instead of overall survival):
→ **−1 grade** (applied once; not duplicated)

Examples of surrogate endpoints: blood pressure, cholesterol levels, PSA, radiological response, HbA1c, CD4 count, viral load (depends on context).

### Meta-Analysis Inconsistency
If I² > 50% with no subgroup explanation or pre-specified heterogeneity analysis:
→ **−1 grade**

---

## Output Schema

For each domain assessed, output:
```json
{
  "domain": "domain_name",
  "evidence_found": "string — text located in the paper with section attribution (e.g., 'Methods §2.3: allocation was...')",
  "judgment": "low | some_concerns | high | critical | unclear",
  "delta": 0,
  "reasoning": "string — full explanation linking evidence to judgment and delta"
}
```

Plus:
```json
{
  "tool_used": "RoB_2.0 | QUADAS-2 | GRADE_upgrade",
  "additional_checks": {
    "surrogate_endpoint": { "detected": false, "evidence": "", "delta": 0 },
    "meta_analysis_inconsistency": { "applicable": false, "i_squared": null, "delta": 0 }
  },
  "stage_score_delta": 0.0
}
```

---

## Quality Principles for This Stage

- **Always cite the paper text** that supports each domain judgment. Do not assert bias without showing evidence.
- **Distinguish between absence of reporting and confirmed absence.** "Not reported" ≠ "Not done." Flag as `some_concerns` when information is missing.
- **Phase 0/I hard constraint:** Only two domains. Do not run other RoB 2.0 domains even if the paper contains enough information.
- **QUADAS-2 cap is non-negotiable.** Even if raw domain deductions sum to −3 or −4, apply max −2.
