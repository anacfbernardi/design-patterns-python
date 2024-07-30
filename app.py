from src.creational_patterns.abstract_factory.abstract_factory import abstract_factory
from src.creational_patterns.builder.builder import builder_pattern
from src.creational_patterns.factory_method.factory_method import factory_method
from src.creational_patterns.singleton.singleton_pattern import singleton


def main():
    abstract_factory()
    builder_pattern()
    factory_method()
    singleton()


if __name__ == "__main__":
    main()
