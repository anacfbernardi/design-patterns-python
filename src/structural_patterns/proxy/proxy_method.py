from src.structural_patterns.proxy.proxy import Proxy
from src.structural_patterns.proxy.real_subject import RealSubject


def proxy_method():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()
