"""

Student: Tristan Galloway
Teacher: Brother Clements
file: water_flow.py
Purpose: Prove that you can write a Python program and 
write and run test functions to help you find and fix 
mistakes in your program.

"""

def water_column_height(tower_height, tank_height):
    """Returns the water column height based on the 
    tower height and tank height
    """

    wch = tower_height + (3 * tank_height / 4)

    return wch


def pressure_gain_from_water_height(height):
    """Returns pressure gain based on the 
    tower height
    """

    pressure_gain = 998.2 * 9.80665 * height / 1000

    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Returns pressure gain based on the 
    pipe diameter, pipe length, friction of the water,
    and the fluids velocity.
    """

    pressure_lost = -friction_factor * pipe_length * 998.2 * fluid_velocity**2 / (2000 * pipe_diameter)

    return pressure_lost