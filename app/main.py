from abc import ABC


class IntegerRange:
    def __init__(self, min_amount: int,
                 max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner: type[object],
                     name: str) -> None:
        self.protect_name = "_" + name

    def __get__(self, instance: object,
                owner: type[object]) -> int:
        return getattr(instance, self.protect_name)

    def __set__(self, instance: object,
                value: int) -> None:
        if self.min_amount <= value <= self.max_amount:
            setattr(instance, self.protect_name, True)
        else:
            setattr(instance, self.protect_name, False)


class Visitor:
    def __init__(self, name: str,
                 age: int,
                 weight: int,
                 height: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self, age: int,
                 height: int,
                 weight: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(4, 14)
    height = IntegerRange(80, 120)
    weight = IntegerRange(20, 50)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(14, 60)
    height = IntegerRange(120, 220)
    weight = IntegerRange(50, 120)


class Slide:
    def __init__(self, name: str,
                 limitation_class: type[SlideLimitationValidator]) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_access(self, visitor: Visitor) -> bool:
        result = self.limitation_class(visitor.age,
                                       visitor.height,
                                       visitor.weight)
        return all((result.age, result.weight, result.height))
