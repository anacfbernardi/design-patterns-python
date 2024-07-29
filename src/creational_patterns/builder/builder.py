from src.creational_patterns.builder import ConcreteBuilder, Director


def builder_pattern():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product
