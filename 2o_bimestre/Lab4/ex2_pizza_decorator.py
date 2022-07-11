class PizzaComponent():
    def get_description(self) -> str:
        return self.__class__.__name__

    def get_total_cost(self) -> float:
        return self.__class__.cost


class Dough(PizzaComponent):
    cost = 0.0


class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent: PizzaComponent) -> None:
        self.component = pizzaComponent

    def get_total_cost(self) -> float:
        return self.component.get_total_cost() + PizzaComponent.get_total_cost(self)

    def get_description(self) -> str:
        return self.component.get_description() + " " + PizzaComponent.get_description(self)


class TomatoSauce(Decorator):
    cost = 0.20

    def __init__(self, pizzaComponent: PizzaComponent) -> None:
        super().__init__(pizzaComponent)


class Mozzarella(Decorator):
    cost = 1.50

    def __init__(self, pizzaComponent: PizzaComponent) -> None:
        super().__init__(pizzaComponent)


class Gorgonzola(Decorator):
    cost = 3.50

    def __init__(self, pizzaComponent: PizzaComponent) -> None:
        super().__init__(pizzaComponent)


class Parmesan(Decorator):
    cost = 2.50

    def __init__(self, pizzaComponent: PizzaComponent) -> None:
        super().__init__(pizzaComponent)


class Ricotta(Decorator):
    cost = 2.00

    def __init__(self, pizzaComponent: PizzaComponent) -> None:
        super().__init__(pizzaComponent)


def create_menu(pizza: PizzaComponent, name: str) -> None:
    print(name)
    print(pizza.get_description())
    print(f"U$ {pizza.get_total_cost():.2f}")


if __name__ == "__main__":
    pizza = Dough()
    pizza = TomatoSauce(pizza)
    pizza = Mozzarella(pizza)
    pizza = Gorgonzola(pizza)
    pizza = Parmesan(pizza)
    pizza = Ricotta(pizza)

    create_menu(pizza, "Quattro Formaggi")


""" OUTPUT
Quattro Formaggi
Dough TomatoSauce Mozzarella Gorgonzola Parmesan Ricotta
U$ 9.70
"""
