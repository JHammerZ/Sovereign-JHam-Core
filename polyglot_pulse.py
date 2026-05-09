# Sovereign-JHam-Core/polyglot_pulse.py
from universal_translator import UniversalTranslator
from synthesis import SovereignReactor

class PolyglotPulse:
    def __init__(self):
        self.translator = UniversalTranslator()
        self.reactor = SovereignReactor()

    def process_broadcast(self, broadcast_text, language="Auto"):
        print(f"[POLYGLOT]: Detecting language... Input: '{broadcast_text}'")
        intent = self.translator.decode_to_intent(broadcast_text)
        
        if intent:
            print(f"[POLYGLOT]: Intent identified as {intent}. Relaying to Reactor.")
            self.reactor.synthesize([{'type': cmd.upper(), 'val': 1.0} for cmd in intent])
        else:
            print("[POLYGLOT]: No valid geometric intent found in broadcast.")
