"""
This module contains the Pydantic Models for the Saless
"""
from datetime import datetime

from typing import Optional, Literal
from pydantic import BaseModel


class Sales(BaseModel):
    """
    Class Model for Register Sales
    """
    sale_id: Optional[int] = None
    car_id: int
    buyer_cpf: str
    sale_status: Literal['PENDING', 'COMPLETED', 'CANCELLED']
    sale_date: Optional[datetime] = None
    sale_created_at: Optional[datetime] = None
    sale_updated_at: Optional[datetime] = None

    class Config:
        """
        Class config for Register Sales
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1,
                "buyer_cpf": "12345678900",
                "sale_status": "PENDING",
                "sale_date": "2021-10-10T00:00:00"
            }
        }
