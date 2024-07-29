from src.creational_patterns.factory_method.creator import ConcreteCreator1


def factory_method():
    concrete_creator = ConcreteCreator1()
    concrete_creator.product.interface()
    concrete_creator.some_operation()
