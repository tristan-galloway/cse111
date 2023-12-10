import tkinter as tk

root = tk.Tk()

# Create a boolean variable
var = tk.BooleanVar()

# Create a checkbutton
checkbutton = tk.Checkbutton(root, text="Check me", variable=var)

# Pack the checkbutton
checkbutton.pack()

# Start the mainloop
root.mainloop()