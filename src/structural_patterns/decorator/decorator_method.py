from src.structural_patterns.decorator.concrete_component import ConcreteComponent
from src.structural_patterns.decorator.concrete_decorator_a import ConcreteDecoratorA
from src.structural_patterns.decorator.concrete_decorator_b import ConcreteDecoratorB


def decorator_method():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()
