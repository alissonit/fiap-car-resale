from fastapi import Depends
from dependency_injector.wiring import Provide, inject

from src.application.ports.car import CarPort

from fastapi_filter import FilterDepends
from sqlalchemy.sql.expression import select

from src.application.filters.car import CarFilter
from src.infrastructure.database.models.tables import Car as CarTable

from src.adapters.driving.rest.v1.dto.cars import (
    RegisterCarV1Request,
    RegisterCarV1Response,
    DeleteCarV1Response
)
from src.configuration.dependency_injection import Container


@inject
async def use_case_list_cars(
    car_filter: CarFilter = FilterDepends(CarFilter),
    car_port: CarPort = Depends(
        Provide[Container.car_repository]),
    order_by: str = CarTable.car_price.desc()
) -> list[RegisterCarV1Response]:
    """
    List cars
    """

    if order_by == "-car_price":
        order_by = CarTable.car_price.desc()
    if order_by == "+car_price":
        order_by = CarTable.car_price.asc()

    query = select(CarTable)

    query = car_filter.filter(query).order_by(order_by)

    cars = await car_port.car_filter(query)

    return cars


@inject
async def use_case_create_car(
    car_request: RegisterCarV1Request,
    car_port: CarPort = Depends(Provide[Container.car_repository])
) -> RegisterCarV1Response:
    """
    Register a car
    """

    car = await car_port.register_car(car_request)

    return car


@inject
async def use_case_update_car(
        car_request: RegisterCarV1Request,
        car_port: CarPort = Depends(
            Provide[Container.car_repository])) -> RegisterCarV1Response:
    """
    Update a car
    """

    car = await car_port.update_car(car_request)

    return car


@inject
async def use_case_delete_car(
        car_id: int,
        car_port: CarPort = Depends(
            Provide[Container.car_repository])) -> DeleteCarV1Response:
    """
    Delete a car
    """
    car = await car_port.delete_car(car_id)

    return car
