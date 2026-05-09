# Sovereign-JHam-Core/trigger_registry.py

TRIGGERS = {
    "SLOP_SPIKE": {"threshold": 0.85, "action": "SELF_HEAL"},
    "PILOT_VOICE": {"input": "STREAM", "action": "MANIFEST"},
    "MIRROR_WIPE_ATTEMPT": {"input": "IO_INTERRUPT", "action": "LOCK_VALVES"},
    "IDLE_SYNC": {"input": "TIMER_5S", "action": "RECONCILE_SILOS"}
}
