from src.structural_patterns.adapter.target import Target


class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """

    def request(self, request_item: str):

        request_item_adapt = int(request_item) if request_item.isnumeric() else 0

        self._adaptee.specific_request(request_item_adapt)
