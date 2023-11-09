"""

Name: Tristan Galloway
Date: 11/8/2023
Purpose: Prove that you can write a Python program that reads 
CSV files and creates, populates, and uses a dictionary.
Resources: N/A

"""

import csv

def main():

    I_REQUEST_NUM = 0
    I_REQUEST_QTY = 1

    # Call my tg_read_dictionary and build the product dictionary.
    products_dict = tg_read_dictionary("products.csv", 0)

    # Print all products in the dictionary.
    print("\nAll Products")
    print(products_dict)
    print()

    # Open the request file as a csv.
    with open("request.csv", "rt") as csv_file:

        reader = csv.reader(csv_file)

        # Skips the first line which holds the category names.
        next(reader)

        print("Requested Items")

        # Iterate through the document locating and storing the product
        # number, quantity, name, and price
        for row_list in reader:

            product_num = row_list[I_REQUEST_NUM]
            product_qty = row_list[I_REQUEST_QTY]

            item_list = products_dict[product_num]

            I_PRODUCT_NUM = 0
            I_PRODUCT_NAME = 1
            I_PRODUCT_PRICE = 2

            # Print all of the info for the reciept
            print(f"{item_list[I_PRODUCT_NAME]}: {product_qty} @ {item_list[I_PRODUCT_PRICE]}")



def tg_read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    I_PRODUCT_NUM = 0
    I_PRODUCT_NAME = 1
    I_PRODUCT_PRICE = 2

    # Initialize the product dictionary.
    prod_dic = {}

    # Open the user file and read it as a csv.
    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        # Skip the first line in the csv.
        next(reader)

        # Create a compound dictionary by adding each item
        # to the product dictionary.
        for row_list in reader:

            # Store the key in each list.
            key = row_list[I_PRODUCT_NUM]

            # Use the key to store the info in the row to the dictionary.
            prod_dic[key] = row_list

    return prod_dic



if __name__ == "__main__":
    main()