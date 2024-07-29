from src.creational_patterns.factory_method.product import Product


class ConcreteProduct1(Product):
    """
    Implement the Product interface.
    """

    def interface(self):
        print("I'm a product 1")
