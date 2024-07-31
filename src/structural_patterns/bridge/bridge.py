from src.structural_patterns.bridge.abstraction import Abstraction
from src.structural_patterns.bridge.concrete_implementor_a import ConcreteImplementorA
from src.structural_patterns.bridge.concrete_implementor_b import ConcreteImplementorB


def bridge_method():
    concrete_implementor_a = ConcreteImplementorA()
    concrete_implementor_b = ConcreteImplementorB()
    abstraction = Abstraction(concrete_implementor_a)
    abstraction.operation()

    abstraction = Abstraction(concrete_implementor_b)
    abstraction.operation()
