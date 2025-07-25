import customtkinter as ctk
import time
import os

escape_proof = False
SKIP_FILE = "skip_flag"

def run_lock_screen(delay_seconds, goal, escape_mode):
    global escape_proof
    escape_proof = escape_mode
    root = ctk.CTk()
    root.withdraw()
    def _maybe_show():
        if not escape_mode and os.path.exists(SKIP_FILE):
            try:
                last = int(open(SKIP_FILE).read())
                if time.time() - last < delay_seconds:
                    root.destroy()
                    return
            except:
                pass
        LockScreen(root, goal)
    root.after(int(delay_seconds * 1000), _maybe_show)
    root.mainloop()

class LockScreen(ctk.CTkToplevel):
    def __init__(self, parent, goal):
        super().__init__(parent)
        self.parent = parent
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+0+0")
        self.configure(bg="black")
        self._opacity = 0.0
        self.attributes("-alpha", self._opacity)
        self.after(0, self._fade_in)
        container = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=20)
        container.place(relx=0.5, rely=0.5, anchor="center")
        ctk.CTkLabel(
            container,
            text=f"⏰ Time to {goal}! ⏰",
            font=("Segoe UI", 28, "bold"),
            text_color="#BB86FC"
        ).pack(pady=(20,20), padx=20)
        ctk.CTkButton(
            container,
            text="I'm Done!",
            fg_color="#03DAC6",
            hover_color="#018786",
            command=self._done,
            width=200
        ).pack(pady=(0,10), padx=20, fill="x")
        if not escape_proof:
            ctk.CTkButton(
                container,
                text="I'm Seriously Busy",
                fg_color="#CF6679",
                hover_color="#B00020",
                command=self._skip,
                width=200
            ).pack(padx=20, fill="x")

    def _fade_in(self):
        self._opacity = min(self._opacity + 0.05, 0.8)
        self.attributes("-alpha", self._opacity)
        if self._opacity < 0.8:
            self.after(50, self._fade_in)

    def _done(self):
        self.destroy()
        self.parent.destroy()

    def _skip(self):
        with open(SKIP_FILE, "w") as f:
            f.write(str(int(time.time())))
        self.destroy()
        self.parent.destroy()
