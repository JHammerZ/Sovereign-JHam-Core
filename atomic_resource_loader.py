# Sovereign-JHam-Core/atomic_resource_loader.py
import os
import mmap

class AtomicLoader:
    """The Ground-Up Data Pipe: Zero-Copy Memory Mapping."""
    
    def __init__(self):
        self.active_buffer = {}

    def mount_resource(self, file_path):
        """Uses Memory Mapping (mmap) to link files directly to RAM."""
        # This bypasses the slow 'Read/Write' OS calls
        fd = os.open(file_path, os.O_RDONLY)
        buf = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
        print(f"[LOADER]: Atomic Link established for {file_path}")
        return buf

    def stream_packet(self, buffer, offset, size):
        """Injects a specific 'Atom' of data into the Neural-Bus."""
        # No 'Loading Screen' because the data is already mapped to memory
        return buffer[offset:offset+size]
