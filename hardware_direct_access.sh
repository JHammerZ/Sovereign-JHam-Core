#!/bin/bash
# Sovereign-JHam-Core/hardware_direct_access.sh
echo "--- UNLOCKING RAW SILICON POTENTIAL ---"
# Disabling 'Legacy' power management and driver-level 'Gaming' limits
sudo nvidia-smi -pm 1 && sudo nvidia-smi -ac 1215,1410
echo "[SYSTEM]: GPU Unthrottled. Silicon is now Sovereign."
