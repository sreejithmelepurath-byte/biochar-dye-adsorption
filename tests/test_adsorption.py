"""Checks the calculations against hand-worked values and recovers known
parameters from synthetic curves (synthetic data is used only in tests)."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import adsorption as ad  # noqa: E402


def test_percent_removal():
    assert ad.percent_removal(0.80, 0.20) == pytest.approx(75.0)


def test_capacity():
    # (100 - 25 mg/L) * 0.010 L / 0.050 g = 15 mg/g
    assert ad.capacity_mg_per_g(100, 25, 10, 50) == pytest.approx(15.0)


def test_template_has_no_readings_yet():
    template = pd.read_csv(Path(__file__).resolve().parents[1] / "data" / "experiment_template.csv")
    assert ad.process_runs(template).empty


def test_langmuir_fit_recovers_parameters():
    ce = np.linspace(5, 200, 12)
    qe = ad.langmuir(ce, 40.0, 0.03)
    langmuir = ad.fit_isotherms(ce, qe)[0]
    assert langmuir.params["q_max"] == pytest.approx(40.0, rel=1e-3)
    assert langmuir.r_squared > 0.999


def test_pseudo_second_order_fit_recovers_parameters():
    t = np.array([10, 20, 30, 40, 50, 60], dtype=float)
    qt = ad.pseudo_second_order(t, 18.0, 0.02)
    pso = ad.fit_kinetics(t, qt)[1]
    assert pso.params["q_e"] == pytest.approx(18.0, rel=1e-3)
