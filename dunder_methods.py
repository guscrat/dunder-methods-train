from typing import Any


class Human:
    """
    python dunder methods practice
    """
    def __init__(self, age, name) -> Any:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        pass


