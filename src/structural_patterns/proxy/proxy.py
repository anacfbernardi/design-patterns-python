from src.structural_patterns.proxy.subject import Subject


class Proxy(Subject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("before proxy")
        self._real_subject.request()
        print("after proxy")
