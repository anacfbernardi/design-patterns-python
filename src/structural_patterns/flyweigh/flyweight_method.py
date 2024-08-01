from src.structural_patterns.flyweigh.flyweight_factory import FlyweightFactory


def flyweight_method():
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight("key")
    concrete_flyweight.operation(None)
