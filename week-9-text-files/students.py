import csv

I_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    """Call the read_dictionary function to read the students
    file. Then ask for an I_number and check if a student with that
    I number exists in the dictionary.
    """
    # Create a dictionary from the students.csv.
    students_dic = read_dictionary("students.csv")

    # Get an I_number from the user to search for.
    i_number_search = input("Enter an I-Number: ")

    # If the I_number is in the dictionary, return the students name.
    # If it doesn't exist, display an error message.
    if i_number_search in students_dic:
        print(f"{students_dic[i_number_search][NAME_INDEX]}\n")
    else:
        print("No such student\n")

    

def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if row_list != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[I_NUMBER_INDEX]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

        return dictionary

if __name__ == "__main__":
    main()