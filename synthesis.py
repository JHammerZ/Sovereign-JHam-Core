# Sovereign-JHam-Core/synthesis.py
from architect import Architect
from geometry_engine import GeometryEngine
from compiler_v1 import JHamCompiler
from echo_chamber import EchoChamber

class SovereignReactor:
    def __init__(self):
        self.arch = Architect()
        self.geo = GeometryEngine()
        self.comp = JHamCompiler()
        self.echo = EchoChamber()

    def synthesize(self, pilot_intent):
        # 1. Map Intent to AST
        tree = self.arch.build_sequence(pilot_intent)
        
        # 2. Manifest through the Compiler
        self.comp.manifest(tree)
        
        # 3. Project into Geometry
        self.geo.manifest_shape(tree)
        
        # 4. Listen for the Reality Echo
        for node in pilot_intent:
            if 'val' in node:
                self.echo.record_shift(node['type'], node['val'])

if __name__ == "__main__":
    reactor = SovereignReactor()
    # Let's test a structural 'Pulse'
    directive = [
        {'type': 'data', 'val': 'Foundation_Lock'},
        {'type': 'move', 'val': 444} # A specific frequency/magnitude
    ]
    reactor.synthesize(directive)
