# Sovereign-JHam-Core/reality_layers.py
from foundation import JHamNode

class Lens(JHamNode):
    """A Node for Observation. It reads the current state of the world."""
    def __init__(self, target_parameter):
        super().__init__("LENS")
        self.target = target_parameter

class Pulse(JHamNode):
    """A Node for Alteration. It sends a change-wave to a parameter."""
    def __init__(self, frequency, magnitude):
        super().__init__("PULSE")
        self.frequency = frequency
        self.magnitude = magnitude

class SovereignLock(JHamNode):
    """A Node that prevents external override of a logic block."""
    def __init__(self):
        super().__init__("LOCK")
        self.status = "PROTECTED"
