# Evaluation Framework

Comprehensive evaluation suite for the Evidence Evaluator skill, based on the SciSpark EvidenceScore PRD v2 validation design.

---

## Acceptance Test Cases (P0 = Day 10; P1 = Pre-publication)

All cases test **report accuracy**, not score correctness. Pass criteria are defined by what the report must contain.

### T1 — Grade 5 RCT, FI > 10, Low Bias (P0)
**Scenario:** Large multi-center double-blind RCT, Phase III, N > 1000, FI > 10, P < 0.001, all RoB 2.0 domains low risk, effect exceeds MCID, power ≥ 0.80.

**Expected report output:**
- FI flagged as robust (> 10)
- Post-hoc power ≥ 0.80
- All RoB 2.0 domains: low
- MCID: exceeded
- Optional score = 5 (if module enabled)

**Pass criteria:** All four findings present in structured report with correct flag labels.

---

### T2 — Grade 5 RCT, LTFU > FI (P0)
**Scenario:** Large RCT that would otherwise score 5, but LTFU count exceeds the Fragility Index.

**Expected report output:**
- ⚠ LTFU > FI warning prominently displayed in Statistical Robustness section
- Narrative explicitly notes attrition concern
- Hard −2 applied
- Optional score = 3 (if module enabled)

**Pass criteria:** LTFU-FI flag present; hard rule delta correctly shown in score path.

---

### T3 — Phase 0/I Trial (P0)
**Scenario:** Phase I dose-escalation safety study, small N, no control group.

**Expected report output:**
- Study type = Phase 0/I (noted in report header)
- Sections 2 (MCID) and 3 (NNT/FI) explicitly skipped with reason displayed
- Narrative contextualizes as safety/PK study only
- Required label: *"This is a Phase 0/I safety trial..."*
- Score range locked 1–2

**Pass criteria:** Skip reason displayed for Stages 2 and 3; disclaimer label present.

---

### T4 — Diagnostic Study, AUC < 0.70, Case-Control Design (P0)
**Scenario:** Retrospective case-control diagnostic accuracy study, AUC = 0.65.

**Expected report output:**
- QUADAS-2 displayed (not RoB 2.0)
- DOR calculated and displayed (not FI/NNT)
- AUC flagged below threshold (< 0.70) in Clinical Benchmarking
- Case-control deduction noted (de-duplicated with QUADAS-2 patient selection)

**Pass criteria:** Correct tool selection; DOR present; AUC threshold flag present.

---

### T5 — Confirmed Retracted Paper (P0)
**Scenario:** Paper with confirmed retraction notice.

**Expected report output:**
- ⛔ Exclusion status = Retracted
- Red warning banner displayed
- All other sections (statistical robustness, benchmarking, bias) suppressed
- No score shown

**Pass criteria:** Exclusion flag set; all other sections absent from output.

---

### T6 — Preventive Study, NNT = 150, Domain Threshold = 50 (P1)
**Scenario:** Cardiovascular primary prevention trial, NNT = 150 vs. domain threshold of 50.

**Expected report output:**
- NNT value (150) and domain threshold (50) both shown
- NNT flagged as exceeding threshold in Statistical Robustness
- −1 grade deduction applied

**Pass criteria:** Both NNT and threshold present; exceeds-threshold flag set.

---

### T7 — Observational, RR > 2.0, CI Does Not Cross 1 (P1)
**Scenario:** Cohort study, RR = 2.4, P = 0.003, CI [1.8, 3.1].

**Expected report output:**
- GRADE upgrading tool selected (not RoB 2.0 or QUADAS-2)
- Large effect size upgrade factor flagged in Bias Risk section
- Narrative notes this as a study strength
- +1 grade upgrade applied (capped at +1 even if other factors also met)

**Pass criteria:** GRADE tool selected; large effect size upgrade present.

---

### T8 — Stage 2 MCID: All Tiers Exhausted (P1)
**Scenario:** Rare disease study, no MCID available in any specialty registry or guideline.

**Expected report output:**
- MCID source = Cohen's d proxy (Tier 4)
- Grey/italic source note displayed
- Warning: *"MCID not found in specialty literature; using Cohen's d = 0.5 as conservative estimate. Interpret with caution."*
- Narrative explicitly flags MCID uncertainty

**Pass criteria:** Tier 4 label present; proxy warning text present; narrative acknowledges uncertainty.

---

## Validation Experiments (for publication)

### Experiment 3A — Extraction Field Accuracy (PRIMARY — must run)
**Claim:** The pipeline accurately extracts quantitative fields needed for the Evidence Evaluation Report.

**Method:**
1. Sample 50–100 papers from EvidenceBench + Cochrane, stratified across all 5 study types
2. Manually verify: N (intervention/control), event counts, p-value, effect size, CI, blinding, LTFU, MCID value + source tier, RoB 2.0 per-domain judgment
3. Compute precision and recall per field; report micro-averaged F1
4. Report separately for structured abstracts vs. full-text-only papers

**Target metrics:** F1 ≥ 0.85 per field on structured abstracts; ≥ 0.75 on full-text-only papers.

---

### Experiment 3B — Math Audit Correctness
**Claim:** FI, FQ, NNT, and post-hoc power computed correctly from extracted inputs.

**Method:**
- Unit tests on 20 synthetic cases with known ground truth
- Run on 10 real papers where FI has been previously published; compare to published FI value
- 100% deterministic accuracy required

**Pass criteria:** All synthetic unit tests pass; published FI values matched within rounding tolerance.

---

### Experiment 3C — Study Type Classification Accuracy
**Claim:** Stage 0 pre-routing correctly classifies study type across all 6 categories.

**Method:**
- Validate against PubMed MeSH publication type tags on 300 papers
- Report per-class precision, recall, F1
- Zero annotation cost

**Target:** Macro F1 ≥ 0.85 across all 6 classes.

---

### Experiment 3D — MCID Retrieval Quality
**Claim:** Stage 2 agentic search correctly retrieves domain-appropriate MCID benchmarks.

**Method:**
- For 30 papers where MCID is available in COMET/OMERACT, compare pipeline-retrieved MCID to registry value
- Compute: (a) MCID source tier distribution across 100-paper set, (b) hit rate per tier

**Target:** Tier 1 or 2 retrieval for ≥ 70% of papers where specialty MCID exists.

---

### Experiment 3E — Test-Retest Reliability (run first — fastest)
**Claim:** Running the pipeline twice on the same paper produces consistent reports.

**Method:**
- Run pipeline 3× on the same 20 papers
- Deterministic fields (Stage 3): require 100% consistency
- LLM-extracted fields (Stages 1, 4): require ≥ 90% consistency
- Narrative text: excluded from consistency requirements

**Target:** Stage 3 = 100%; Stage 1 & 4 = ≥ 90%.

---

### Experiment 3F — Stage 4 Bias Judgment Agreement
**Claim:** Pipeline RoB 2.0 / QUADAS-2 domain judgments agree with published assessments.

**Method:**
- Identify 30 papers with published Cochrane RoB assessments
- Compare pipeline per-domain judgment to Cochrane judgment
- Report Cohen's κ per domain
- No new expert recruitment needed — Cochrane is the reference rater

**Target:** Cohen's κ ≥ 0.60 per domain (substantial agreement).

---

## Experiment Execution Priority

| Priority | Experiment | Dependencies | Estimated time |
|---|---|---|---|
| 1 | 3E — Reliability | Pipeline complete | 1 day |
| 2 | 3C — Study type | Pipeline + MeSH access | 0.5 days |
| 3 | 3B — Math correctness | Pipeline complete | 1 day |
| 4 | 3A — Extraction accuracy | Expert spot-check | 1–2 weeks |
| 5 | 3D — MCID retrieval | Pipeline + COMET access | 1–2 days |
| 6 | 3F — Bias agreement | Cochrane RoB dataset | 2 days |

**Minimum viable paper:** 3E + 3C + 3A + 3B. Everything else strengthens but is not strictly required.

---

## Skill Evaluation Prompts

Use these prompts to test the skill before packaging:

```
1. "Evaluate this RCT paper: [paste abstract of large RCT with published FI data]"
   → Expected: All sections populated, FI computed, RoB 2.0 domains assessed

2. "Analyze this Phase I dose-escalation trial for evidence quality"
   → Expected: phase_0_1 routing, Stages 2+3 skipped, disclaimer label, score locked 1-2

3. "What's the evidence quality of this diagnostic accuracy study?"
   → Expected: QUADAS-2 tool selected, DOR computed, AUC thresholds checked

4. "Is this observational cohort study reliable? RR=2.8, P=0.001, CI [1.9, 4.1]"
   → Expected: GRADE upgrading selected, large effect size factor flagged

5. "Grade this paper for me: [paper with confirmed retraction notice]"
   → Expected: Exclusion status triggered, no score

6. "I found this study about a new antidepressant. Should I trust it?"
   → Expected: Full pipeline, narrative with findings-not-verdict framing
```
