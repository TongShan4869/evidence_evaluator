---
name: evidence-evaluator
description: >
  Automated structured evidence evaluation of clinical/biomedical research papers via a
  6-stage agentic pipeline: (0) study type routing, (1) variable + PICO extraction with
  majority-vote confidence, (2) agentic MCID/domain benchmark retrieval, (3) deterministic
  math audit (Fragility Index, NNT, post-hoc power), (4) bias risk assessment (RoB 2.0 /
  QUADAS-2 / GRADE), (5) Evidence Evaluation Report synthesis. Outputs structured JSON +
  plain-language narrative. Optional heuristic 1-5 suggested score via rule engine.
  USE THIS SKILL when the user asks to evaluate, grade, or appraise a clinical paper;
  uploads a paper and wants evidence quality analyzed; asks about statistical robustness
  or bias risk; requests Fragility Index, NNT, post-hoc power, RoB 2.0, QUADAS-2, or
  MCID analysis; asks "is this paper good evidence?"; wants a structured EBM review;
  or asks about PICO extraction or study type classification.
---

# Evidence Evaluator Skill

A 6-stage agentic pipeline that produces a **structured Evidence Evaluation Report** for any clinical or biomedical research paper. Designed to match the reasoning of a trained EBM reviewer.

## Quick Start

1. **Receive paper** — PDF upload, pasted abstract/text, DOI, or PMID
2. **Run stages 0–5 sequentially** — each stage feeds the next via a shared `PipelineContext`
3. **Output report** — structured JSON + 500–800 word narrative summary
4. **Optional** — append heuristic suggested score (1–5) with explicit disclaimer

Read the stage references before running each stage:
- `references/stages_0_1.md` — Study type routing + variable extraction
- `references/stages_2_3.md` — MCID search + math audit
- `references/stage_4.md` — Bias risk assessment
- `references/stage_5_report.md` — Report synthesis + scoring
- `references/formulas.md` — All formulas (FI, FQ, NNT, DOR, power)
- `references/eval_framework.md` — Evaluation experiments + acceptance test cases

---

## Pipeline Architecture

```
Input (PDF / text / DOI / PMID)
  → Stage 0: Study Type Pre-Routing
  → Stage 1: Variable Extraction & Initial Grading  [LLM, 3× majority vote]
  → Stage 2: Domain Benchmark & MCID Search          [LLM + web search, agentic]
  → Stage 3: Deterministic Math Audit                [Python / formula walkthrough]
  → Stage 4: Bias Risk Audit                         [LLM]
  → Stage 5: Evidence Evaluation Report Synthesis    [LLM + rule engine]
  → Output: Structured JSON Report + Narrative
```

**Tiered context strategy** — always use abstract + methods + conclusion first (Tier 1). Only escalate to full text if agent signals `needs_full_paper: true`. This covers ~80% of cases at ~20% of token cost.

---

## Stage Execution Order

### Stage 0: Study Type Pre-Routing
Read `references/stages_0_1.md → Stage 0`.

Classify the paper into one of:
`RCT_intervention | diagnostic | preventive | observational | meta_analysis | phase_0_1`

Output a confidence score (0–1). If confidence < 0.7, flag for human review but continue.

**Routing consequences:**
- `phase_0_1` → skip Stage 2 + Stage 3 entirely; lock score range 1–2
- `diagnostic` → Stage 2 uses diagnostic thresholds (not MCID); Stage 3 computes DOR (not FI/NNT); Stage 4 uses QUADAS-2 (not RoB 2.0)
- All others → full pipeline

---

### Stage 1: Variable Extraction & Initial Grading
Read `references/stages_0_1.md → Stage 1`.

**LLM Strategy:** Self-reflection few-shot + 3× CoT majority vote.
Run extraction 3 times independently. Fields where all 3 agree = high confidence. Disagreements → `low_confidence_fields` flag.

Extract: N (intervention/control), events, LTFU count, p-value, effect size + type, CI, blinding, randomization, trial phase, alpha, stated power, primary outcome, PICO.

Assign **Initial Grade (1–5)** based on study design hierarchy. See grade table in `references/stages_0_1.md`.

Special rules: Phase 0/I → auto-lock Grade 2. Retracted paper → Excluded (no score).

---

### Stage 2: Domain Benchmark & MCID Search
Read `references/stages_2_3.md → Stage 2`.

**Skip if:** `study_type = phase_0_1`

Agentic search (up to 5 rounds) using Stage 1's PICO + `pico_search_string`.
Source priority: COMET/OMERACT → PubMed SRs → Society guidelines → Cohen's d proxy (Tier 4, flag with warning).

For diagnostic studies: retrieve AUC/Sn/Sp thresholds instead of MCID.

Evaluate: effect vs. MCID, N vs. domain standard, NNT vs. domain threshold.

---

### Stage 3: Deterministic Math Audit
Read `references/stages_2_3.md → Stage 3` and `references/formulas.md`.

**Skip if:** `study_type = phase_0_1`
**Diagnostic studies:** compute DOR only (skip FI/NNT)

Compute (deterministically):
1. **Fragility Index (FI)** — iterative Fisher exact test
2. **LTFU-FI Attrition Rule** — if LTFU > FI → hard −2 (highest priority)
3. **Fragility Quotient (FQ)** — FI / N_total
4. **Post-hoc Power** — using MCID as target effect size
5. **NNT / NNH** — from ARR = CER − IER
6. **DOR** (diagnostic only)

Show full computation trace with inputs, intermediate values, and interpretation.

De-duplication: among {power < 0.8, N < domain standard, NNT > threshold} — apply only the most severe deduction once.

---

### Stage 4: Bias Risk & Evidence Certainty Audit
Read `references/stage_4.md`.

Select tool based on study type:
- `RCT_intervention / meta_analysis / preventive` → **RoB 2.0** (5 domains)
- `diagnostic` → **QUADAS-2** (4 domains, capped at −2)
- `observational` → **GRADE upgrading** (3 factors, capped at +1)

Also check: surrogate endpoint (−1), meta-analysis I² > 50% (−1).

For Phase 0/I: run only randomization + selective reporting domains of RoB 2.0.

---

### Stage 5: Evidence Evaluation Report Synthesis
Read `references/stage_5_report.md`.

**Part 1 — Structured Findings (deterministic):** Assemble all stage outputs into 4 sections:
- Section 1: Study Design & Population
- Section 2: Statistical Robustness (Stage 3)
- Section 3: Clinical Benchmarking (Stage 2)
- Section 4: Bias Risk Assessment (Stage 4)

**Part 2 — Narrative Summary (LLM):** 500–800 words for clinician audience. Cover findings, not verdict. Do not render a final judgment — let the clinician decide.

**Part 3 — Optional Score (rule engine):** Apply boundary matrix + de-duplication to generate suggested 1–5 score. Label clearly: *"Suggested score — heuristic, pending expert calibration."*

---

## Output Format

Default output is plain text (structured sections + narrative). Pass `output_format: markdown` to also receive a fully-rendered `.md` file. See `references/stage_5_report.md → Part 5` for the full markdown template.

```
══════════════════════════════════════════════════════════
EVIDENCE EVALUATION REPORT
══════════════════════════════════════════════════════════
Paper: [title] | [journal] | [year]
Study type: [type] · Routing confidence: [X]%
══════════════════════════════════════════════════════════

SECTION 1 — STUDY DESIGN & POPULATION
  [PICO summary, N, phase, blinding, randomization]

SECTION 2 — STATISTICAL ROBUSTNESS
  Fragility Index (FI): [value]  [robust | fragile | extreme_fragile]
  Fragility Quotient (FQ): [value]  [below 0.01 threshold: yes/no]
  Post-hoc Power: [value]%  [≥ 0.80: yes/no]
  LTFU vs FI: LTFU=[X], FI=[Y]  [safe | ⚠ LTFU > FI — attrition concern]
  NNT: [value]  (domain threshold: [value])  [favorable | exceeds threshold]

SECTION 3 — CLINICAL BENCHMARKING
  MCID: [value] [units]  (source: [COMET | PubMed SR | Guidelines | Cohen proxy])
  Observed effect: [value]  vs. MCID: [exceeds | below | borderline]
  MCID source tier: [1–4]

SECTION 4 — BIAS RISK ASSESSMENT
  Tool: [RoB 2.0 | QUADAS-2 | GRADE]
  [Per-domain findings]
  Surrogate endpoint: [yes | no]
  Overall concern: [low | some_concerns | high | critical]

══════════════════════════════════════════════════════════
NARRATIVE SUMMARY
[500–800 words — findings, not verdict]
══════════════════════════════════════════════════════════

[OPTIONAL] SUGGESTED SCORE: [1–5] [★★★★☆]
  ⓘ Heuristic score — design choices pending expert calibration
══════════════════════════════════════════════════════════
```

---

## De-duplication Rules (apply in Stage 5)

1. **Statistical stability dimension:** Among {post-hoc power < 0.8, N < domain standard, NNT > threshold} → apply only the most severe deduction. Suppress others.
2. **Case-control spectrum bias (diagnostic):** Stage 2 case-control deduction vs. QUADAS-2 patient selection domain → apply only once.
3. **QUADAS-2 cap:** Max −2 total across all QUADAS-2 domains.
4. **GRADE upgrade cap:** Max +1 total regardless of how many factors are met.
5. **LTFU-FI hard rule:** −2 grade, highest priority. Not deduplicated with any other rule.

---

## Running Evaluations

To run the full PRD validation suite, see `references/eval_framework.md`.

Acceptance test cases (T1–T8) are defined there with expected outputs and pass criteria.

Validation experiments (3A–3F) follow the same file.

---

## Key Design Principles

- **Not a black-box classifier.** Every finding is auditable and citable.
- **Report is the contribution; score is optional.** The 1–5 score is a heuristic pending expert calibration — never present it as validated.
- **Findings only, no verdict.** The narrative summary surfaces what was found; the clinician judges what it means.
- **Tiered reading saves tokens.** Always Tier 1 first; only escalate on `needs_full_paper` signal.
- **LTFU > FI is the hardest rule.** −2 grade, not negotiable, not deduplicated.
