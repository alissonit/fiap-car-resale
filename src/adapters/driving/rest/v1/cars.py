# Description: Cars API endpoints
from fastapi_filter import FilterDepends
from fastapi import APIRouter, Response, status

from src.application.filters.car import CarFilter
from src.infrastructure.database.models.tables import Car as CarTable
from src.adapters.driving.rest.v1.dto.cars import (
    RegisterCarV1Request,
    RegisterCarV1Response,
    DeleteCarV1Response
)

from src.application.use_cases.car import (
    use_case_create_car,
    use_case_update_car,
    use_case_delete_car,
    use_case_list_cars
)

router = APIRouter()


@router.get("/api/v1/cars", response_model=list[RegisterCarV1Response])
async def list_cars(
    car_filter: CarFilter = FilterDepends(CarFilter),
    order_by: str = CarTable.car_price.desc()
) -> list[RegisterCarV1Response]:
    """
    List cars
    """

    cars = await use_case_list_cars(car_filter=car_filter, order_by=order_by)

    return cars


@router.post("/api/v1/cars", response_model=RegisterCarV1Response)
async def register_car(
    response: Response,
    car_request: RegisterCarV1Request,
) -> RegisterCarV1Response:
    """
    Register a car
    """

    car = await use_case_create_car(car_request)

    response.status_code = status.HTTP_201_CREATED

    return car


@router.put("/api/v1/cars", response_model=RegisterCarV1Response)
async def update_car(
        response: Response,
        car_request: RegisterCarV1Request) -> RegisterCarV1Response:
    """
    Update a car
    """

    car = await use_case_update_car(car_request)

    response.status_code = status.HTTP_201_CREATED

    return car


@router.delete("/api/v1/cars/{car_id}", response_model=DeleteCarV1Response)
async def delete_car(
        response: Response,
        car_id: int) -> DeleteCarV1Response:
    """
    Delete a car
    """
    car = await use_case_delete_car(car_id)

    response.status_code = status.HTTP_200_OK

    return car
