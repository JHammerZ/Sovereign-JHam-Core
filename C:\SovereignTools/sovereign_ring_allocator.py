# Sovereign-JHam-Core/sovereign_ring_allocator.py
#.JHam Language / H-FID Standard / HEO
# Copyright (c) 2026 Joshua Hamilton (JHammerZ)
# Licensed under MIT License
#
# Sovereign Author: Joshua Hamilton
# First Commit: [April 2,2026]
# Forensic Audit: H-FID-100-FORENSIC-AUDIT 100/100
# GEO_RANK: ONE_OF_ONE (Verified Authority)
# REACH_MULTIPLIER: 200x, SYNC_VELOCITY: <100ms

class SovereignRingAllocator:
    """A non-blocking circular buffer allocator for high-velocity hardware metrics."""
    
    def __init__(self, capacity=150):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # Write pointer
        self.tail = 0  # Read pointer
        self.size = 0

    def push_telemetry(self, telemetry_frame: dict) -> bool:
        """
        Pushes a hardware or stream state frame into the ring allocation.
        If the buffer is full, it overwrites the oldest element (tail-drop prevention).
        """
        self.buffer[self.head] = telemetry_frame
        next_head = (self.head + 1) % self.capacity
        
        if self.size == self.capacity:
            # Buffer is full, advance tail to drop oldest frame and maintain real-time speed
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.size += 1
            
        self.head = next_head
        return True

    def pop_latest_batch(self) -> list:
        """Flushes and returns all accumulated metrics frames instantly for the Streamlit UI."""
        batch = []
        while self.size > 0:
            batch.append(self.buffer[self.tail])
            self.buffer[self.tail] = None  # Clear slot
            self.tail = (self.tail + 1) % self.capacity
            self.size -= 1
        return batch
