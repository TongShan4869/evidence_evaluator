# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Evidence Evaluator is an installable Claude Code plugin containing a 6-stage agentic pipeline that produces structured evidence quality reports for clinical/biomedical research papers. Distributed as an open-source skill via `npx skills add SciSpark-ai/evidence_evaluator`.

## Repo Structure

```
.claude-plugin/plugin.json          ← Plugin manifest
skills/evidence-evaluator/
  SKILL.md                          ← Skill entry point
  pipeline/stage3_math.py           ← Stage 3: deterministic math (no LLM)
  pipeline/stage5_report.py         ← Stage 5: score engine + report assembly
  references/                       ← Stage specs, formulas, eval framework
tests/                              ← Development only (not part of skill package)
```

## Running Tests

```bash
pip install scipy statsmodels numpy

python tests/test_stage3_math.py                 # 147/147 pass
python tests/test_stage5_report.py               # 70/70 pass
```

Tests use a custom pass/fail counter (not pytest). They print results to stdout.

## Architecture

- `skills/evidence-evaluator/SKILL.md` — Skill entry point. Defines pipeline, stage execution order, output format, and Python code usage.
- `skills/evidence-evaluator/pipeline/stage3_math.py` — Deterministic math audit. Exports `run_stage3()`, `compute_fragility_index`, `compute_nnt`, `compute_dor`, etc. Routes by study type.
- `skills/evidence-evaluator/pipeline/stage5_report.py` — Score rule engine + report assembly. Exports `compute_suggested_score()`, `assemble_report()`, `deduplicate_stage4_deltas()`.
- `skills/evidence-evaluator/references/` — Stage specs the agent reads before executing each stage.
- `tests/` — Dev-only validation tests (not part of installed skill).

## Key Domain Rules

- **LTFU > FI hard rule**: LTFU exceeds FI → −2 grades, no exceptions, never deduplicated
- **De-duplication**: {power < 0.80, N < domain standard, NNT > threshold} → only most severe applies
- **Study type routing**: `phase_0_1` skips Stages 2+3, locks score 1–2; `diagnostic` uses QUADAS-2 + DOR
- **Score disclaimer**: 1–5 score is heuristic, pending expert calibration — always display disclaimer

## Tech Context

- Stage 3 and Stage 5 score engine are deterministic Python (scipy, statsmodels, numpy)
- Stages 0, 1, 2, 4 are agent reasoning tasks — no Python modules needed
- All Python commands must run from `skills/evidence-evaluator/` directory for imports to resolve
