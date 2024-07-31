"""
Compose objects into tree structures to represent part-whole
hierarchies. Composite lets clients treat individual objects and
compositions of objects uniformly.
"""

import abc


class Component(metaclass=abc.ABCMeta):
    """
    Declare the interface for objects in the composition.
    Implement default behavior for the interface common to all classes,
    as appropriate.
    Declare an interface for accessing and managing its child
    components.
    Define an interface for accessing a component's parent in the
    recursive structure, and implement it if that's appropriate
    (optional).
    """

    @abc.abstractmethod
    def operation(self):
        pass
