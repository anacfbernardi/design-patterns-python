from src.structural_patterns.composite.composite import Composite
from src.structural_patterns.composite.leaf import Leaf


def composite_method():
    leaf_1 = Leaf()
    leaf_2 = Leaf()
    composite = Composite()
    composite.add(leaf_1)
    composite.add(leaf_2)
    composite.operation()
