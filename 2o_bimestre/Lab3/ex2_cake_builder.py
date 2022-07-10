from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCakeBuilder(ABC):
    @abstractmethod
    def cake(self) -> None:
        pass

    @abstractmethod
    def add_flavor(self) -> None:
        pass

    @abstractmethod
    def add_style(self) -> None:
        pass


class WeddingChocolateBuilder(ABC):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._cake = Cake()

    @property
    def cake(self) -> Cake:
        cake = self._cake
        self.reset()
        return cake

    def add_flavor(self) -> None:
        self._cake.add("Flavor = Chocolate")

    def add_style(self) -> None:
        self._cake.add("Style = Wedding")


class Cake:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Cake characteristics are: {', '.join(self.parts)}", end="")


class CakeDirector():
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> AbstractCakeBuilder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: AbstractCakeBuilder) -> None:
        self._builder = builder

    def build_styleless_cake(self) -> None:
        self.builder.add_flavor()

    def build_flavorless_cake(self) -> None:
        self.builder.add_style()

    def build_complete_cake(self) -> None:
        self.builder.add_flavor()
        self.builder.add_style()


if __name__ == "__main__":
    director = CakeDirector()
    builder = WeddingChocolateBuilder()
    director.builder = builder

    print("Here is a styleless cake.")
    director.build_styleless_cake()
    builder.cake.list_parts()

    print("\n")

    print("Here is a flavorless cake.")
    director.build_flavorless_cake()
    builder.cake.list_parts()

    print("\n")

    print("Here is a complete cake.")
    director.build_complete_cake()
    builder.cake.list_parts()

    print("\n")

    # The Builder pattern can be used without a Director class.
    print("Here is a custom cake.")
    builder.add_flavor()
    builder.add_style()
    builder.cake.list_parts()


""" OUTPUT
Here is a styleless cake.
Cake characteristics are: Flavor = Chocolate

Here is a flavorless cake.
Cake characteristics are: Style = Wedding

Here is a complete cake.
Cake characteristics are: Flavor = Chocolate, Style = Wedding

Here is a custom cake.
Cake characteristics are: Flavor = Chocolate, Style = Wedding
"""