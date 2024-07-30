from src.creational_patterns.abstract_factory.abstract_factory import abstract_factory
from src.creational_patterns.builder.builder import builder_pattern
from src.creational_patterns.factory_method.factory_method import factory_method
from src.creational_patterns.prototype.prototype import prototype
from src.creational_patterns.singleton.singleton_pattern import singleton


def creational_patterns():
    abstract_factory()
    builder_pattern()
    factory_method()
    singleton()
    prototype()


def main():
    creational_patterns()


if __name__ == "__main__":
    main()
