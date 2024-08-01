from src.creational_patterns import abstract_factory, builder_pattern, factory_method, prototype, singleton
from src.structural_patterns import (
    adapter_method,
    bridge_method,
    composite_method,
    decorator_method,
    facade_method,
    flyweight_method,
)


def creational_patterns():
    abstract_factory()
    builder_pattern()
    factory_method()
    singleton()
    prototype()


def structural_patterns():
    adapter_method()
    bridge_method()
    composite_method()
    decorator_method()
    facade_method()
    flyweight_method()


def main():
    print("======creational_patterns======")
    creational_patterns()
    print("======structural_patterns======")
    structural_patterns()


if __name__ == "__main__":
    main()
