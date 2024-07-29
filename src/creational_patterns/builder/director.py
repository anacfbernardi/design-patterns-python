class Director:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()
