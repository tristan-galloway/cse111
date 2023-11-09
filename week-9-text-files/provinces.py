"""

Name: Tristan Galloway
Date: 11/07/2023
Purpose: Check your understanding of text files and lists by writing
a program that reads the contents of a text file into a list and 
then changes some of the values in the list.
Sources: N/A

"""

def main():
    # Read the contents of the provinces file into a list.
    provinces_list = tg_read_list("provinces.txt")

    PROVINCES_LIST_INDEX = 0
    COUNT_AB_INDEX = 1

    print(provinces_list[PROVINCES_LIST_INDEX])

    print(f"\nAlberta Occurs {provinces_list[COUNT_AB_INDEX]} times in the modified list.")

def tg_read_list(filename):

    # Create an empty list that will store
    # the lines of text from the text file.
    pronvices_list = []
    count_AB = 0

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:
        
        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # If the cleaned line is "AB" replace it with Alberta and 
            # increment the count_AB variable.
            if clean_line == "AB":
                clean_line = "Alberta"

            # Append the clean line of text
            # onto the end of the list.
            pronvices_list.append(clean_line)
                
        # Remove the first and last element of the list
        pronvices_list.pop(0)
        pronvices_list.pop(len(pronvices_list) - 1)
 
        # Count each instance of "Alberta" in the modified list.
        for line in pronvices_list:
            if line == "Alberta":
                count_AB += 1

    return pronvices_list, count_AB


# Call main to start this program.
if __name__ == "__main__":
    main()