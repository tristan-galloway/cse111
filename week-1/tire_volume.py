"""

Student: Tristan Galloway
Teacher: Brother Clements
file: tire_volume.py
Purpose: Prove that you can write a Python program that gets input from a user, performs arithmetic, and displays results for the user to see.

"""

import math

# Collect from the user the width, aspect ratio, and diameter of their tire
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Using the users given info, calculate the volume of their tire in liters
volume = math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter) / 10 ** 10

# Return to user their tire's volume in liters
print(f"\nThe approximate volume is {volume:.2f} liters\n")