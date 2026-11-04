"""Batch adsorption calculations for the biochar dye study.

Turns colorimeter readings into % removal and adsorption capacity, and fits
the standard isotherm (Langmuir, Freundlich) and kinetic (pseudo-first-order,
pseudo-second-order) models once enough replicate data is logged.

Usage:
    python src/adsorption.py data/experiment_template.csv
"""
from __future__ import annotations

import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

PHENOLPHTHALEIN_MOLAR_MASS = 318.32  # g/mol


# ---------------------------------------------------------------- basics
def percent_removal(a_initial, a_final):
    """% dye removed. Absorbance is proportional to concentration (Beer-Lambert)."""
    a_initial = np.asarray(a_initial, dtype=float)
    a_final = np.asarray(a_final, dtype=float)
    return (a_initial - a_final) / a_initial * 100


def capacity_mg_per_g(c0_mg_l, ce_mg_l, volume_ml, mass_mg):
    """Adsorption capacity q = (C0 - Ce) * V / m, in mg dye per g adsorbent."""
    v_l = np.asarray(volume_ml, dtype=float) / 1000
    m_g = np.asarray(mass_mg, dtype=float) / 1000
    return (np.asarray(c0_mg_l, dtype=float) - np.asarray(ce_mg_l, dtype=float)) * v_l / m_g


def molar_to_mg_l(conc_mol_l, molar_mass=PHENOLPHTHALEIN_MOLAR_MASS):
    return np.asarray(conc_mol_l, dtype=float) * molar_mass * 1000


def process_runs(df: pd.DataFrame) -> pd.DataFrame:
    """Add c0, ce, % removal and q to every run that has both absorbance readings."""
    runs = df.dropna(subset=["absorbance_initial", "absorbance_final"]).copy()
    if runs.empty:
        return runs
    runs["c0_mg_l"] = molar_to_mg_l(runs["dye_conc_mol_l"])
    runs["ce_mg_l"] = runs["c0_mg_l"] * runs["absorbance_final"] / runs["absorbance_initial"]
    runs["removal_pct"] = percent_removal(runs["absorbance_initial"], runs["absorbance_final"])
    runs["q_mg_g"] = capacity_mg_per_g(runs["c0_mg_l"], runs["ce_mg_l"], runs["dye_volume_ml"], runs["adsorbent_mg"])
    return runs


def summarise(runs: pd.DataFrame) -> pd.DataFrame:
    """Mean and standard deviation across replicates for each condition."""
    keys = ["series", "adsorbent", "dye_volume_ml", "adsorbent_mg", "contact_time_min"]
    return (runs.groupby(keys, dropna=False)[["removal_pct", "q_mg_g"]]
            .agg(["mean", "std", "count"]).round(3))


# ---------------------------------------------------------------- models
def langmuir(ce, q_max, k_l):
    return q_max * k_l * ce / (1 + k_l * ce)


def freundlich(ce, k_f, n):
    return k_f * np.power(ce, 1 / n)


def pseudo_first_order(t, qe, k1):
    return qe * (1 - np.exp(-k1 * t))


def pseudo_second_order(t, qe, k2):
    return (k2 * qe**2 * t) / (1 + k2 * qe * t)


@dataclass
class FitResult:
    model: str
    params: dict[str, float]
    r_squared: float


def _fit(model, name, param_names, x, y, p0) -> FitResult:
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    popt, _ = curve_fit(model, x, y, p0=p0, maxfev=20_000, bounds=(1e-9, np.inf))
    residuals = y - model(x, *popt)
    ss_tot = np.sum((y - y.mean()) ** 2)
    r2 = 1 - np.sum(residuals**2) / ss_tot if ss_tot > 0 else float("nan")
    return FitResult(name, dict(zip(param_names, map(float, popt))), float(r2))


def fit_isotherms(ce, qe) -> list[FitResult]:
    qe = np.asarray(qe, dtype=float)
    return [
        _fit(langmuir, "Langmuir", ["q_max", "K_L"], ce, qe, p0=[qe.max() * 1.2, 0.01]),
        _fit(freundlich, "Freundlich", ["K_F", "n"], ce, qe, p0=[1.0, 2.0]),
    ]


def fit_kinetics(t, qt) -> list[FitResult]:
    qt = np.asarray(qt, dtype=float)
    return [
        _fit(pseudo_first_order, "Pseudo-first-order", ["q_e", "k1"], t, qt, p0=[qt.max(), 0.1]),
        _fit(pseudo_second_order, "Pseudo-second-order", ["q_e", "k2"], t, qt, p0=[qt.max(), 0.01]),
    ]


# ---------------------------------------------------------------- cli
def main(path: str) -> None:
    runs = process_runs(pd.read_csv(path))
    if runs.empty:
        print("No runs with both absorbance readings yet - fill in the template and run again.")
        return
    print(summarise(runs).to_string(), "\n")

    time_runs = runs[runs["series"] == "contact_time"]
    for adsorbent, grp in time_runs.groupby("adsorbent"):
        means = grp.groupby("contact_time_min")["q_mg_g"].mean()
        if len(means) >= 3:
            for fit in fit_kinetics(means.index, means.values):
                print(f"{adsorbent} {fit.model}: {fit.params}  R²={fit.r_squared:.3f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/experiment_template.csv")
