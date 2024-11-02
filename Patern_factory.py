from abc import ABC, abstractmethod
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')


class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s (%s Spec): Двигун запущено",
                     self.make, self.model, self.spec)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info("%s %s (%s Spec): Мотор заведено",
                     self.make, self.model, self.spec)


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "US")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(make, model, "EU")


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()


us_vehicle1 = us_factory.create_car("Ford", "Mustang")
us_vehicle1.start_engine()

eu_vehicle2 = eu_factory.create_motorcycle("Ducati", "Panigale")
eu_vehicle2.start_engine()
