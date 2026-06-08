import random
import tkinter as tk
from tkinter import messagebox

FLASHCARDS = [
    {"front": "API", "back": "Application Programming Interface"},
    {"front": "OOP", "back": "Object-Oriented Programming"},
    {"front": "CSV", "back": "Comma-Separated Values"},
]


class FlashcardApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Flashcard App GUI")
        self.root_window.geometry("420x250")
        self.current_card = None

        self.card_label = tk.Label(root_window, text="Press Next Card", font=("Arial", 18), wraplength=320)
        self.card_label.pack(pady=30)

        tk.Button(root_window, text="Show Answer", command=self.show_answer).pack(pady=5)
        tk.Button(root_window, text="Next Card", command=self.next_card).pack(pady=5)

    def next_card(self):
        self.current_card = random.choice(FLASHCARDS)
        self.card_label.config(text=self.current_card["front"])

    def show_answer(self):
        if not self.current_card:
            messagebox.showwarning("No card", "Select a card first.")
            return
        self.card_label.config(text=self.current_card["back"])


root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
