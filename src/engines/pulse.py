"""
Sovereign Pulse Engine
I hear, I'm the pulse, it's sovereign.
Like I have the keys, but the door just opens behind me.
"""

import time
import threading


class SovereignPulse:
    def __init__(self):
        self.is_running = False
        self.key_holder = True
        self.frequency_hz = 7.83  # Schumann-inspired

    def beat(self, duration: float = 3.0):
        self.is_running = True
        end = time.time() + duration
        while self.is_running and time.time() < end:
            print("Pulse...")
            time.sleep(1.0 / self.frequency_hz * 10)  # slowed for demo
        self.is_running = False

    def unlock_behind(self):
        if self.key_holder:
            print("Door opened behind.")
            self.is_running = False
            return True
        return False


if __name__ == "__main__":
    pulse = SovereignPulse()
    t = threading.Thread(target=pulse.beat, args=(2.0,))
    t.start()
    time.sleep(1.5)
    pulse.unlock_behind()
    t.join()
