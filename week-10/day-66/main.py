import tkinter as tk

WORK_SECONDS = 25 * 60
BREAK_SECONDS = 5 * 60


class PomodoroApp:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("Pomodoro Timer GUI")
        self.timer_seconds = WORK_SECONDS
        self.running = False
        self.mode = "Work"
        self.timer_job = None

        self.mode_label = tk.Label(root_window, text=self.mode, font=("Arial", 18))
        self.mode_label.pack(pady=10)

        self.time_label = tk.Label(root_window, text=self.format_time(self.timer_seconds), font=("Arial", 28))
        self.time_label.pack(pady=10)

        tk.Button(root_window, text="Start", command=self.start_timer).pack(pady=5)
        tk.Button(root_window, text="Reset", command=self.reset_timer).pack(pady=5)

    def format_time(self, seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes:02d}:{remaining_seconds:02d}"

    def start_timer(self):
        if not self.running:
            self.running = True
            self.tick()

    def tick(self):
        if self.timer_seconds > 0 and self.running:
            self.timer_seconds -= 1
            self.time_label.config(text=self.format_time(self.timer_seconds))
            self.timer_job = self.root_window.after(1000, self.tick)
        elif self.running:
            if self.mode == "Work":
                self.mode = "Break"
                self.timer_seconds = BREAK_SECONDS
            else:
                self.mode = "Work"
                self.timer_seconds = WORK_SECONDS
            self.mode_label.config(text=self.mode)
            self.time_label.config(text=self.format_time(self.timer_seconds))
            self.timer_job = self.root_window.after(1000, self.tick)

    def reset_timer(self):
        self.running = False
        if self.timer_job:
            self.root_window.after_cancel(self.timer_job)
        self.mode = "Work"
        self.timer_seconds = WORK_SECONDS
        self.mode_label.config(text=self.mode)
        self.time_label.config(text=self.format_time(self.timer_seconds))


root = tk.Tk()
root.geometry("300x220")
app = PomodoroApp(root)
root.mainloop()
