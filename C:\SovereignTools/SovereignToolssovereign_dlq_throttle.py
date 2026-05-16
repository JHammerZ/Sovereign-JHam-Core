# Sovereign-JHam-Core/sovereign_dlq_throttle.py
import time
import collections

class SovereignDLQThrottle:
    """An asynchronous backpressure valve and Dead-Letter Queue (DLQ) for the swarm."""

    def __init__(self, failure_threshold=3, cooldown_period=5.0):
        self.failure_threshold = failure_threshold
        self.cooldown_period = cooldown_period
        
        # Dead-Letter Queue memory store for isolated, corrupted, or blocked payloads
        self.dead_letter_queue = collections.deque(maxlen=1000)
        
        # Track routing errors per destination to prevent cascading network failures
        self.endpoint_faults = collections.defaultdict(int)
        self.cooldown_timers = collections.defaultdict(float)

    def verify_route_health(self, endpoint: str) -> bool:
        """Checks if a target platform is currently in a defensive cooldown state."""
        current_time = time.time()
        if self.cooldown_timers[endpoint] > current_time:
            return False  # Route is throttled; tell the daemon to hold back pressure
        return True

    def log_route_transaction(self, endpoint: str, status_code: str) -> bool:
        """Logs transaction events and automatically drops gates if an anomaly triggers."""
        if status_code in ["SUCCESS", "BROADCAST_ACTIVE_100/100"]:
            self.endpoint_faults[endpoint] = 0
            return True

        # If a connection fails, increment fault status
        self.endpoint_faults[endpoint] += 1
        if self.endpoint_faults[endpoint] >= self.failure_threshold:
            # Drop the phalanx gate for this specific route to initiate isolation
            self.cooldown_timers[endpoint] = time.time() + self.cooldown_period
            print(f"[SECURITY ALERT]: Endpoint {endpoint} isolated for {self.cooldown_period}s.")
        return False

    def isolate_to_dlq(self, failed_agent_id: str, payload: dict, error_message: str):
        """Isolates corrupted tracking payloads away from the core memory fabric."""
        quarantine_record = {
            "agent_id": failed_agent_id,
            "timestamp": time.time(),
            "payload_dump": payload,
            "error": error_message
        }
        self.dead_letter_queue.append(quarantine_record)
        print(f"[DLQ QUARANTINE]: Agent {failed_agent_id} isolated a corrupted state.")

    def flush_dlq_for_analysis(self) -> list:
        """Returns all quarantined event failures for forensic audit tracking."""
        batch = []
        while self.dead_letter_queue:
            batch.append(self.dead_letter_queue.popleft())
        return batch
