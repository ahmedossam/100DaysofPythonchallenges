import tkinter as tk
from tkinter import messagebox
import numpy as np


# Function to perform the selected operation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = np.add(num1, num2)
        elif operation == "Subtract":
            result = np.subtract(num1, num2)
        elif operation == "Multiply":
            result = np.multiply(num1, num2)
        elif operation == "Divide":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = np.divide(num1, num2)
        else:
            result = "Invalid Operation"

        # Display the result
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))


# Creating the GUI window
window = tk.Tk()
window.title("Extended NumPy Calculator")

# Entry for first number
label1 = tk.Label(window, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

# Entry for second number
label2 = tk.Label(window, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Dropdown to select the operation
operation_var = tk.StringVar(window)
operation_var.set("Add")  # default value

operation_menu = tk.OptionMenu(window, operation_var, "Add", "Subtract", "Multiply", "Divide")
operation_menu.pack()

# Button to calculate the result
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Run the main loop
window.mainloop()
