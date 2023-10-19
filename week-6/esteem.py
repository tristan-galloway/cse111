"""

Team: 3 (Tristan Galloway, Jude Ebigide)
Teacher: Brother Clements
File: esteem.py
Purpose: Write a program with several functions. Use a debugger while 
writing your program or after writing it to step through your code.

"""

questions = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.", "I am able to do things as well as most other people.", "I feel I do not have much to be proud of.", "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.", "I wish I could have more respect for myself.", "I certainly feel useless at times.", "At times I think I am no good at all."]

def main():

    instructions = """This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement.
"""

    print(instructions)

    question_score = 0 
    total_score = 0

    for i, question in enumerate(questions):
        print(f"{i + 1}. {question}")
        response = input("   Enter D, d, a, or A: ")
        question_score = determine_score(i + 1, response)
        total_score += question_score

    print(f"\nYour score is {total_score}.")
    print("A score below 15 may indicate problematic low self-esteem.")

def determine_score(question_number, response):

    postitive_questions = [1, 2, 4, 6, 7] 

    if question_number in postitive_questions:
        if response == "D":
            return 0
        elif response == "d":
            return 1
        elif response == "a":
            return 2
        elif response == "A":
            return 3
    else:
        if response == "D":
            return 3
        elif response == "d":
            return 2
        elif response == "a":
            return 1
        elif response == "A":
            return 0

main()           