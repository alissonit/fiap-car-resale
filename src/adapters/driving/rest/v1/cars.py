# Description: Cars API endpoints
from typing import Union
from fastapi_filter import FilterDepends
from fastapi import APIRouter, Response

from src.application.filters.car import CarFilter
from infrastructure.database.models.tables import Car as CarTable
from src.adapters.driving.rest.v1.dto.cars import (
    RegisterCarV1Request,
    RegisterCarV1Response,
    DeleteCarV1Response,
    UpdateCarV1Request,
    ExceptionResponse
)

from src.application.use_cases.car import (
    use_case_create_car,
    use_case_update_car,
    use_case_delete_car,
    use_case_list_cars
)

router = APIRouter()


@router.get("/cars", response_model=list[RegisterCarV1Response])
async def list_cars(
    response: Response,
    car_filter: CarFilter = FilterDepends(CarFilter),
    order_by: str = CarTable.car_price.desc()
) -> list[RegisterCarV1Response]:
    """
    List cars
    """

    cars, _ = await use_case_list_cars(
        car_filter=car_filter, order_by=order_by, response=response)

    return cars


@router.post("/cars", response_model=Union[RegisterCarV1Response, ExceptionResponse])
async def register_car(
    response: Response,
    car_request: RegisterCarV1Request,
) -> Union[RegisterCarV1Response, ExceptionResponse]:
    """
    Register a car
    """

    car, _ = await use_case_create_car(
        car_request=car_request, response=response)

    return car


@router.put("/cars", response_model=Union[RegisterCarV1Response, ExceptionResponse])
async def update_car(
        response: Response,
        car_request: UpdateCarV1Request) -> Union[RegisterCarV1Response, ExceptionResponse]:
    """
    Update a car
    """

    car, _ = await use_case_update_car(
        car_request=car_request, response=response)

    return car


@router.delete("/cars/{car_id}", response_model=Union[DeleteCarV1Response, ExceptionResponse])
async def delete_car(
        response: Response,
        car_id: int) -> Union[DeleteCarV1Response, ExceptionResponse]:
    """
    Delete a car
    """
    car, _ = await use_case_delete_car(
        car_id=car_id, response=response)

    return car
