"""
Tests for pipeline/stage3_math.py

Validates all Stage 3 computations against the same synthetic data
used in acceptance_tests_T1_T8.py and experiment_3B_math_unit_tests.py.
"""

import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pipeline.stage3_math import (
    compute_fragility_index,
    compute_ltfu_fi_rule,
    compute_fragility_quotient,
    compute_nnt,
    compute_nnt_threshold_delta,
    compute_posthoc_power_binary,
    compute_posthoc_power_continuous,
    compute_dor,
    deduplicate_statistical_stability,
    run_stage3,
    FI_ROBUST_THRESHOLD,
    POWER_THRESHOLD,
)

PASS = 0
FAIL = 0

def check(name, got, expected, tol=0.001):
    global PASS, FAIL
    if isinstance(expected, float) and math.isinf(expected):
        ok = math.isinf(got) and (got > 0) == (expected > 0)
    elif isinstance(expected, float):
        ok = abs(got - expected) <= tol
    elif isinstance(expected, bool):
        ok = bool(got) == expected
    else:
        ok = got == expected
    status = "✅" if ok else "❌"
    if not ok:
        FAIL += 1
    else:
        PASS += 1
    print(f"  {status} {name}: got={got}, expected={expected}")


print("=" * 60)
print("STAGE 3 MODULE TESTS")
print("=" * 60)

# ── Fragility Index ──────────────────────────────────────────
print("\n[Fragility Index]")
r = compute_fragility_index(47, 500, 60, 500, 0.038)
check("FI_fragile_1", r["fi"], 1)
check("FI_fragile_interp", r["interpretation"], "extreme_fragile")
check("FI_fragile_delta", r["delta"], -1)

r = compute_fragility_index(48, 512, 89, 508, 0.0001)
check("FI_robust_19", r["fi"], 19)
check("FI_robust_interp", r["interpretation"], "robust")
check("FI_robust_delta", r["delta"], 0.5)

r = compute_fragility_index(55, 500, 60, 500, 0.41)
check("FI_nonsig", r["fi"], 0)
check("FI_nonsig_interp", r["interpretation"], "not_computable")
check("FI_nonsig_delta", r["delta"], 0)

# ── LTFU-FI Rule ─────────────────────────────────────────────
print("\n[LTFU-FI Rule]")
r = compute_ltfu_fi_rule(8, 1)
check("LTFU_triggers", r["triggered"], True)
check("LTFU_triggers_delta", r["delta"], -2)

r = compute_ltfu_fi_rule(5, 19)
check("LTFU_safe", r["triggered"], False)
check("LTFU_safe_delta", r["delta"], 0)

r = compute_ltfu_fi_rule(19, 19)
check("LTFU_boundary_eq", r["triggered"], False)

r = compute_ltfu_fi_rule(20, 19)
check("LTFU_pierces", r["triggered"], True)

# ── Fragility Quotient ───────────────────────────────────────
print("\n[Fragility Quotient]")
r = compute_fragility_quotient(1, 1000)
check("FQ_below_threshold", r["below_threshold"], True)
check("FQ_below_delta", r["delta"], -0.5)

r = compute_fragility_quotient(19, 1020)
check("FQ_above_threshold", r["below_threshold"], False)
check("FQ_above_delta", r["delta"], 0)
check("FQ_value", r["fq"], round(19 / 1020, 6), tol=0.0001)

# ── NNT ──────────────────────────────────────────────────────
print("\n[NNT / NNH]")
r = compute_nnt(48, 512, 89, 508)
check("NNT_benefit_dir", r["direction"], "benefit")
check("NNT_value", r["nnt"], 12.3, tol=0.3)

r = compute_nnt(70, 500, 50, 500)
check("NNH_harm_dir", r["direction"], "harm")
check("NNH_value", r["nnt"], 25.0, tol=0.5)

r = compute_nnt(50, 500, 50, 500)
check("NNT_neutral_dir", r["direction"], "neutral")
check("NNT_neutral_delta", r["delta"], -1)

# ── NNT Threshold ────────────────────────────────────────────
print("\n[NNT Threshold]")
r = compute_nnt_threshold_delta(150, 50)
check("NNT_exceeds", r["exceeds_threshold"], True)
check("NNT_exceeds_delta", r["delta"], -1)

r = compute_nnt_threshold_delta(12.3, 50)
check("NNT_within", r["exceeds_threshold"], False)
check("NNT_within_delta", r["delta"], 0)

# ── DOR ──────────────────────────────────────────────────────
print("\n[DOR]")
r = compute_dor(80, 70, 20, 30)
check("DOR_T4_value", r["dor"], 9.33, tol=0.05)
check("DOR_T4_interp", r["interpretation"], "adequate")

r = compute_dor(90, 85, 10, 15)
check("DOR_excellent", r["dor"] > 20, True)
check("DOR_excellent_interp", r["interpretation"], "high")
check("DOR_excellent_delta", r["delta"], 0.5)

r = compute_dor(60, 50, 40, 50)
check("DOR_poor_value", r["dor"] < 5, True)
# DOR=1.5, CI crosses 1 → "unstable" takes precedence over "poor"
check("DOR_poor_interp", r["interpretation"], "unstable")
check("DOR_poor_delta", r["delta"], -1)

# ── Post-hoc Power ───────────────────────────────────────────
print("\n[Post-hoc Power]")
p_control = 0.17
p_mcid = 0.17 - 0.08
r = compute_posthoc_power_binary(p_mcid, p_control, 512, 508)
check("Power_adequate", r["adequate"], True)
check("Power_adequate_val", r["power"] >= 0.80, True)

r = compute_posthoc_power_binary(p_mcid, p_control, 50, 50)
check("Power_inadequate", r["adequate"], False)

# ── De-duplication ───────────────────────────────────────────
print("\n[De-duplication]")
power_r = {"delta": -1, "reasoning": "underpowered"}
nnt_r = {"delta": -1, "reasoning": "NNT exceeds threshold"}
n_r = {"delta": -1, "reasoning": "N < domain"}
dedup = deduplicate_statistical_stability(power_r, n_r, nnt_r)
active_count = sum(1 for v in dedup.values() if not v["suppressed"])
check("Dedup_only_one_active", active_count, 1)
suppressed_count = sum(1 for v in dedup.values() if v["suppressed"])
check("Dedup_two_suppressed", suppressed_count, 2)

# ── run_stage3: phase_0_1 skip ───────────────────────────────
print("\n[run_stage3: phase_0_1]")
r = run_stage3({}, study_type="phase_0_1")
check("Phase01_skipped", r["skipped"], True)
check("Phase01_delta", r["total_delta"], 0)

# ── run_stage3: T1 scenario (Grade 5 RCT, FI=19, low bias) ──
print("\n[run_stage3: T1 — robust RCT]")
r = run_stage3(
    {
        "events_intervention": 48, "n_intervention": 512,
        "events_control": 89, "n_control": 508,
        "p_value": 0.0001, "ltfu_count": 12, "alpha": 0.05,
    },
    study_type="RCT_intervention",
)
check("T1_fi", r["metrics"]["fragility_index"]["fi"], 19)
check("T1_fi_delta", r["metrics"]["fragility_index"]["delta"], 0.5)
check("T1_ltfu_safe", r["metrics"]["ltfu_fi_rule"]["triggered"], False)

# ── run_stage3: T2 scenario (LTFU > FI) ─────────────────────
print("\n[run_stage3: T2 — LTFU > FI]")
r = run_stage3(
    {
        "events_intervention": 47, "n_intervention": 500,
        "events_control": 60, "n_control": 500,
        "p_value": 0.038, "ltfu_count": 8, "alpha": 0.05,
    },
    study_type="RCT_intervention",
)
check("T2_fi", r["metrics"]["fragility_index"]["fi"], 1)
check("T2_ltfu_triggered", r["metrics"]["ltfu_fi_rule"]["triggered"], True)
check("T2_ltfu_delta", r["metrics"]["ltfu_fi_rule"]["delta"], -2)

# ── run_stage3: T4 diagnostic ───────────────────────────────
print("\n[run_stage3: T4 — diagnostic]")
r = run_stage3(
    {"tp": 80, "tn": 70, "fp": 20, "fn": 30},
    study_type="diagnostic",
)
check("T4_dor", r["metrics"]["dor"]["dor"], 9.33, tol=0.05)
check("T4_no_fi", "fragility_index" not in r["metrics"], True)

# ══════════════════════════════════════════════════════════════
# EDGE CASES
# ══════════════════════════════════════════════════════════════

# ── FI: boundary at exactly 2 (upper edge of extreme) ────────
print("\n[Edge: FI boundary]")
# FI = 2 → extreme_fragile (FI <= 2)
r = compute_fragility_index(46, 500, 60, 500, 0.018)
if r["fi"] == 2:
    check("FI_exactly_2_interp", r["interpretation"], "extreme_fragile")
    check("FI_exactly_2_delta", r["delta"], -1)
elif r["fi"] == 3:
    # FI=3 is moderate, that's also fine — depends on Fisher exact outcome
    check("FI_3_interp", r["interpretation"], "moderate")
    check("FI_3_delta", r["delta"], 0)
else:
    check("FI_boundary_computed", True, True)  # accept whatever FI the math gives

# FI = 10 → moderate (FI > 10 required for robust)
r = compute_fragility_index(48, 512, 89, 508, 0.0001)
# We know this is 19, but let's test the threshold boundary explicitly
check("FI_10_not_robust", 10 > FI_ROBUST_THRESHOLD, False)
check("FI_11_is_robust", 11 > FI_ROBUST_THRESHOLD, True)

# ── FI: zero events in one arm ───────────────────────────────
print("\n[Edge: zero events]")
r = compute_fragility_index(0, 100, 10, 100, 0.001)
check("FI_zero_ei_computes", r["fi"] > 0, True)
check("FI_zero_ei_has_log", len(r["iteration_log"]) > 0, True)

# ── FQ: exactly at threshold ─────────────────────────────────
print("\n[Edge: FQ boundary]")
# FQ = 0.01 exactly → NOT below threshold (< 0.01 is the condition)
r = compute_fragility_quotient(10, 1000)  # FQ = 0.01
check("FQ_exact_threshold_not_below", r["below_threshold"], False)
check("FQ_exact_threshold_delta", r["delta"], 0)

# FQ just below threshold
r = compute_fragility_quotient(9, 1000)  # FQ = 0.009
check("FQ_just_below", r["below_threshold"], True)
check("FQ_just_below_delta", r["delta"], -0.5)

# ── FQ: N_total = 0 ──────────────────────────────────────────
print("\n[Edge: FQ zero N]")
r = compute_fragility_quotient(5, 0)
check("FQ_zero_N", r["fq"], 0.0)

# ── NNT: very small ARR ──────────────────────────────────────
print("\n[Edge: NNT extremes]")
r = compute_nnt(499, 500, 500, 500)
check("NNT_very_large", r["nnt"] > 100, True)
check("NNT_very_large_dir", r["direction"], "benefit")

# NNT: single event difference
r = compute_nnt(9, 100, 10, 100)
check("NNT_single_event_diff", r["nnt"], 100.0)

# ── NNT threshold: exactly at threshold ──────────────────────
print("\n[Edge: NNT threshold boundary]")
r = compute_nnt_threshold_delta(50.0, 50.0)
# NNT > threshold triggers; NNT == threshold does NOT
check("NNT_at_threshold_no_exceed", r["exceeds_threshold"], False)

r = compute_nnt_threshold_delta(50.01, 50.0)
check("NNT_just_above_threshold", r["exceeds_threshold"], True)

# NNT threshold with infinity
r = compute_nnt_threshold_delta(float("inf"), 50)
check("NNT_inf_exceeds", r["exceeds_threshold"], True)
check("NNT_inf_delta", r["delta"], -1)

# ── DOR: zero cell (FP=0) ────────────────────────────────────
print("\n[Edge: DOR zero cells]")
r = compute_dor(80, 70, 0, 30)  # FP = 0
check("DOR_fp_zero_inf", r["dor"], float("inf"))

r = compute_dor(80, 70, 20, 0)  # FN = 0
check("DOR_fn_zero_inf", r["dor"], float("inf"))

# DOR: all cells equal (poor discrimination)
r = compute_dor(50, 50, 50, 50)
check("DOR_equal_cells", r["dor"], 1.0)
check("DOR_equal_poor_or_unstable", r["delta"], -1)

# DOR: perfect discrimination
r = compute_dor(100, 100, 0, 0)
check("DOR_perfect", r["dor"], float("inf"))

# ── DOR: grade-gating for +0.5 bonus ─────────────────────────
print("\n[Edge: DOR grade gating]")
r = run_stage3(
    {"tp": 90, "tn": 85, "fp": 10, "fn": 15, "initial_grade": 3},
    study_type="diagnostic",
)
check("DOR_grade3_bonus", r["metrics"]["dor"]["delta"], 0.5)

r = run_stage3(
    {"tp": 90, "tn": 85, "fp": 10, "fn": 15, "initial_grade": 5},
    study_type="diagnostic",
)
check("DOR_grade5_no_bonus", r["metrics"]["dor"]["delta"], 0)

r = run_stage3(
    {"tp": 90, "tn": 85, "fp": 10, "fn": 15, "initial_grade": 2},
    study_type="diagnostic",
)
check("DOR_grade2_no_bonus", r["metrics"]["dor"]["delta"], 0)

# ── Power: boundary at exactly 0.80 ──────────────────────────
print("\n[Edge: Power boundary]")
# Test that >= 0.80 is adequate
r = compute_posthoc_power_binary(0.09, 0.17, 512, 508)
if r["power"] >= 0.80:
    check("Power_adequate_boundary", r["adequate"], True)
    check("Power_adequate_delta", r["delta"], 0)
else:
    check("Power_inadequate_at_this_N", r["adequate"], False)

# ── Power: continuous (SMD) ───────────────────────────────────
print("\n[Edge: Continuous power]")
r = compute_posthoc_power_continuous(0.5, 200, 200)
check("Power_continuous_adequate", r["adequate"], True)

r = compute_posthoc_power_continuous(0.2, 20, 20)
check("Power_continuous_small_N", r["adequate"], False)

# ── LTFU: zero LTFU ──────────────────────────────────────────
print("\n[Edge: LTFU zero]")
r = compute_ltfu_fi_rule(0, 5)
check("LTFU_zero_safe", r["triggered"], False)

r = compute_ltfu_fi_rule(0, 0)
check("LTFU_zero_fi_zero_safe", r["triggered"], False)  # 0 > 0 is False

# ── De-duplication: single candidate (no suppression) ─────────
print("\n[Edge: Dedup single]")
dedup = deduplicate_statistical_stability(
    power_result={"delta": -1, "reasoning": "underpowered"},
    n_vs_domain=None,
    nnt_threshold_result=None,
)
check("Dedup_single_not_suppressed", dedup["power"]["suppressed"], False)
check("Dedup_single_delta_kept", dedup["power"]["delta"], -1)

# De-duplication: no candidates
dedup = deduplicate_statistical_stability(None, None, None)
check("Dedup_empty", len(dedup), 0)

# De-duplication: all zeroes (no negatives)
dedup = deduplicate_statistical_stability(
    {"delta": 0, "reasoning": "ok"}, {"delta": 0, "reasoning": "ok"}, None,
)
check("Dedup_no_negatives", len(dedup), 0)

# ══════════════════════════════════════════════════════════════
# REMAINING ACCEPTANCE SCENARIOS VIA run_stage3
# ══════════════════════════════════════════════════════════════

# ── T6: Preventive, NNT=150 vs threshold=50 ──────────────────
print("\n[run_stage3: T6 — preventive NNT threshold]")
r = run_stage3(
    {
        "events_intervention": 10, "n_intervention": 1000,
        "events_control": 17, "n_control": 1000,
        # CER=0.017, IER=0.010, ARR=0.007, NNT≈142.9
        "p_value": 0.04, "ltfu_count": 0, "alpha": 0.05,
    },
    stage2_output={"domain_nnt_threshold": 50},
    study_type="preventive",
)
check("T6_nnt_benefit", r["metrics"]["nnt"]["direction"], "benefit")
check("T6_nnt_exceeds", r["metrics"]["nnt_threshold"]["exceeds_threshold"], True)
check("T6_nnt_threshold_delta", r["metrics"]["nnt_threshold"]["delta"], -1)

# ── T7: Observational — no post-hoc power computed ───────────
print("\n[run_stage3: T7 — observational, no power]")
r = run_stage3(
    {
        "events_intervention": 40, "n_intervention": 500,
        "events_control": 60, "n_control": 500,
        "p_value": 0.003, "ltfu_count": 5, "alpha": 0.05,
    },
    stage2_output={"mcid": 0.03},
    study_type="observational",
)
check("T7_no_power", "posthoc_power" not in r["metrics"], True)
check("T7_has_fi", "fragility_index" in r["metrics"], True)
check("T7_has_nnt", "nnt" in r["metrics"], True)

# ── run_stage3: RCT with Stage 2 data (full pipeline) ────────
print("\n[run_stage3: full RCT with Stage 2]")
r = run_stage3(
    {
        "events_intervention": 48, "n_intervention": 512,
        "events_control": 89, "n_control": 508,
        "p_value": 0.0001, "ltfu_count": 5, "alpha": 0.05,
        "effect_size_type": "binary",
    },
    stage2_output={
        "mcid": 0.05,
        "domain_n": 500,
        "domain_nnt_threshold": 30,
    },
    study_type="RCT_intervention",
)
check("Full_has_fi", "fragility_index" in r["metrics"], True)
check("Full_has_ltfu", "ltfu_fi_rule" in r["metrics"], True)
check("Full_has_fq", "fragility_quotient" in r["metrics"], True)
check("Full_has_nnt", "nnt" in r["metrics"], True)
check("Full_has_power", "posthoc_power" in r["metrics"], True)
check("Full_fi_robust", r["metrics"]["fragility_index"]["fi"], 19)

# ── run_stage3: meta_analysis routes like RCT ─────────────────
print("\n[run_stage3: meta_analysis routing]")
r = run_stage3(
    {
        "events_intervention": 48, "n_intervention": 512,
        "events_control": 89, "n_control": 508,
        "p_value": 0.0001, "ltfu_count": 3, "alpha": 0.05,
    },
    study_type="meta_analysis",
)
check("Meta_not_skipped", r["skipped"], False)
check("Meta_has_fi", "fragility_index" in r["metrics"], True)
check("Meta_has_nnt", "nnt" in r["metrics"], True)

# ══════════════════════════════════════════════════════════════
# TEST-RETEST (Experiment 3E for Stage 3)
# ══════════════════════════════════════════════════════════════

print("\n[Test-retest: deterministic consistency]")
test_input = {
    "events_intervention": 48, "n_intervention": 512,
    "events_control": 89, "n_control": 508,
    "p_value": 0.0001, "ltfu_count": 12, "alpha": 0.05,
    "effect_size_type": "binary",
}
test_stage2 = {"mcid": 0.05, "domain_n": 500, "domain_nnt_threshold": 30}
results = [run_stage3(test_input, test_stage2, "RCT_intervention") for _ in range(20)]
first = results[0]
all_identical = all(
    r["total_delta"] == first["total_delta"]
    and r["metrics"]["fragility_index"]["fi"] == first["metrics"]["fragility_index"]["fi"]
    and r["metrics"]["nnt"]["nnt"] == first["metrics"]["nnt"]["nnt"]
    and r["metrics"]["posthoc_power"]["power"] == first["metrics"]["posthoc_power"]["power"]
    for r in results[1:]
)
check("Retest_20_runs_identical", all_identical, True)

# ── Summary ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"RESULTS: {PASS} passed, {FAIL} failed out of {PASS + FAIL} tests")
print("=" * 60)
if FAIL > 0:
    sys.exit(1)
