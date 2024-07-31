from src.structural_patterns.decorator.decorator import Decorator


class ConcreteDecoratorB(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        print("concrete decorator A - Before")
        self._component.operation()
        print("concrete decorator A - After")
