"""

Student: Tristan Galloway
Teacher: Brother Clements
file: heart_rate.py
Purpose: Write a Python program that gets input from a user, uses variables, performs arithmetic, and displays results for the user to see.

"""

# Explanation of what the program should accomplish
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# Get the users age
user_age = int(input("Please enter your age: "))
# Calculate their max heart rate followed by what 85% and 65% respectfully are based on their age.
max_heart = 220 - user_age
low_range = max_heart * .65
hi_range = max_heart * .85

# Return to user the recommended heart rate range
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {low_range:.0f} and {hi_range:.0f} beats per minute.")

print("Commit_2")