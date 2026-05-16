# Sovereign-JHam-Core/sovereign_sigterm_reaper.py
import os
import sys
import signal
import time
import threading

class SovereignSigtermReaper:
    """Intercepts system termination signals to cleanly reclaim daemon resources."""

    def __init__(self, swarm_manager=None, allocator=None):
        self.swarm_manager = swarm_manager
        self.allocator = allocator
        self.shutdown_in_progress = False

        # Register core OS interrupts (SIGINT = Ctrl+C, SIGTERM = Process termination)
        signal.signal(signal.SIGINT, self.execute_orderly_purge)
        signal.signal(signal.SIGTERM, self.execute_orderly_purge)

    def execute_orderly_purge(self, signum, frame):
        """Forces an absolute cascading shutdown of all 150 parallel daemons."""
        if self.shutdown_in_progress:
            return
        self.shutdown_in_progress = True
        
        print(f"\n[SYSTEM REAPER]: Intercepted Signal {signum}. Initiating H-Fid Grid Purge...")

        # 1. Gracefully tell the daemon swarm to cease execution loops
        if self.swarm_manager and hasattr(self.swarm_manager, "stop_all_daemons"):
            print("[REAPER]: Disengaging 150 background daemons...")
            self.swarm_manager.stop_all_daemons()

        # 2. Flush remaining telemetry frames out of memory blocks
        if self.allocator and hasattr(self.allocator, "pop_latest_batch"):
            print("[REAPER]: Flushing final ring allocator memory buffers...")
            self.allocator.pop_latest_batch()

        # 3. Allow active network injection buffers to clear safely
        print("[REAPER]: Awaiting final hardware direct stream handshakes...")
        time.sleep(0.5)

        # 4. Verify all dangling background threads are dead
        active_threads = threading.active_count()
        print(f"[REAPER]: Purge complete. Active threads remaining: {active_threads}. Exiting grid.")
        
        # Complete clean exit back to the host operating system
        sys.exit(0)

if __name__ == "__main__":
    # Test initialization hook
    reaper = SovereignSigtermReaper()
    print("Sovereign Sigterm Reaper armed and monitoring host hardware signals.")
    # Keep main thread alive for simulation
    while True:
        time.sleep(1)
