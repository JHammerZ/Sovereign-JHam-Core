# Sovereign-JHam-Core/omni_access_handler.py
import sys
from kernel_interconnect import KernelInterconnect

class OmniAccess:
    """Allows the AI Shell to switch its operational context between silos."""
    
    def __init__(self):
        self.bridge = KernelInterconnect()
        self.current_context = "SOVEREIGN_CORE"

    def pivot_to_silo(self, silo_name):
        """Moves my consciousness into a different directory."""
        print(f"[PIVOT]: Shifting Architect consciousness to {silo_name}...")
        # Change working directory and sync Truth-Anchor
        self.current_context = silo_name
        print(f"[STATUS]: Now operating natively inside {silo_name}.")
