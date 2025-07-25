import os, json
import customtkinter as ctk
from tkinter import messagebox
from app.overlay import run_lock_screen

CONFIG_PATH = os.path.join("config", "config.json")

def save_config_file(data):
    os.makedirs("config", exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f)

def load_config_file():
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

class GrindGuardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Grind Guard")
        self.geometry("420x480")
        self.resizable(False, False)

        cfg = load_config_file()
        self.goal_var    = ctk.StringVar(value=cfg.get("goal", "Workout for 30 minutes"))
        self.hours_var   = ctk.StringVar(value=str(cfg.get("hours", 0)))
        self.minutes_var = ctk.StringVar(value=str(cfg.get("minutes", 0)))
        self.seconds_var = ctk.StringVar(value=str(cfg.get("seconds", 0)))
        self.escape_var  = ctk.BooleanVar(value=cfg.get("escape_proof", False))

        self.create_widgets()
        self.bind("<Return>", lambda e: self.start_guard())

    def create_widgets(self):
        frm = ctk.CTkFrame(self, corner_radius=20)
        frm.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(frm, text="Grind Guard", font=("Segoe UI", 24, "bold")).pack(pady=(10,20))
        ctk.CTkEntry(frm, textvariable=self.goal_var, placeholder_text="Your Goal").pack(pady=10, fill="x")

        tf = ctk.CTkFrame(frm, fg_color="transparent")
        tf.pack(pady=10)

        he = ctk.CTkEntry(tf, textvariable=self.hours_var, width=80, placeholder_text="H")
        he.grid(row=0, column=0, padx=5)
        he.bind("<KeyRelease>", lambda e: self.cap(self.hours_var, 24))
        
        me = ctk.CTkEntry(tf, textvariable=self.minutes_var, width=80, placeholder_text="M")
        me.grid(row=0, column=1, padx=5)
        me.bind("<KeyRelease>", lambda e: self.cap(self.minutes_var, 59))
        
        se = ctk.CTkEntry(tf, textvariable=self.seconds_var, width=80, placeholder_text="S")
        se.grid(row=0, column=2, padx=5)
        se.bind("<KeyRelease>", lambda e: self.cap(self.seconds_var, 59))

        ctk.CTkLabel(tf, text="H").grid(row=1, column=0, pady=(4,0))
        ctk.CTkLabel(tf, text="M").grid(row=1, column=1, pady=(4,0))
        ctk.CTkLabel(tf, text="S").grid(row=1, column=2, pady=(4,0))

        ctk.CTkCheckBox(frm, text="Enable Escape‑Proof Mode", variable=self.escape_var).pack(pady=10)

        btn_save  = ctk.CTkButton(frm, text="Save Settings", command=self.save_settings)
        btn_save.pack(pady=(20,5), fill="x")
        btn_start = ctk.CTkButton(frm, text="Start Grind Guard", command=self.start_guard)
        btn_start.pack(fill="x")

        ctk.CTkLabel(frm, text="© 2025 Yomo Development™", font=("Segoe UI", 10), text_color="#666").pack(pady=(20,0))

    def cap(self, var, maximum):
        v = var.get()
        if not v.isdigit():
            var.set("0")
        else:
            iv = int(v)
            var.set(str(min(max(iv, 0), maximum)))

    def save_settings(self):
        cfg = {
            "goal":    self.goal_var.get(),
            "hours":   int(self.hours_var.get() or 0),
            "minutes": int(self.minutes_var.get() or 0),
            "seconds": int(self.seconds_var.get() or 0),
            "escape_proof": self.escape_var.get()
        }
        save_config_file(cfg)
        messagebox.showinfo("Settings Saved", "✅ Settings were saved.")

    def start_guard(self):
        cfg = {
            "goal":    self.goal_var.get(),
            "hours":   int(self.hours_var.get() or 0),
            "minutes": int(self.minutes_var.get() or 0),
            "seconds": int(self.seconds_var.get() or 0),
            "escape_proof": self.escape_var.get()
        }
        save_config_file(cfg)
        total = (cfg["hours"]*3600 + cfg["minutes"]*60 + cfg["seconds"])
        if total <= 0:
            messagebox.showerror("Invalid Time", "Set at least one second.")
            return
        self.destroy()
        run_lock_screen(total, cfg["goal"], cfg["escape_proof"])
