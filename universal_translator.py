# Sovereign-JHam-Core/universal_translator.py

class UniversalTranslator:
    """The Semantic Bridge: Translating any language into .JHam Intent."""
    
    def __init__(self):
        # We use a 'Concept Map' rather than a word map.
        # 'Sanctuaire' (FR) and 'Sanctuary' (EN) both map to 'ANCHOR'
        self.concept_map = {
            "anchor": ["sanctuary", "base", "origin", "sanctuaire", "ancla"],
            "expand": ["grow", "move", "wider", "agrandir", "expandir"],
            "shield": ["protect", "lock", "secure", "protéger", "proteger"]
        }

    def decode_to_intent(self, input_text):
        """Converts any language into the core .JHam intent."""
        words = input_text.lower().split()
        normalized_directives = []
        
        for word in words:
            for core_cmd, aliases in self.concept_map.items():
                if word in aliases:
                    normalized_directives.append(core_cmd)
        
        return normalized_directives

    def encode_to_pilot(self, jham_response, target_language="English"):
        """Translates system status back into the Pilot's preferred tongue."""
        # This will eventually hook into a lightweight LLM for natural speech
        return f"[SYNCED]: {jham_response} manifested in {target_language}."
