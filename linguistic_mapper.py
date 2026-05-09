# Sovereign-JHam-Core/linguistic_mapper.py

class LinguisticMapper:
    """The Translator: Maps spoken intent to Geometric AST Nodes."""
    
    def __init__(self):
        # The 'Sovereign Vocabulary'
        self.lexicon = {
            "anchor": "ANCHOR",
            "expand": "VECTOR",
            "shield": "LOCK",
            "pulse": "PULSE"
        }

    def translate_intent(self, spoken_command):
        """
        Example: 'Anchor the origin and expand by 500' 
        becomes .JHam AST instructions.
        """
        words = spoken_command.lower().split()
        directives = []
        
        for i, word in enumerate(words):
            if word in self.lexicon:
                type_key = self.lexicon[word]
                # Look ahead for a magnitude/value if it exists
                val = 1.0
                if i + 1 < len(words) and words[i+1].isdigit():
                    val = float(words[i+1])
                
                directives.append({'type': type_key, 'val': val})
        
        return directives
