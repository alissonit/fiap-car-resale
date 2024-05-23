import pytest
from starlette.testclient import TestClient
from unittest.mock import AsyncMock
from src.configuration.dependency_injection import Container
from src.application.models.car import Car
from src.application.models.sales import Sales
from src.application.ports.car import CarPort
from src.application.ports.sales import SalesPort
from main import app


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
def mock_car() -> Car:
    return Car(
        car_user_id="1",
        car_brand="Fiat",
        car_model="Uno",
        car_year=2021,
        car_color="Red",
        car_price=10000,
        car_type="Hatch",
        car_condition="New",
        car_transmission="Manual",
        car_mileage=0,
        car_engine="1.0",
        car_fuel="Gasoline",
        car_description="New car",
        car_armored=False,
        car_sold=False,
        car_created_at="2021-09-01T00:00:00",
        car_updated_at=None
    )

@pytest.fixture
def sales() -> Sales:
    return Sales(
        sales_id="1",
        sales_user_id="1",
        sales_car_id="1",
        sales_payment_status="Pending",
        sales_created_at="2021-09-01T00:00:00",
        sales_updated_at=None
    )


@pytest.fixture
def mock_car_port() -> CarPort:
    return AsyncMock(
        spec=CarPort,
        register_car=AsyncMock(),
        list_cars=AsyncMock(),
        list_by_user_id=AsyncMock(),
        list_by_car_id=AsyncMock(),
        update_car=AsyncMock(),
        delete_car=AsyncMock(),
        car_filter=AsyncMock()
    )


@pytest.fixture
def mock_sales_port() -> SalesPort:
    return AsyncMock(
        spec=SalesPort,
        register_sales=AsyncMock(),
        list_sales=AsyncMock(),
        list_by_sales_id=AsyncMock(),
        list_sales_by_payment_code=AsyncMock(),
        update_sales=AsyncMock(),
        delete_sales=AsyncMock()
    )


@pytest.fixture
def container(mocker, mock_car_port, mock_sales_port):
    container = Container()
    container.engine.override(mocker.Mock())
    container.car_repository.override(mock_car_port)
    container.sales_repository.override(mock_sales_port)
    return container


@pytest.fixture
def client(container):
    app.container = container
    return TestClient(app)


def test_list_car(mocker, client):
    response = client.get("/fiap-car-resale/api/v1/cars")

    assert response.status_code == 200


def test_list_sales(mocker, client):
    response = client.get("/fiap-car-resale/api/v1/sales")

    assert response.status_code == 200

