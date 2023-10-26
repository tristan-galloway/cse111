"""

Student: Tristan Galloway
Date: 10/25/2023
Purpose: To test the water_flow.py files functions 
using a variety of test cases.
Resources: Week 5/6 study materials.

"""

from pytest import approx
import pytest
from water_flow import tg_water_column_height, tg_pressure_gain_from_water_height, tg_pressure_loss_from_pipe, tg_pressure_loss_from_fittings, tg_reynolds_number, tg_pressure_loss_from_pipe_reduction

def test_tg_water_column_height():
    """tests the water_column_height function
    with 4 test cases"""

    assert tg_water_column_height(0, 0) == 0
    assert tg_water_column_height(0, 10) == 7.5
    assert tg_water_column_height(25, 0) == 25
    assert tg_water_column_height(48.3, 12.8) == 57.9
    
def test_tg_pressure_gain_from_water_height():
    """tests the pressure_gain_from_water_height function
    with 3 test cases"""

    assert tg_pressure_gain_from_water_height(0) == approx(0, abs=.001)
    assert tg_pressure_gain_from_water_height(30.2) == approx(295.628, abs=.001)
    assert tg_pressure_gain_from_water_height(50) == approx(489.450, abs=.001)

def test_tg_pressure_loss_from_pipe():
    """tests the pressure_loss_from_pipe function
    with 7 test cases"""

    assert tg_pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert tg_pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert tg_pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert tg_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001) 
    assert tg_pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert tg_pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert tg_pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_tg_pressure_loss_from_fittings():
    """tests the pressure_loss_from_fittings function
    with 5 test cases"""

    assert tg_pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert tg_pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert tg_pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert tg_pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert tg_pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_tg_reynolds_number():
    """tests the tg_reynolds_number function
    with 5 test cases"""
    assert tg_reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert tg_reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert tg_reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert tg_reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert tg_reynolds_number(0.28687, 1.75) == approx(500318, abs=1)

def test_tg_pressure_loss_from_pipe_reduction():
    """tests the tg_pressure_loss_from_pipe_reduction function
    with 3 test cases"""
    assert tg_pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, 0.001)
    assert tg_pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, 0.001)
    assert tg_pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, 0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])