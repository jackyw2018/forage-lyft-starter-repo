from abc import ABC, abstractmethod
from datetime import datetime

from battery import Battery, SpindlerBattery, NubbinBattery
from engine import Engine, SternmanEngine, CapuletEngine, WilloughbyEngine


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        """
        Args:
            engine (Engine): Engine instance of the car
            battery (Battery): Battery instance of the car
        """
        self._engine = engine
        self._battery = battery

    def needs_service(self) -> bool:
        """
        Whether the engine needs serivcing

        Returns:
            bool
        """
        return self._battery.needs_service() and self._engine.needs_service()


class CarFactory():

    @classmethod
    def create_calliope(
            current_date: datetime.date, last_service_date: datetime.date,
            current_mileage: int, last_service_mileage: int) -> Car:
        """Create a Calliope-model car

        Args:
            current_date (datetime.date): Current date
            last_service_date (datetime.date): The date of last service
            current_mileage (int): Mileage traveled thus far
            last_service_mileage (int): Mileage tracked during last service

        Returns:
            Car
        """
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @classmethod
    def create_glissade(
            current_date: datetime.date, last_service_date: datetime.date,
            current_mileage: int, last_service_mileage: int) -> Car:
        """Create a Glissade-model car

        Args:
            current_date (datetime.date): Current date
            last_service_date (datetime.date): The date of last service
            current_mileage (int): Mileage traveled thus far
            last_service_mileage (int): Mileage tracked during last service

        Returns:
            Car
        """
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @classmethod
    def create_palindrome(
            current_date: datetime.date, last_service_date: datetime.date,
            warning_light_on: bool) -> Car:
        """Create a Palindrome-model car

        Args:
            current_date (datetime.date): Current date
            last_service_date (datetime.date): The date of last service
            warning_light_on (bool): Warning light is on or not

        Returns:
            Car
        """
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)

    @classmethod
    def create_rorschach(
            current_date: datetime.date, last_service_date: datetime.date,
            current_mileage: int, last_service_mileage: int) -> Car:
        """Create a Rorschach-model car

        Args:
            current_date (datetime.date): Current date
            last_service_date (datetime.date): The date of last service
            current_mileage (int): Mileage traveled thus far
            last_service_mileage (int): Mileage tracked during last service

        Returns:
            Car
        """
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    @classmethod
    def create_thovex(
            current_date: datetime.date, last_service_date: datetime.date,
            current_mileage: int, last_service_mileage: int) -> Car:
        """Create a Thovex-model car

        Args:
            current_date (datetime.date): Current date
            last_service_date (datetime.date): The date of last service
            current_mileage (int): Mileage traveled thus far
            last_service_mileage (int): Mileage tracked during last service

        Returns:
            Car
        """
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
