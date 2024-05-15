"""
This module contains the Pydantic Models for the Cars
"""
from typing import Literal, Optional
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class RegisterCarV1Request(BaseModel):
    """
    Class Model for Register Car
    """
    car_id: Optional[int]
    car_user_id: int
    car_brand: str
    car_model: str
    car_year: int
    car_color: str
    car_price: int
    car_type: Literal[
        'Sedan', 'SUV', 'Truck', 'Van',
        'Coupe', 'Convertible', 'Wagon', 'Sports Car', 'Hybrid',
        'Electric', 'Luxury', 'Crossover', 'Hatchback', 'Minivan',
        'Pickup', 'Off-Road', 'Commercial', 'Other']
    car_condition: Literal['New', 'Used']
    car_transmission: Literal['Automatic', 'Manual']
    car_mileage: float
    car_engine: float
    car_fuel: Literal['Gasoline', 'Diesel', 'Electric', 'Hybrid']
    car_price: int
    car_description: str
    car_armored: bool
    car_sold: bool

    class Config:
        """
        Class config for Register Car
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1,
                "car_user_id": 2,
                "car_brand": "Toyota",
                "car_model": "Corolla",
                "car_year": 2021,
                "car_color": "Black",
                "car_price": 30000.00,
                "car_type": "Sedan",
                "car_condition": "New",
                "car_transmission": "Automatic",
                "car_mileage": 10.500,
                "car_engine": 1.8,
                "car_fuel": "Gasoline",
                "car_description": "Brand new car",
                "car_armored": False,
                "car_sold": False
            }
        }


@dataclass
class RegisterCarV1Response(BaseModel):
    """
    Class Model for List Car
    """
    car_id: int
    car_user_id: int
    car_brand: str
    car_model: str
    car_year: int
    car_color: str
    car_price: int
    car_type: Literal[
        'Sedan', 'SUV', 'Truck', 'Van',
        'Coupe', 'Convertible', 'Wagon', 'Sports Car', 'Hybrid',
        'Electric', 'Luxury', 'Crossover', 'Hatchback', 'Minivan',
        'Pickup', 'Off-Road', 'Commercial', 'Other']
    car_condition: Literal['New', 'Used']
    car_transmission: Literal['Automatic', 'Manual']
    car_mileage: float
    car_engine: float
    car_fuel: Literal['Gasoline', 'Diesel', 'Electric', 'Hybrid']
    car_description: str
    car_armored: bool
    car_sold: bool

    class Config:
        """
        Class config for List Car
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1,
                "car_user_id": 2,
                "car_brand": "Toyota",
                "car_model": "Corolla",
                "car_year": 2021,
                "car_color": "Black",
                "car_price": 30000.00,
                "car_type": "Sedan",
                "car_condition": "New",
                "car_transmission": "Automatic",
                "car_mileage": 10.500,
                "car_engine": 1.8,
                "car_fuel": "Gasoline",
                "car_description": "Brand new car",
                "car_armored": False,
                "car_sold": False
            }
        }


@dataclass
class CreateCarV1ListResponse(BaseModel):
    cars: list[RegisterCarV1Response]


@dataclass
class DeleteCarV1Request(BaseModel):
    car_id: int

    class Config:
        """
        Class config for delete Car
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1
            }
        }


@dataclass
class DeleteCarV1Response(BaseModel):
    car_id: int

    class Config:
        """
        Class config for delete Car
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1
            }
        }
