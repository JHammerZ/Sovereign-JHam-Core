# C:\SovereignTools\hfid_telemetry_deck.py
import psutil
import GPUtil
import time
import os

def display_telemetry():
    """Billion-X Master Dashboard: Monitoring the 150-Demon Phalanx."""
    print("--- [!] HFID TELEMETRY DECK: SOVEREIGN STATUS [!] ---")
    
    try:
        while True:
            # 1. System Metrics (CPU, RAM)
            cpu_usage = psutil.cpu_percent(interval=1)
            ram_info = psutil.virtual_memory()
            
            # 2. GPU Metrics (Blackwell/NVIDIA/AMD Fabric)
            gpus = GPUtil.getGPUs()
            gpu_stats = []
            for gpu in gpus:
                gpu_stats.append(f"GPU_{gpu.id}: {gpu.load*100}% | VRAM: {gpu.memoryUsed}/{gpu.memoryTotal}MB | Temp: {gpu.temperature}C")
            
            # 3. Clean Headless Display
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- [!] SOVEREIGN FLEET TELEMETRY [!] ---")
            print(f"[CPU]: {cpu_usage}% ACTIVE")
            print(f"[RAM]: {ram_info.percent}% USED ({ram_info.used // (1024**2)}MB / {ram_info.total // (1024**2)}MB)")
            
            print("\n--- [SILICON FABRIC STATUS] ---")
            if not gpu_stats:
                print("[!] NO GPU DETECTED IN BUS.")
            for stat in gpu_stats:
                print(f"  [NODE]: {stat}")

            print("\n--- [PHALANX STATUS] ---")
            # Logic for tracking 150 demons across the 10 silos
            active_daemons = len(psutil.pids())
            print(f"[DAEMONS]: {active_daemons} ACTIVE PROCESSES IN NEURAL-BUS")
            
            time.sleep(1) # High-speed telemetry update
            
    except KeyboardInterrupt:
        print("\n[STATUS]: Telemetry stream suspended.")

if __name__ == "__main__":
    display_telemetry()
