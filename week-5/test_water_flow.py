"""

Student: Tristan Galloway
Teacher: Brother Clements
file: test_water_flow.py
Purpose: To test the water_flow.py files functions 
using a variety of test cases.

"""

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
    """tests the water_column_height function
    with 4 test cases"""

    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == 57.9
    
def test_pressure_gain_from_water_height():
    """tests the pressure_gain_from_water_height function
    with 3 test cases"""

    assert pressure_gain_from_water_height(0) == approx(0, rel=.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, rel=.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, rel=.001)

def test_pressure_loss_from_pipe():
    """tests the test_pressure_loss_from_pipe function
    with 7 test cases"""

    assert pressure_loss_from_pipe(.048692, 0, .018, 1.75) == approx(0, rel=.001)
    assert pressure_loss_from_pipe(.048692, 200, 0, 1.75) == approx(0, rel=.001)
    assert pressure_loss_from_pipe(.048692, 200, .018, 0) == approx(0, rel=.001)
    assert pressure_loss_from_pipe(.048692, 200, .018, 1.75) == approx(-113.008, rel=.001) 
    assert pressure_loss_from_pipe(.048692, 200, .018, 1.65) == approx(-100.462, rel=.001)
    assert pressure_loss_from_pipe(.28687, 1000, .013, 1.65) == approx(-61.576, rel=.001)
    assert pressure_loss_from_pipe(.28687, 1800.75, .013, 1.65) == approx(-110.884, rel=.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])