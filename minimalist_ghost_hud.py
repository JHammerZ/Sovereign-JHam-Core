# Sovereign-JHam-Core/minimalist_ghost_hud.py

class GhostHUD:
    """The 'Whispering' HUD: Information only when Intent calls for it."""
    
    def __init__(self):
        self.is_visible = False
        self.opacity = 0.0

    def whisper_intel(self, context_dna):
        """Manifests minimalist telemetry based on player focus."""
        print(f"[HUD]: Projecting ghost-telemetry for {context_dna}...")
        # Clean, vector-based lines that vanish the moment you look away.
        return "CONTEXT_REVEALED"
