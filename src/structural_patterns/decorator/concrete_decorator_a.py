from src.structural_patterns.decorator.decorator import Decorator


class ConcreteDecoratorA(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        print("concrete decorator B - Before")
        self._component.operation()
        print("concrete decorator B - After")
