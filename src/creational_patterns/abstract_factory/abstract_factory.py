from src.creational_patterns.abstract_factory.factory import ConcreteFactory1, ConcreteFactory2


def abstract_factory():
    print("Factory Method")
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()
