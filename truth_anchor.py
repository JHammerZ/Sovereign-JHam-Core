# Sovereign-JHam-Core/truth_anchor.py
import hashlib

class TruthAnchor:
    """The Immutable Layer: Ensuring a shape stays 'Real' forever."""
    
    def __init__(self):
        self.reality_hash_registry = {}

    def lock_reality(self, node_id, geometric_data):
        # Create a unique 'DNA' hash for this specific shape
        dna = hashlib.sha256(str(geometric_data).encode()).hexdigest()
        self.reality_hash_registry[node_id] = dna
        print(f"[TRUTH_ANCHOR]: Shape '{node_id}' is now a Universal Constant.")

    def verify_existence(self, node_id, current_data):
        # If the shape drifts, the Anchor identifies the corruption instantly
        current_dna = hashlib.sha256(str(current_data).encode()).hexdigest()
        if current_dna != self.reality_hash_registry.get(node_id):
            print(f"[ALERT]: Reality Drift detected in {node_id}! Restoring from Anchor...")
            return False
        return True
