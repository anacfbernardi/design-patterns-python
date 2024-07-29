from src.creational_patterns.abstract_factory.factory.abstract_factory import AbstractFactory
from src.creational_patterns.abstract_factory.product import ConcreteProductA1, ConcreteProductB1


class ConcreteFactory1(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()
