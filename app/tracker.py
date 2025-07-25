from pynput import mouse, keyboard
import threading, time

class ActivityTracker:
    def __init__(self):
        self.active_time = 0
        self.last_input = time.time()
        self.running = True
        self.lock = threading.Lock()

    def on_input(self, *args):
        with self.lock:
            self.last_input = time.time()

    def start(self):
        self.mouse_listener = mouse.Listener(on_move=self.on_input, on_click=self.on_input)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_input)
        self.mouse_listener.start()
        self.keyboard_listener.start()
        threading.Thread(target=self._track, daemon=True).start()

    def _track(self):
        while self.running:
            with self.lock:
                if time.time() - self.last_input < 60:
                    self.active_time += 1
            time.sleep(1)

    def get_active_minutes(self) -> int:
        return self.active_time // 60

    def stop(self):
        self.running = False