"""

Student: Tristan Galloway
Teacher: Brother Clements
file: tire_volume.py
Purpose: Prove that you can write a Python program that calls functions and methods to get the current date and to append values to a text file.

"""

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
import math

# Collect from the user the width, aspect ratio, and diameter of their tire
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Using the users given info, calculate the volume of their tire in liters
volume = math.pi * width ** 2 * aspect * (width * aspect + 2540 * diameter) / 10 ** 10

# Return to user their tire's volume in liters
print(f"\nThe approximate volume is {volume:.2f} liters\n")

# Ask if the user would like to buy tires with the entered stats
purchase = input("Would you like to purchase tires with this volume (yes/no): ").lower()

# If the user wants the tires, get their number and store it in the volumes file.
# If they don't input a number, set the value as na for "not applicable"
if purchase == "yes":
    phone_number = input("Enter your phone number so we can contact you about your purchase (ex. 1234567899): ")
else:
    phone_number = "na"

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Open a text file named cities.txt in append mode.
with open('volumes.txt', 'at') as volumes_file:
    # Print the list of stats to the volumes file
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {aspect}, {diameter}, {volume:.2f}, {phone_number}", file=volumes_file)