import abc

class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def interface_a(self):
        pass