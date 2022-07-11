from __future__ import annotations
from abc import ABC, abstractmethod


class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def get_vehicle(self) -> Car:
        return Car()


class TruckFactory(VehicleFactory):
    def get_vehicle(self) -> Truck:
        return Truck()


class Vehicle(ABC):
    @abstractmethod
    def honk(self) -> None:
        pass

    def set_engine(self, engine: Engine) -> None:
        self.engine = engine


class Truck(Vehicle):
    def honk(self) -> None:
        print(f"BEEEEEP it's me, the {self.engine.get_engine()} Truck!")


class Car(Vehicle):
    def honk(self) -> None:
        print(f"Beep beep it's me, the {self.engine.get_engine()} Car!")


class Engine(ABC):
    @abstractmethod
    def get_engine(self) -> str:
        pass


class ElectricEngine(Engine):
    def get_engine(self) -> str:
        return "Electric"


class HybridEngine(Engine):
    def get_engine(self) -> str:
        return "Hybrid"


class CombustionEngine(Engine):
    def get_engine(self) -> str:
        return "Combustion"


if __name__ == "__main__":
    vehicle = CarFactory().get_vehicle()
    engine = ElectricEngine()
    vehicle.set_engine(engine)
    vehicle.honk()

    print("")

    vehicle =TruckFactory().get_vehicle()
    engine = HybridEngine()
    vehicle.set_engine(engine)
    vehicle.honk()


""" OUTPUT
Beep beep it's me, the Electric Car!

BEEEEEP it's me, the Hybrid Truck!
"""
