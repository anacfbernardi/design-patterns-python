from src.creational_patterns import abstract_factory, builder_pattern, factory_method, prototype, singleton

from src.structural_patterns.adapter.adapter_method import adapter_method


def creational_patterns():
    abstract_factory()
    builder_pattern()
    factory_method()
    singleton()
    prototype()

def structural_patterns():
    adapter_method()

def main():
    print("======creational_patterns======")
    creational_patterns()
    print("======structural_patterns======")
    structural_patterns()

if __name__ == "__main__":
    main()
