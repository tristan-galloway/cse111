"""

Student: Tristan Galloway
Date: 10/25/2023
Purpose: Prove that you can write a Python program and 
write and run test functions to help you find and fix 
mistakes in your program.
Resources: Week 5/6 study materials.

"""

WATER_DENSITY = 998.2
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DYNAMIC_VISCOSITY = 0.0010016

def tg_water_column_height(tower_height, tank_height):
    """Returns the water column height based on the 
    tower height and tank height
    """

    wch = tower_height + (3 * tank_height / 4)

    return wch


def tg_pressure_gain_from_water_height(height):
    """Returns pressure gain based on the 
    tower height
    """

    pressure_gain = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000

    return pressure_gain

def tg_pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Returns pressure gain based on the 
    pipe diameter, pipe length, friction of the water,
    and the fluids velocity.
    """

    pressure_lost = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2 / (2000 * pipe_diameter)

    return pressure_lost

def tg_pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Returns the pressure loss from
    pipe fittings.
    """

    loss = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000

    return loss

def tg_reynolds_number(hydraulic_diameter, fluid_velocity):
    """calculates and returns the Reynolds number 
    for a pipe with water flowing through it.
    """
    reynolds =  WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY 

    return reynolds

def tg_pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """calculates the water pressure lost because 
    of water moving from a pipe with a large 
    diameter into a pipe with a smaller diameter.
    """

    k = (.1 + (50/reynolds_number)) * ((larger_diameter/smaller_diameter) ** 4 - 1)

    pressure_loss = -k * WATER_DENSITY * fluid_velocity ** 2 / 2000

    return pressure_loss

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def tg_main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = tg_water_column_height(tower_height, tank_height)
    pressure = tg_pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = tg_reynolds_number(diameter, velocity)
    loss = tg_pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = tg_pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = tg_pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = tg_pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    tg_main()