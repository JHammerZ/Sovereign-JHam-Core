# Sovereign-JHam-Core/foundation.py

class JHamNode:
    """The base atom of the .JHam reality."""
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

class Point(JHamNode):
    """A Node representing a fixed value or coordinate."""
    def __init__(self, value):
        super().__init__("POINT")
        self.value = value

class Vector(JHamNode):
    """A Node representing movement or transformation."""
    def __init__(self, magnitude):
        super().__init__("VECTOR")
        self.magnitude = magnitude

class Anchor(JHamNode):
    """A Node representing a logic gate or decision."""
    def __init__(self, condition):
        super().__init__("ANCHOR")
        self.condition = condition
