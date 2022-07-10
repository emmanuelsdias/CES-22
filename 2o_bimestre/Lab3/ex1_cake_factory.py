from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCakeFactory(ABC):
    @abstractmethod
    def create_chocolate_cake(self) -> ChocolateCake:
        pass

    @abstractmethod
    def create_manioc_cake(self) -> ManiocCake:
        pass

    @abstractmethod
    def create_carrot_cake(self) -> CarrotCake:
        pass


class BirthdayCakeFactory(AbstractCakeFactory):
    def create_chocolate_cake(self) -> ChocolateCake:
        return ChocolateCake("Birthday")

    def create_manioc_cake(self) -> ManiocCake:
        return ManiocCake("Birthday")

    def create_carrot_cake(self) -> CarrotCake:
        return CarrotCake("Birthday")


class WeddingCakeFactory(AbstractCakeFactory):
    def create_chocolate_cake(self) -> ChocolateCake:
        return ChocolateCake("Wedding")

    def create_manioc_cake(self) -> ManiocCake:
        return ManiocCake("Wedding")

    def create_carrot_cake(self) -> CarrotCake:
        return CarrotCake("Wedding")


class InformalCakeFactory(AbstractCakeFactory):
    def create_chocolate_cake(self) -> ChocolateCake:
        return ChocolateCake("Informal")

    def create_manioc_cake(self) -> ManiocCake:
        return ManiocCake("Informal")

    def create_carrot_cake(self) -> CarrotCake:
        return CarrotCake("Informal")


class AbstractCake(ABC):
    @abstractmethod
    def __init__(self, style: str) -> None:
        pass

    @abstractmethod
    def get_flavor(self) -> str:
        pass

    @abstractmethod
    def get_style(self) -> str:
        pass

    @abstractmethod
    def what_kind_of_cake(self) -> str:
        pass


class ChocolateCake(AbstractCake):
    def __init__(self, style: str) -> None:
        self.flavor = self.get_flavor()
        self.style = style

    def get_flavor(self) -> str:
        return "Chocolate"

    def get_style(self) -> str:
        return self.style

    def what_kind_of_cake(self) -> str:
        return f"Im a {self.get_flavor()} cake made in a {self.get_style()} style!"


class ManiocCake(AbstractCake):
    def __init__(self, style: str) -> None:
        self.flavor = self.get_flavor()
        self.style = style

    def get_flavor(self) -> str:
        return "Manioc"

    def get_style(self) -> str:
        return self.style

    def what_kind_of_cake(self) -> str:
        return f"Im a {self.get_flavor()} cake made in a {self.get_style()} style!"


class CarrotCake(AbstractCake):
    def __init__(self, style: str) -> None:
        self.flavor = self.get_flavor()
        self.style = style

    def get_flavor(self) -> str:
        return "Carrot"

    def get_style(self) -> str:
        return self.style

    def what_kind_of_cake(self) -> str:
        return f"Im a {self.get_flavor()} cake made in a {self.get_style()} style!"


def client_code(factory: AbstractCakeFactory) -> None:
    """
    Produce all available flavors of cakes in a specific style.
    """
    chocolate_cake = factory.create_chocolate_cake()
    manioc_cake = factory.create_manioc_cake()
    carrot_cake = factory.create_carrot_cake()

    print(chocolate_cake.what_kind_of_cake())
    print(manioc_cake.what_kind_of_cake())
    print(carrot_cake.what_kind_of_cake())


if __name__ == "__main__":
    print("Testing client code with the Wedding Cake style:")
    client_code(WeddingCakeFactory())


""" OUTPUT
Testing client code with the Wedding Cake style:
Im a Chocolate cake made in a Wedding style!
Im a Manioc cake made in a Wedding style!
Im a Carrot cake made in a Wedding style!
"""
