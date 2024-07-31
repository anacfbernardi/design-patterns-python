from src.structural_patterns.decorator.component import Component


class ConcreteComponent(Component):
    """
    Define an object to which additional responsibilities can be
    attached.
    """

    def operation(self):
        print("concrete component")
