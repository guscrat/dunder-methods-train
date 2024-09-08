from typing import Any


class Human:
    """
    python dunder methods practice
    """
    def __init__(self, age, name) -> Any:
        self.name = name
        self.age = age

    def __setattr__(self, name: str, value: Any) -> None:
        if isinstance(value, str):
            value = value.upper()

        elif isinstance(value, int):
            pass

        super().__setattr__(name, value)

    def __getattr__(self, item):
        self.__dict__[item] = 0
        return 0


obj1: Human = Human(
    name='Gustavo',
    age=27
)

print(obj1.name)
print(obj1.wheith)
