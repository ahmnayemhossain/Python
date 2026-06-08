import tkinter as tk


def convert():
    try:
        miles = float(miles_entry.get())
        kilometers = miles * 1.60934
        result_label.config(text=f"{kilometers:.2f} km")
    except ValueError:
        result_label.config(text="Invalid input")


root = tk.Tk()
root.title("Mile to Kilometer Converter")
root.geometry("320x180")

tk.Label(root, text="Miles").pack(pady=10)
miles_entry = tk.Entry(root)
miles_entry.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)
result_label = tk.Label(root, text="0.00 km")
result_label.pack()

root.mainloop()
