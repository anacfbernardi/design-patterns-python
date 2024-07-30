class Adaptee:
    """
    Define an existing interface that needs adapting.
    """

    def specific_request(self, request_item: int):
        request_result = request_item * 2
        print(f"request_result: {request_result}")
