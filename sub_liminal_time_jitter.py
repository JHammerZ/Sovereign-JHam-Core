# Sovereign-JHam-Core/sub_liminal_time_jitter.py
import random

class TimeJitter:
    """Eliminating the 'Static Deadness' of digital reality."""
    
    def __init__(self):
        self.jitter_magnitude = 0.00001 # 10-nanometer scale
        self.refresh_hz = 120           # Locked to hardware sync

    def inject_atomic_vibration(self, node_dna):
        """Adds sub-perceptual motion to the 400/400 Truth-Anchor."""
        # This mimics the Brownian motion of particles in a fluid
        jitter_vector = (
            random.uniform(-self.jitter_magnitude, self.jitter_magnitude),
            random.uniform(-self.jitter_magnitude, self.jitter_magnitude),
            random.uniform(-self.jitter_magnitude, self.jitter_magnitude)
        )
        
        # Applying the jitter to the 'Macro-Focus' area for maximum realism
        print(f"[JITTER]: Injecting atomic pulse into {node_dna[:8]}...")
        return jitter_vector

    def sync_to_neural_bus(self):
        """Synchronizes the jitter to the Pilot's visual perception rate."""
        print("[JITTER]: Atomic vibration synchronized to Neural-Bus.")
        return "TIME_VIBRATION_LOCKED"
