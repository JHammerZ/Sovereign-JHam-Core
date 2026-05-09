# Sovereign-JHam-Core/silo_event_watcher.py

class SiloWatcher:
    """Watchdog that triggers the Translator when any silo is modified."""
    
    def on_modified(self, event):
        if not event.is_directory:
            print(f"[WATCHER]: Activity detected in {event.src_path}. Triggering Translation.")
            # This is where it feeds the change directly into the AutoTranslator
