import os
import mmap
import json
import time
import struct

class HardwareBridgeIPC:
    def __init__(self, tag="sovereign_hw_bridge", size=1024):
        self.tag = tag
        self.size = size
        self.shm_path = f"/dev/shm/{self.tag}" if os.name != 'nt' else f"C:\\SovereignTools\\{self.tag}.dat"
        self._initialize_buffer()

    def _initialize_buffer(self):
        """Creates or opens the physical memory-mapped allocation block."""
        if not os.path.exists(self.shm_path):
            with open(self.shm_path, "wb") as f:
                f.write(b'\x00' * self.size)
        
        self.file_obj = open(self.shm_path, "r+b")
        self.shm = mmap.mmap(self.file_obj.fileno(), self.size)

    def write_hardware_metrics(self, cpu_load: float, memory_util: float, thread_count: int):
        """
        Pipes raw metrics into the memory map using a packed binary structure 
        to ensure zero string-parsing latency for the daemons.
        """
        self.shm.seek(0)
        # Pack format: d (double/float), d (double/float), i (int)
        payload = struct.pack("ddi", cpu_load, memory_util, thread_count)
        self.shm.write(payload)
        # Pad the remainder with null bytes to prevent corruption
        self.shm.write(b'\x00' * (self.size - len(payload)))

    def read_hardware_metrics(self) -> dict:
        """Reads and unpacks the raw memory block instantly for the MAS Orchestrator."""
        self.shm.seek(0)
        data = self.shm.read(struct.calcsize("ddi"))
        if not data or data == b'\x00' * len(data):
            return {"cpu": 0.0, "memory": 0.0, "daemons_active": 0}
        
        cpu_load, memory_util, thread_count = struct.unpack("ddi", data)
        return {
            "cpu": round(cpu_load, 2),
            "memory": round(memory_util, 2),
            "daemons_active": thread_count,
            "timestamp": time.time()
        }

    def close(self):
        self.shm.close()
        self.file_obj.close()

if __name__ == "__main__":
    # Internal test execution
    bridge = HardwareBridgeIPC()
    print("IPC Memory Map initialized safely. Awaiting parallel stream input.")
