"""

Student: Tristan Galloway
Teacher: Brother Clements
file: boxes.py
Purpose: Check your understanding of calling built-in Python functions and functions that are in a standard Python module.

"""
# Import math module so I can use math.ceil().
import math

# Asks the user for the quantity of items and how many of that item fits in a given box.
item = int(input("Enter the number of items: "))
qty_items = int(input("Enter the number of items per box: "))

# Take the number of items and devide it by how many will fit in a box to find out how many boxes to make.abs(x)
boxes = item / qty_items

# Return the number of boxes needed to the user.
print(f"\nFor {item} items, packing {qty_items} items in each box, you will need {math.ceil(boxes)} boxes.\n")
