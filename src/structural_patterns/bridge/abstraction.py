"""
Decouple an abstraction from its implementation so that the two can vary
independently.
"""

from src.structural_patterns.bridge.implementor import Implementor


class Abstraction:
    """
    Define the abstraction's interface.
    Maintain a reference to an object of type Implementor.
    """

    def __init__(self, imp: Implementor):
        self._imp = imp

    def operation(self):
        self._imp.operation_imp()
