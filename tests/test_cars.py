import pytest
import requests
from unittest.mock import MagicMock
from src.application.models.car import Car
from src.application.ports.car import CarPort
from src.adapters.driven.repositories.cars import CarRepository


class ResponseObject:

    @staticmethod
    def json():
        return {
            "car_id": 1,
            "car_user_id": 1,
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


@pytest.fixture
def car_adapter():
    return CarRepository(engine=MagicMock())


@pytest.fixture
async def mock_car():
    return Car(
        car_user_id=1,
        car_brand="Toyota",
        car_model="Corolla",
        car_year=2021,
        car_color="Black",
        car_price=30000.00,
        car_type="Sedan",
        car_condition="New",
        car_transmission="Automatic",
        car_mileage=10.500,
        car_engine=1.8,
        car_fuel="Gasoline",
        car_description="Brand new car",
        car_armored=False,
        car_sold=False
    )


@pytest.mark.asyncio
async def test_list_cars(car_adapter: CarPort):

    expected_data = ResponseObject
    # Mock the requests.get method
    car_adapter.list_cars = MagicMock(return_value=expected_data)

    # When
    result = car_adapter.list_cars()

    # Then
    assert result.json() == expected_data.json()


@pytest.mark.asyncio
async def test_register_car(car_adapter: CarPort, mock_car):

    expected_data = ResponseObject
    # Mock the requests.post method
    car_adapter.register_car = MagicMock(return_value=expected_data)

    # When
    result = car_adapter.register_car(mock_car)

    # Then
    assert result.json() == expected_data.json()

@pytest.mark.asyncio
async def test_update_car(car_adapter: CarPort, mock_car):
    # Given
    expected_data = ResponseObject
    # Mock the requests.put method
    car_adapter.update_car = MagicMock(return_value=expected_data)
    # When
    result = car_adapter.update_car(mock_car)
    # Then
    assert result.json() == expected_data.json()


@pytest.mark.asyncio
async def test_car_filter(car_adapter: CarPort, mock_car):
    # Given
    expected_data = ResponseObject
    # Mock the requests.get method
    car_adapter.car_filter = MagicMock(return_value=expected_data)
    # When
    result = car_adapter.car_filter(mock_car)
    # Then
    assert result.json() == expected_data.json()