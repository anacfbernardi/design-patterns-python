from src.creational_patterns.abstract_factory.product.abstract_product_a import AbstractProductA

class ConcreteProductA2(AbstractProductA):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_a(self):
        print("I'm a product type A model 2")