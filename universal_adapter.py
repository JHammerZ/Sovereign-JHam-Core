# Sovereign-JHam-Core/universal_adapter.py
import json

class UniversalAdapter:
    """Translates .JHam Geometry into Industry Standard 3D Data."""
    
    def __init__(self):
        self.manifest_log = []

    def export_to_gltf_schema(self, geometry_data):
        """
        Converts internal geometry mapping to a JSON schema 
        compatible with 3D Renderers (Blender/Three.js/Unreal).
        """
        schema = {
            "version": "1.0.JHAM",
            "entities": []
        }
        
        for item in geometry_data:
            # Mapping our 'form' to a standard 'mesh' or 'light'
            entity = {
                "type": item.get("type"),
                "coordinates": item.get("vertex", (0,0,0)),
                "scale": item.get("edge_length", 1.0)
            }
            schema["entities"].append(entity)
            
        return json.dumps(schema, indent=4)

    def broadcast_to_external(self, schema):
        print("[ADAPTER]: Broadcasting Geometric Intent to External Renderers...")
        # In a real sync, this would be a socket or file-write
        print(f"[DATA_STREAM]: {schema}")
