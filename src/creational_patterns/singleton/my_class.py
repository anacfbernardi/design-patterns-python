from src.creational_patterns.singleton.singleton import Singleton


class MyClass(metaclass=Singleton):
    """
    Example class.
    """

    def print_instance(self):
        instance_id = id(self)
        print(f"Instance ID: {instance_id}")
