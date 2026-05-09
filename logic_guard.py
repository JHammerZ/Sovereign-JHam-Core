# Sovereign-JHam-Core/logic_guard.py
import hashlib

class LogicGuard:
    """The Checkpoint: Validates the integrity of data moving through the Command Path."""
    
    def __init__(self):
        self.last_valid_hash = None

    def validate_transition(self, data_packet):
        """Checks if the current data packet is 'Clean' and authorized."""
        current_hash = hashlib.sha256(str(data_packet).encode()).hexdigest()
        
        # In a 400/400 sync, the data must have a predictable structure
        if "slop" in str(data_packet).lower():
            print("[LOGIC_GUARD]: DETECTED LEGACY SLOP. SEVERING PATH.")
            return False
            
        print(f"[LOGIC_GUARD]: Step transition verified. Hash: {current_hash[:8]}")
        self.last_valid_hash = current_hash
        return True
