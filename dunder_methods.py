from typing import Any


class Human:
    """
    python dunder methods practice
    """
    def __init__(self, age, name) -> Any:
        self.name = name
        self.age = age


object1: Human = Human(
    name='Gustavo',
    age=27
)
