from src.creational_patterns.singleton.my_class import MyClass

def singleton():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2
    m1.print_instance()
    m2.print_instance()