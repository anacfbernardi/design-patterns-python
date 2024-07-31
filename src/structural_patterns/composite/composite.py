from src.structural_patterns.composite.component import Component


class Composite(Component):
    """
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Component interface.
    """

    def __init__(self):
        self._children = set()

    def operation(self):
        for child in self._children:
            child.operation()

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)
