from src.creational_patterns.factory_method.creator import Creator
from src.creational_patterns.factory_method.product import ConcreteProduct2


class ConcreteCreator2(Creator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct2.
    """

    def _factory_method(self):
        return ConcreteProduct2()
