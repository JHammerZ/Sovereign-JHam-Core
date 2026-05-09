#!/bin/bash
# Sovereign-JHam-Core/shell_entrypoint.sh
echo "--- IGNITING SOVEREIGN AI SHELL ---"
python3 sovereign_daemon.py & # Start background persistence
python3 genesis_manifest.py "Anchor the Shell and Expand 1000"
echo "[SYSTEM]: Cockpit ready for LYSANDER_UNIT occupancy."
