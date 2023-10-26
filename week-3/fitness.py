"""

Team: 3 (Tristan Galloway, Jude Ebigide, Andres Mendoza)
Teacher: Brother Clements
File: fitness.py
Purpose: Boost your understanding of writing your own functions with parameters and then calling those functions with arguments.

"""

# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Please enter your gender (M or F): ").upper()
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in U.S. pounds: "))
    stones = float(input("Enter your weight in British stones: "))
    feet = float(input("Enter your height in U.S. feet and inches: "))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    years = compute_age(birthdate)
    kg = kg_from_lb(pounds)
    st = kg_from_stone(stones)
    cm = cm_from_in(feet)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    # Print the results for the user to see.
    print(f"Age (years): {years}")
    print(f"Weight (kg from lb): {round(kg, 2)}")
    print(f"Weight (kg from st): {round(st, 2)}")
    print(f"Height (m): {round(cm / 100, 2)}")
    print(f"Body mass index: {round(bmi, 1)}")
    print(f"Basal metabolic rate (kcal/day): {round(bmr)}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kg = pounds / 2.2046

    return kg


def kg_from_stone(stones):
    """Convert a mass in stones to kilograms.
    Perameter stones: a mass in British stones.
    Return: the mass in kilograms.
    """
    kg = stones * 6.35

    return kg


def cm_from_in(feet):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    cm = feet * 30.48

    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = 10000*weight / height**2

    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "F":
        bmr = 447.593 + 9.247*weight + 3.098*height - 4.330*age
    elif gender == "M":
        bmr = 88.362 + 13.397*weight + 4.799*height - 5.677*age

    return bmr


# Call the main function so that
# this program will start executing.
main()