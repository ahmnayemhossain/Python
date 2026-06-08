import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

DATA_FILE = Path(__file__).with_name("passwords.json")


def load_passwords():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return {}


def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    data = load_passwords()
    data[website] = {"email": email, "password": password}
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    messagebox.showinfo("Saved", "Password saved successfully.")


root = tk.Tk()
root.title("Password Manager GUI V1")
root.geometry("360x240")

tk.Label(root, text="Website").grid(row=0, column=0, padx=10, pady=8, sticky="w")
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=8, sticky="w")
tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=8, sticky="w")

website_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
password_entry = tk.Entry(root, width=30)

website_entry.grid(row=0, column=1, padx=10, pady=8)
email_entry.grid(row=1, column=1, padx=10, pady=8)
password_entry.grid(row=2, column=1, padx=10, pady=8)

tk.Button(root, text="Save", command=save_password).grid(row=3, column=1, pady=15)

root.mainloop()
