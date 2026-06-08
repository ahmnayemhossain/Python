import tkinter as tk


def add_to_expression(value):
    current_text = display_var.get()
    display_var.set(current_text + value)


def calculate():
    try:
        result = eval(display_var.get(), {"__builtins__": {}}, {})
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")


def clear_display():
    display_var.set("")


root = tk.Tk()
root.title("Simple Calculator GUI")
root.geometry("280x320")

title_label = tk.Label(root, text="Simple Calculator")
title_label.pack(pady=10)

calculator_frame = tk.Frame(root)
calculator_frame.pack()

display_var = tk.StringVar()
display_entry = tk.Entry(calculator_frame, textvariable=display_var, width=20, justify="right")
display_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, row, column in buttons:
    command = calculate if text == "=" else lambda value=text: add_to_expression(value)
    tk.Button(calculator_frame, text=text, width=5, command=command).grid(row=row, column=column, padx=3, pady=3)

tk.Button(root, text="Clear", command=clear_display).pack(pady=10)

root.mainloop()
