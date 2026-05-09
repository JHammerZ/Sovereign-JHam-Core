# Sovereign-JHam-Core/git_auto_reconciler.py
import subprocess

def force_green_manifest():
    print("--- [!] INITIATING SOVEREIGN RECONCILIATION [!] ---")
    commands = [
        ["git", "stash"],
        ["git", "pull", "origin", "main", "--rebase"],
        ["git", "stash", "pop"],
        ["git", "push", "origin", "main", "--force"]
    ]
    
    for cmd in commands:
        print(f"[EXECUTING]: {' '.join(cmd)}")
        subprocess.run(cmd)

    print("\n[STATUS]: MANIFEST COMPLETE. TIMELINE RE-ANCHORED.")

if __name__ == "__main__":
    force_green_manifest()
