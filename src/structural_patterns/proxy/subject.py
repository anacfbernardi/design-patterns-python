"""
Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.
"""

import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def request(self):
        pass
