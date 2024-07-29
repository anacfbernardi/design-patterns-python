from src.creational_patterns.builder.abstract_builder import Builder


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def produce_part_a(self) -> None:
        self.product.add("PartA1")

    def produce_part_b(self) -> None:
        self.product.add("PartB1")

    def produce_part_c(self) -> None:
        self.product.add("PartC1")
