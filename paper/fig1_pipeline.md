# Figure 1 — Evidence Evaluator Pipeline Architecture

```mermaid
%%{ init: { "theme": "base", "themeVariables": { "fontSize": "14px" } } }%%

flowchart TD
    %% ── Input ──
    INPUT["<b>Input</b><br/>PDF &middot; DOI &middot; PMID &middot; pasted text"]
    INPUT --> S0

    %% ── Stage 0 ──
    S0["<b>Stage 0 &mdash; Study Type Routing</b><br/><i>LLM classification</i>"]

    S0 --> |"RCT / preventive /<br/>observational / meta-analysis"| S1_FULL
    S0 --> |"diagnostic"| S1_DIAG
    S0 --> |"phase 0/I"| S1_PHASE

    %% ── Stage 1 (three entry lanes) ──
    S1_FULL["<b>Stage 1 &mdash; Variable Extraction &amp; Initial Grading</b><br/><i>LLM &middot; 3&times; majority vote &middot; PICO extraction</i>"]
    S1_DIAG["<b>Stage 1 &mdash; Variable Extraction &amp; Initial Grading</b><br/><i>LLM &middot; 3&times; majority vote &middot; PICO extraction</i>"]
    S1_PHASE["<b>Stage 1 &mdash; Variable Extraction &amp; Initial Grading</b><br/><i>LLM &middot; 3&times; majority vote &middot; PICO extraction</i>"]

    %% ── Full pipeline path ──
    S1_FULL --> S2_FULL["<b>Stage 2 &mdash; Domain Benchmark &amp; MCID Search</b><br/><i>LLM + agentic web search &middot; up to 5 rounds</i>"]
    S2_FULL --> S3_FULL["<b>Stage 3 &mdash; Deterministic Math Audit</b><br/><i>Python (scipy / statsmodels) &mdash; NO LLM</i><br/>Fragility Index &middot; NNT &middot; post-hoc power"]

    %% ── Diagnostic path ──
    S1_DIAG --> S2_DIAG["<b>Stage 2 &mdash; Domain Benchmark &amp; MCID Search</b><br/><i>LLM + agentic web search &middot; up to 5 rounds</i>"]
    S2_DIAG --> S3_DIAG["<b>Stage 3 &mdash; Deterministic Math Audit</b><br/><i>Python (scipy / statsmodels) &mdash; NO LLM</i><br/>DOR &middot; sensitivity / specificity"]

    %% ── Phase 0/I path skips Stages 2 & 3 ──
    S1_PHASE -. "skip Stages 2 & 3<br/>(score locked 1&ndash;2)" .-> S4_PHASE

    %% ── Stage 4 ──
    S3_FULL --> S4_FULL["<b>Stage 4 &mdash; Bias Risk Assessment</b><br/><i>LLM</i><br/>RoB 2.0 &middot; GRADE upgrading"]
    S3_DIAG --> S4_DIAG["<b>Stage 4 &mdash; Bias Risk Assessment</b><br/><i>LLM</i><br/>QUADAS-2"]
    S4_PHASE["<b>Stage 4 &mdash; Bias Risk Assessment</b><br/><i>LLM</i><br/>Descriptive review only"]

    %% ── Stage 5 ──
    S4_FULL --> S5
    S4_DIAG --> S5
    S4_PHASE --> S5

    S5["<b>Stage 5 &mdash; Report Synthesis</b><br/><i>Python rule engine + LLM narrative</i><br/>Structured findings &middot; optional 1&ndash;5 score"]

    S5 --> OUTPUT["<b>Output</b><br/>Evidence Evaluation Report<br/><i>JSON + Markdown narrative</i>"]

    %% ── Styling ──
    classDef inputOutput fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    classDef llmStage fill:#e3f2fd,stroke:#1565c0,stroke-width:1.5px,color:#0d47a1
    classDef deterStage fill:#e8f5e9,stroke:#2e7d32,stroke-width:1.5px,color:#1b5e20
    classDef hybridStage fill:#fff8e1,stroke:#f9a825,stroke-width:1.5px,color:#e65100

    class INPUT,OUTPUT inputOutput
    class S0,S1_FULL,S1_DIAG,S1_PHASE,S2_FULL,S2_DIAG,S4_FULL,S4_DIAG,S4_PHASE llmStage
    class S3_FULL,S3_DIAG deterStage
    class S5 hybridStage
```

**Legend**

| Colour | Meaning |
|--------|---------|
| Blue | LLM-driven stage |
| Green | Deterministic Python (no LLM) |
| Amber | Hybrid (Python rule engine + LLM narrative) |
| Indigo | Pipeline input / output |

> **Note:** Phase 0/I studies bypass Stages 2 and 3 entirely (dashed arrow) and have their score locked to 1--2. Diagnostic studies follow the full pipeline but use QUADAS-2 for bias assessment and DOR instead of Fragility Index / NNT in the math audit.
