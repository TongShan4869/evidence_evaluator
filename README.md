# Evidence Evaluator — SciSpark EvidenceScore Skill

An AI agent skill implementing the **SciSpark EvidenceScore pipeline** (v2): a 6-stage agentic system that automatically generates structured evidence quality reports for clinical and biomedical research papers.

Mirrors the reasoning of a trained Evidence-Based Medicine (EBM) reviewer.

---

## Pipeline Overview

```
Input (PDF / text / DOI / PMID)
  → Stage 0: Study Type Pre-Routing
  → Stage 1: Variable Extraction & Initial Grading  [LLM, 3× majority vote]
  → Stage 2: Domain Benchmark & MCID Search          [LLM + web search, agentic]
  → Stage 3: Deterministic Math Audit                [FI, FQ, NNT, post-hoc power]
  → Stage 4: Bias Risk Audit                         [RoB 2.0 / QUADAS-2 / GRADE]
  → Stage 5: Evidence Evaluation Report Synthesis    [LLM + optional rule engine]
  → Output: Structured JSON Report + Narrative
```

---

## Repo Structure

```
evidence_evaluator/
├── SKILL.md                        ← Agent skill entry point
├── references/
│   ├── stages_0_1.md               ← Study type routing + variable extraction
│   ├── stages_2_3.md               ← MCID search + deterministic math audit
│   ├── stage_4.md                  ← Bias risk (RoB 2.0 / QUADAS-2 / GRADE)
│   ├── stage_5_report.md           ← Report synthesis + optional scoring
│   ├── formulas.md                 ← All formulas (FI, FQ, NNT, DOR, power)
│   └── eval_framework.md           ← Acceptance tests T1–T8 + Experiments 3A–3F
└── tests/
    ├── acceptance_tests_T1_T8.py   ← 8 acceptance test cases (all pass)
    └── experiment_3B_math_unit_tests.py  ← Stage 3 math unit tests (21/21 correct)
```

---

## Primary Output

A structured **Evidence Evaluation Report** with:

- **Section 1** — Study Design & Population (PICO, N, blinding, phase)
- **Section 2** — Statistical Robustness (Fragility Index, FQ, NNT, LTFU-FI rule, post-hoc power)
- **Section 3** — Clinical Benchmarking (MCID, observed effect vs. benchmark)
- **Section 4** — Bias Risk Assessment (per-domain RoB 2.0 / QUADAS-2 / GRADE findings)
- **Narrative Summary** — 500–800 word plain-language clinician-facing explanation
- **Optional** — Heuristic suggested 1–5 score via rule engine (labeled as pending expert calibration)

---

## Key Design Principles

- **Not a black-box classifier.** Every finding is auditable and citable.
- **Tiered reading.** Always uses abstract + methods + conclusion first; escalates to full text only when needed.
- **LTFU > FI is the hardest rule.** −2 grade, non-negotiable, not deduplicated.
- **Report is the contribution; score is optional.** The 1–5 score is a heuristic pending expert calibration — never presented as validated.
- **Findings only, no verdict.** The narrative surfaces what was found; the clinician judges what it means.

---

## Running Tests

```bash
# Acceptance tests T1–T8
python tests/acceptance_tests_T1_T8.py

# Stage 3 math unit tests (requires scipy, statsmodels)
pip install scipy statsmodels numpy
python tests/experiment_3B_math_unit_tests.py
```

---

## References

- Li et al. (Quicker), *npj Digital Medicine* 2025 — PICO extraction + CoT majority vote
- Wang et al. (TrialMind), *npj Digital Medicine* 2025 — Programmatic math audit pipeline
- Walsh et al. — Fragility Index
- Sterne et al., *BMJ* 2019 — RoB 2.0
- Whiting et al., *Annals of Internal Medicine* 2011 — QUADAS-2
- Guyatt et al., *Journal of Clinical Epidemiology* 2011 — GRADE

---

*Built by [SciSpark](https://scispark.ai) · team@scispark.ai*
