from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Car(BaseModel):
    """
    Class Model for Car
    """

    car_id: Optional[int] = None
    car_user_id: int
    car_brand: str
    car_model: str
    car_year: int
    car_color: str
    car_price: int
    car_type: str
    car_condition: str
    car_transmission: str
    car_mileage: float
    car_engine: float
    car_fuel: str
    car_description: str
    car_armored: bool
    car_sold: bool
    car_created_at: Optional[datetime] = None
    car_updated_at: Optional[datetime] = None
    car_deleted_at: Optional[datetime] = None

    class Config:
        """
        Class config for Car
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_user_id": "123e4567-e89b-12d3-a456-426614174000",
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
