import tkinter as tk
from tkinter import ttk

# Function to update the input field when a button is pressed
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression and update the input field
def button_equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("error")
        expression = ""

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x324")
root.resizable(0, 0)
root.configure(bg="lightgray")

expression = ""
input_text = tk.StringVar()

# Style configuration
style = ttk.Style()
style.configure("TFrame", background="lightgray")
style.configure("TButton", font=("Arial", 12), padding=10)
style.configure("TEntry", font=("Arial", 18), padding=10)

# Frame for the input field
input_frame = ttk.Frame(root, style="TFrame")
input_frame.pack(side=tk.TOP)

# Input field inside the frame
input_field = ttk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), justify=tk.RIGHT, state='readonly', style="TEntry")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for the buttons
btns_frame = ttk.Frame(root, style="TFrame")
btns_frame.pack()

# Button style configuration
button_style = {
    "background": "#fff",
    "foreground": "#000",
    "activebackground": "#e6e6e6",
    "activeforeground": "#000",
}

# Create a button with a specific style
def create_button(parent, text, command, **options):
    return tk.Button(parent, text=text, command=command, **button_style, **options)

# First row
clear = create_button(btns_frame, text="C", command=button_clear, width=32)
clear.grid(row=0, column=0, columnspan=3)
divide = create_button(btns_frame, text="/", command=lambda: button_click("/"), width=10)
divide.grid(row=0, column=3)

# Second row
seven = create_button(btns_frame, text="7", command=lambda: button_click(7), width=10)
seven.grid(row=1, column=0)
eight = create_button(btns_frame, text="8", command=lambda: button_click(8), width=10)
eight.grid(row=1, column=1)
nine = create_button(btns_frame, text="9", command=lambda: button_click(9), width=10)
nine.grid(row=1, column=2)
multiply = create_button(btns_frame, text="*", command=lambda: button_click("*"), width=10)
multiply.grid(row=1, column=3)

# Third row
four = create_button(btns_frame, text="4", command=lambda: button_click(4), width=10)
four.grid(row=2, column=0)
five = create_button(btns_frame, text="5", command=lambda: button_click(5), width=10)
five.grid(row=2, column=1)
six = create_button(btns_frame, text="6", command=lambda: button_click(6), width=10)
six.grid(row=2, column=2)
minus = create_button(btns_frame, text="-", command=lambda: button_click("-"), width=10)
minus.grid(row=2, column=3)

# Fourth row
one = create_button(btns_frame, text="1", command=lambda: button_click(1), width=10)
one.grid(row=3, column=0)
two = create_button(btns_frame, text="2", command=lambda: button_click(2), width=10)
two.grid(row=3, column=1)
three = create_button(btns_frame, text="3", command=lambda: button_click(3), width=10)
three.grid(row=3, column=2)
plus = create_button(btns_frame, text="+", command=lambda: button_click("+"), width=10)
plus.grid(row=3, column=3)

# Fifth row
zero = create_button(btns_frame, text="0", command=lambda: button_click(0), width=21)
zero.grid(row=4, column=0, columnspan=2)
point = create_button(btns_frame, text=".", command=lambda: button_click("."), width=10)
point.grid(row=4, column=2)
equals = create_button(btns_frame, text="=", command=button_equal, width=10)
equals.grid(row=4, column=3)

# Start the main loop
root.mainloop()
