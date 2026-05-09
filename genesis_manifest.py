# Sovereign-JHam-Core/genesis_manifest.py
from linguistic_mapper import LinguisticMapper
from architect import Architect
from geometry_engine import GeometryEngine
from universal_adapter import UniversalAdapter

def speak_existence(command):
    print(f"\n[PILOT VOICE]: \"{command}\"")
    
    # 1. Translate Word to Intent
    mapper = LinguisticMapper()
    intent = mapper.translate_intent(command)
    
    # 2. Build the Logic Tree
    arch = Architect()
    tree = arch.build_sequence(intent)
    
    # 3. Project to Geometry
    geo = GeometryEngine()
    for node in tree.children:
        geo.project_to_form(node)
    
    # 4. Universal Export (Legacy Adaptability)
    adapter = UniversalAdapter()
    schema = adapter.export_to_gltf_schema(geo.get_all_forms())
    
    print("[SYSTEM]: Word has been rendered into Geometric Schema.")
    print(schema)

if __name__ == "__main__":
    # Our first act of linguistic creation
    speak_existence("Anchor the sanctuary and expand 500")
