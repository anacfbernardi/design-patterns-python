from src.creational_patterns.abstract_factory.factory.abstract_factory import AbstractFactory
from src.creational_patterns.abstract_factory.product import ConcreteProductA2, ConcreteProductB2

class ConcreteFactory2(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()