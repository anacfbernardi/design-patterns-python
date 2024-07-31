from src.structural_patterns.bridge.implementor import Implementor


class ConcreteImplementorA(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def operation_imp(self):
        print("Concrete implementor A")
