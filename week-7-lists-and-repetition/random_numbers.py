"""

Team 3: Tristan Galloway, Jude Ebigide
Date: 10/25/2023
Purpose: Write and call a function that demonstrates both default parameter values and pass by reference.
Resources: W3 Schools

"""

import random

def main():

    numbers = [16.2, 75.1, 52.3]
    words = ["car", "people", "bottle"]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    append_random_words(words, 4)
    print(words)


def append_random_numbers(numbers_list, quantity = 1):
    """Takes a list from the user and a quantity of numbers
    to add, then generates that quantity random numbers rounded
    to one decimal place, then appends those numbers to the user
    given list.
    """

    i = 1
    while i <= quantity:
        number = random.uniform(0, 100)
        number = round(number, 1)
        numbers_list.append(number)
        i += 1

def append_random_words(words_list, quantity = 1):
    """
    """
    
    list_of_words = ["phone", "glasses", "backpack", "shoe", "book"]

    i = 1
    while i <= quantity:
        word = random.choice(list_of_words)
        words_list.append(word)
        i += 1 

if __name__ == "__main__":
    main()