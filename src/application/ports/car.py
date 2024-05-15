from abc import ABC, abstractmethod

from src.application.models.car import Car


class CarPort(ABC):
    """
    Interface for Car Port
    """

    @abstractmethod
    async def register_car(self, car: Car) -> Car:
        """
        Register Car
        """
        pass

    @abstractmethod
    async def list_cars(self) -> list[Car]:
        """
        List Cars
        """
        pass

    @abstractmethod
    async def list_by_user_id(self, user_id: str) -> list[Car]:
        """
        List Cars by Sales ID
        """
        pass

    @abstractmethod
    async def list_by_car_id(self, car_id: str) -> Car:
        """
        List Car by Car ID
        """
        pass

    @abstractmethod
    async def update_car(self, car: Car) -> Car:
        """
        Update Car
        """
        pass

    @abstractmethod
    async def delete_car(self, car_id: str) -> Car:
        """
        Delete Car
        """
        pass
    
    @abstractmethod
    async def car_filter(self, query: Car) -> Car:
        """
        Filter Car
        """
        pass