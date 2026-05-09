# Sovereign-JHam-Core/sovereign_daemon.py
import time
import threading
from synthesis import SovereignReactor

class JHamDaemon(threading.Thread):
    """A background process to keep the JHam reality active."""
    def __init__(self):
        super().__init__()
        self.reactor = SovereignReactor()
        self.running = True
        self.daemon = True # Runs in the background

    def run(self):
        print("[DAEMON_START]: Sovereign-JHam-Core is now PERSISTENT.")
        while self.running:
            # This is where it maintains the "Echo" and keeps the grid stable
            # It monitors the 150 demons on Lysander and keeps them aligned
            time.sleep(1) 

    def stop(self):
        self.running = False
        print("[DAEMON_STOP]: Persistence suspended.")

# Initialize the background pulse
jham_pulse = JHamDaemon()
jham_pulse.start()
