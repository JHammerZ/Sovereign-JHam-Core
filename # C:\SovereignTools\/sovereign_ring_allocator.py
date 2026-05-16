# Sovereign-JHam-Core/sovereign_ring_allocator.py

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
