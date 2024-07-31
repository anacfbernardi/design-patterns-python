from src.structural_patterns.composite.component import Component


class Leaf(Component):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """

    def operation(self):
        print(f"operation no. {id(self)}")
