"""
This module contains the Pydantic Models for the Saless
"""
from typing import Optional, Literal
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass
class RegisterSalesV1Request(BaseModel):
    """
    Class Model for Register Sales
    """
    car_id: int
    buyer_cpf: str
    sale_status: Literal['PENDING', 'COMPLETED', 'CANCELLED'] = 'PENDING'

    class Config:
        """
        Class config for Register Sales
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1,
                "buyer_cpf": "12345678900"
            }
        }


@dataclass
class RegisterSalesV1Response(BaseModel):
    """
    Class Model for Register Sales Response
    """
    sale_id: int
    car_id: int
    buyer_cpf: str
    sale_status: Literal['PENDING', 'COMPLETED', 'CANCELLED']

    class Config:
        """
        Class config for Register Sales
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "car_id": 1,
                "buyer_cpf": "12345678900",
                "sale_status": "COMPLETED",
                "sale_date": "2021-10-10T00:00:00",
                "sale_created_at": "2021-10-10T00:00:00",
                "sale_updated_at": "2021-10-10T00:00:00"
            }
        }


class UpdateSalesV1Request(BaseModel):
    """
    Class Model for Update Sales
    """
    sale_id: int
    car_id: Optional[int]
    buyer_cpf: Optional[str]
    sale_status: Optional[Literal['PENDING', 'COMPLETED', 'CANCELLED']]

    class Config:
        """
        Class config for Update Sales
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "sale_id": 1,
                "car_id": 1,
                "buyer_cpf": "12345678900",
                "sale_status": "COMPLETED"
            }
        }


@dataclass
class RegisterSalesV1ListResponse(BaseModel):
    sales: list[RegisterSalesV1Response]


@dataclass
class DeleteSalesV1Request(BaseModel):
    sale_id: int

    class Config:
        """
        Class config for Delete Sales
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "sale_id": 1
            }
        }


@dataclass
class DeleteSalesV1Response(BaseModel):
    sale_id: int

    class Config:
        """
        Class config for Delete Sales
        """
        from_attributes = True
        json_schema_extra = {
            "example": {
                "sale_id": 1
            }
        }
