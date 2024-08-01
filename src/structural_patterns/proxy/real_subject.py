from src.structural_patterns.proxy.subject import Subject


class RealSubject(Subject):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        print(f"Real subject id{id(self)}")
