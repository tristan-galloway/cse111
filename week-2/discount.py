"""

Team: 3
Teacher: Brother Clements
File: discount.py
Purpose: Improve your understanding of calling built-in Python functions and calling 
functions and methods that are in a standard Python module.
Problem Statement: You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store’s slowest sales days.
On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater,
the store will discount the customer’s subtotal by 10%.

"""

import math
from datetime import datetime

# Ask the user for the subtotal
subtotal = float(input("Please enter the subtotal: "))

# Find todays day of the week and set the default discount to 0%.
todays_date = datetime.now().weekday()
discount = 0

# If it is the first or second day of the week (zero indexed) and the subtotal is
# greater then $50 apply a 10% discount to the subtotal.
if (3 > todays_date > 0) and subtotal > 50:
    discount = subtotal * .10
    subtotal -= discount
    print(f"Discount amount: {discount:.2f}")

tax = subtotal * .06
total = subtotal + tax

# Return to the user their tax, discount, and total.
print(f"Sales tax amount: {tax:.2f}")
print(f"Total: {total:.2f}\n")