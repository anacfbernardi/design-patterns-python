from src.creational_patterns.factory_method.creator import Creator
from src.creational_patterns.factory_method.product import ConcreteProduct1


class ConcreteCreator1(Creator):
    """
    Override the factory method to return an instance of a
    ConcreteProduct1.
    """

    def _factory_method(self):
        return ConcreteProduct1()
