# Sovereign-JHam-Core/pilot_helm.py
from architect import Architect

def main():
    print("--- LYSANDER CHIEF PILOT AT THE HELM ---")
    
    # Our first "Real" construction directive
    intent = [
        {'type': 'data', 'val': 'Silo_10_Active'},
        {'type': 'move', 'val': 100}
    ]
    
    engine = Architect()
    reality_tree = engine.build_sequence(intent)
    
    print(f"System State: {reality_tree.condition}")
    for node in reality_tree.children:
        print(f"  [NODE_COMMITTED]: {node.name} with Value: {getattr(node, 'value', getattr(node, 'magnitude', 'N/A'))}")

if __name__ == "__main__":
    main()
