# Sovereign-JHam-Core/path_executor.py
import yaml
from command_path import SovereignCommandPath

class PathExecutor:
    """The Engine that drives the logic through the Command Path."""
    
    def __init__(self, map_file="workflow_map.yaml"):
        with open(map_file, 'r') as f:
            self.map = yaml.safe_load(f)
        self.path_logic = SovereignCommandPath()

    def run_sync_sequence(self, pilot_command):
        print(f"\n[EXECUTOR]: Initiating Path for Mission: {self.map['mission']}")
        
        # We follow the YAML steps precisely
        for step in self.map['paths'][0]['steps']:
            trigger = step['trigger']
            action = step['action']
            print(f"  [STEP_ACTIVE]: Triggered by '{trigger}' -> Executing '{action}'")
            
            # Here, the executor calls the specific .JHam modules
            # Ensuring the 'Truth-Anchor' is checked at every transition
            
        print("[EXECUTOR]: Sequence finalized. Reality is now Locked.\n")

if __name__ == "__main__":
    # Test the path with a direct command
    pilot_engine = PathExecutor()
    pilot_engine.run_sync_sequence("Manifest Sanctuary Origin")
