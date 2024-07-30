from src.structural_patterns.adapter.adapter import Adapter


def adapter_method():
    adapter = Adapter()
    for i in ("1", "aaa", "3"):
        adapter.request(i)
