import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

DATA_FILE = Path(__file__).with_name("secure_passwords.json")


def load_data():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return {}


def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showerror("Validation Error", "All fields are required.")
        return

    if len(password) < 8:
        messagebox.showerror("Validation Error", "Password must be at least 8 characters.")
        return

    data = load_data()
    data[website] = {"email": email, "password": password}
    save_data(data)
    messagebox.showinfo("Saved", "Password saved successfully.")
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def search_password():
    website = website_entry.get().strip()
    data = load_data()
    if website in data:
        record = data[website]
        messagebox.showinfo("Found", f"Email: {record['email']}\nPassword: {record['password']}")
    else:
        messagebox.showwarning("Missing", "Website not found.")


root = tk.Tk()
root.title("Password Manager Exam GUI")
root.geometry("380x260")

tk.Label(root, text="Website").grid(row=0, column=0, padx=10, pady=8, sticky="w")
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=8, sticky="w")
tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=8, sticky="w")

website_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
password_entry = tk.Entry(root, width=30)

website_entry.grid(row=0, column=1, padx=10, pady=8)
email_entry.grid(row=1, column=1, padx=10, pady=8)
password_entry.grid(row=2, column=1, padx=10, pady=8)

tk.Button(root, text="Search", command=search_password).grid(row=0, column=2, padx=5)
tk.Button(root, text="Save", command=save_password).grid(row=3, column=1, pady=15)

root.mainloop()
