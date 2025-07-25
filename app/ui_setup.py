import tkinter as tk
from tkinter import messagebox
import json

CONFIG_FILE = "config.json"

def save_config():
    goal = goal_entry.get().strip()
    try:
        delay = int(delay_entry.get())
        escape = escape_var.get()
    except ValueError:
        messagebox.showerror("Error", "Delay must be a number.")
        return

    if not goal:
        messagebox.showerror("Error", "Please enter a goal.")
        return

    config = {
        "goal": goal,
        "delay_minutes": delay,
        "escape_proof": escape
    }

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

    messagebox.showinfo("Saved", "Config saved successfully!")

app = tk.Tk()
app.title("Grind Guard Setup")
app.geometry("400x300")
app.configure(bg="#1e1e1e")

tk.Label(app, text="Your Daily Goal", fg="white", bg="#1e1e1e", font=("Segoe UI", 12)).pack(pady=10)
goal_entry = tk.Entry(app, font=("Segoe UI", 12), width=35)
goal_entry.pack()

tk.Label(app, text="Time Until Lock (in minutes)", fg="white", bg="#1e1e1e", font=("Segoe UI", 12)).pack(pady=10)
delay_entry = tk.Entry(app, font=("Segoe UI", 12), width=10)
delay_entry.pack()

escape_var = tk.BooleanVar()
tk.Checkbutton(app, text="Enable Escape-Proof Mode", variable=escape_var, fg="white", bg="#1e1e1e", font=("Segoe UI", 10), selectcolor="#1e1e1e").pack(pady=20)

tk.Button(app, text="Save Config", command=save_config, bg="#00aa88", fg="white", font=("Segoe UI", 12), width=20).pack(pady=10)

app.mainloop()