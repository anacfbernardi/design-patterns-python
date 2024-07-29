from src.creational_patterns.abstract_factory.product.abstract_product_b import AbstractProductB

class ConcreteProductB2(AbstractProductB):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def interface_b(self):
        print("I'm a product type B model 2")