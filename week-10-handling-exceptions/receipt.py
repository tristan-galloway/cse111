"""

Name: Tristan Galloway
Date: 11/16/2023
Purpose: Prove that you can write a Python program that reads 
CSV files and creates, populates, and uses a dictionary.
Prove that you can write a Python program that handles
exceptions, including FileNotFoundError and KeyError.
Resources: N/A

"""

import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.isoweekday()

def main():
    try:
        I_REQUEST_NUM = 0
        I_REQUEST_QTY = 1

        # Call my tg_read_dictionary and build the product dictionary.
        products_dict = tg_read_dictionary("products.csv", 0)

        # # Print all products in the dictionary.
        # print("\nAll Products")
        # print(products_dict)
        # print()

        # Open the request file as a csv.
        with open("request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)

            # Skips the first line which holds the category names.
            next(reader)

            print("Inkom Emporium\n")

            # Initialize a value to hold the total number of items and total cost
            item_qty = 0
            sub_total = 0

            # Iterate through the csv locating and storing the product
            # number, quantity, name, and price
            for row_list in reader:

                product_num = row_list[I_REQUEST_NUM]
                product_qty = row_list[I_REQUEST_QTY]

                I_PRODUCT_NUM = 0
                I_PRODUCT_NAME = 1
                I_PRODUCT_PRICE = 2

                item_list = products_dict[product_num]
                item_name = item_list[I_PRODUCT_NAME]
                item_price = item_list[I_PRODUCT_PRICE]
                # If the day is Tuesday or Wednesday, reduce product price by 10%
                discount = 0 
                if day_of_week == 2 or day_of_week == 3:
                    discount = item_price * .1
                    item_price -= discount

                item_qty += int(product_qty)
                sub_total += float(item_price) * int(product_qty)

                # Print all of the info for the reciept
                print(f"{item_name}: {product_qty}" \
                    f" @ {item_price}")

            # Calculate Sales Tax and Total
            sales_tax = sub_total * .06
            total = sub_total + sales_tax

            # Print receipt
            print(f"\nNumber of Items: {item_qty}")
            print(f"Subtotal: {round(sub_total, 2)}")
            print(f"Sales Tax: {round(sales_tax, 2)}")
            print(f"Total: {round(total, 2)}")
            print()
            print("Thank you for shopping at the Inkom Emporium.")
            print(f"{current_date_and_time:%c}")

    except FileNotFoundError as file_error:
        print()
        print("Error: missing file")
        print(file_error)

    except KeyError as key_error:
        print()
        print(f"Error: unknown product ID in the request.csv file")
        print(key_error)



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