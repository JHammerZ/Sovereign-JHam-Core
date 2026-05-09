# Sovereign-JHam-Core/architect.py
from foundation import Point, Vector, Anchor

class Architect:
    def __init__(self):
        self.root = Anchor("INITIALIZE_REALITY")

    def build_sequence(self, instructions):
        """
        Converts a list of basic instructions into an AST.
        """
        for instr in instructions:
            if instr['type'] == 'data':
                self.root.add_child(Point(instr['val']))
            elif instr['type'] == 'move':
                self.root.add_child(Vector(instr['val']))
        return self.root
