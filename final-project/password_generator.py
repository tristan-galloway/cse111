"""

Name: Tristan Galloway
Date: 12/9/2023
Purpose: Generate and store passwords for a user. Allow user to 
select password length and what characters it can include. Then
allow the user to copy the generated password.
Resources: list_of_links.docx

"""

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math
import string
import random

def main():
	# Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Password Generator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
	"""Populate the main window of this program. In other words, put
	the labels, text entry boxes, and buttons into the main window.

	Parameter
		frm_main: the main frame (window)
	Return: nothing
	"""
	# Create a label that displays "Length:"
	lbl_password_length = Label(frm_main, text="Length:")

	# Create an integer entry box where the user will enter their desired password length.
	ent_password_length = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=14)

	# Create a label that displays "characters"
	lbl_password_length_units = Label(frm_main, text="characters")

	# Create a label that displays "Password:"
	lbl_password_return = Label(frm_main, text="Password:")

	# Create labels that will display the results.
	lbl_password_gen = Label(frm_main, width=14)

	# Create checkbutton variables and boxes for letters, digits, and punctuation.
	letters = tk.BooleanVar()
	digits = tk.BooleanVar()
	punctuation = tk.BooleanVar()
	checkbutton_letters = tk.Checkbutton(frm_main, text="Letters", variable=letters)
	checkbutton_digits = tk.Checkbutton(frm_main, text="digits", variable=digits)
	checkbutton_punctuation = tk.Checkbutton(frm_main, text="punctuation", variable=punctuation)
	
	# Create the Clear button.
	btn_clear = Button(frm_main, text="Clear")

	# Create a button widget
	btn_copy = tk.Button(frm_main, text="Copy", command=lambda: frm_main.clipboard_append(lbl_password_gen)) # This is currently not working.

	# Layout all the labels, entry boxes, and buttons in a grid.
	checkbutton_letters.grid(row=0, column=0, padx=5, pady=3)
	checkbutton_digits.grid(row=0, column=1, padx=5, pady=3)
	checkbutton_punctuation.grid(row=0, column=2, padx=5, pady=3)

	lbl_password_length.grid(row=1, column=0, padx=3, pady=3)
	ent_password_length.grid(row=1, column=1, padx=3, pady=3)
	lbl_password_length_units.grid(row=1, column=2, padx=0, pady=3)
	
	lbl_password_return.grid(row=2, column=0, padx=(30, 3), pady=3)
	lbl_password_gen.grid(row=2, column=1, padx=3, pady=3)

	btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")
	btn_copy.grid(row=3, column=2, padx=3, pady=3, columnspan=4, sticky="w")

	# This function will be called each time the user releases a key.
	def generate_password(event):
		"""Create and display users password."""

		try:
			# Get the length of the desired password.
			length = ent_password_length.get()
			character_list = ""

			# If the checkbox "letters" is selected, add letters to the
			# possible characters in the password.
			if letters.get():
				character_list += string.ascii_letters

			# If the checkbox "digits" is selected, add digits to the
			# possible characters in the password.
			if digits.get():
				character_list += string.digits

			# If the checkbox "punctuation" is selected, add punctuation to the
			# possible characters in the password.
			if punctuation.get():
				character_list += string.punctuation

			# Initialize password string.
			password = ""

			for i in range(length):

				# Picking a random character from our 
				# character list
				randomchar = random.choice(character_list)
				
				# appending a random character to password
				password += randomchar

			# Display the password to the user
			lbl_password_gen.config(text=password)

		except ValueError:
			# When the user deletes all the digits in the age
			# entry box, clear the area label
			lbl_password_gen.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
	def clear():
		"""Clear all the inputs and outputs."""
		btn_clear.focus()
		ent_password_length.clear()
		lbl_password_gen.config(text="")
		ent_password_length.focus()

	# Bind the calculate function to the age entry box so
	# that the computer will call the calculate function
	# when the user changes the text in the entry box.
	ent_password_length.bind("<KeyRelease>", generate_password)

	# Bind the clear function to the clear button so
	# that the computer will call the clear function
	# when the user clicks the clear button.
	btn_clear.config(command=clear)

	# Give the keyboard focus to the age entry box.
	ent_password_length.focus()

# If the program is run rather then being imported, call main.
if __name__ == "__main__":
	main()