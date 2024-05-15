# Description: Cars API endpoints
from fastapi import APIRouter, Response, status
from dependency_injector.wiring import inject

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
@inject
async def list_cars() -> list[RegisterCarV1Response]:
    """
    List cars
    """

    cars = await use_case_list_cars()

    return cars


@router.post("/api/v1/cars", response_model=RegisterCarV1Response)
@inject
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
@inject
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
@inject
async def delete_car(
        response: Response,
        car_id: int) -> DeleteCarV1Response:
    """
    Delete a car
    """
    car = await use_case_delete_car(car_id)

    response.status_code = status.HTTP_200_OK

    return DeleteCarV1Response(car_id=car.car_id)
