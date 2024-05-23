import pytest
import requests
from unittest.mock import MagicMock
from src.application.models.sales import Sales
from src.application.ports.sales import SalesPort
from src.adapters.driven.repositories.sales import SalesRepository


class ResponseObject:

    @staticmethod
    def json():
        return {
            "sales_id": 1,
            "car_id": 1,
            "buyer_cpf": "12345678901",
            "sale_status": "PENDING"
        }


@pytest.fixture
def sales_adapter():
    return SalesRepository(engine=MagicMock())


@pytest.fixture
async def mock_sales():
    return Sales(
        car_id=1,
        buyer_cpf="12345678901",
        sale_status="PENDING"
    )


@pytest.mark.asyncio
async def test_get_sales(sales_adapter: SalesPort):

    expected_data = ResponseObject
    # Mock the requests.get method
    requests.get = MagicMock(return_value=expected_data)

    # When
    result = await sales_adapter.list_sales()

    # Then
    assert type(result) == list


@pytest.mark.asyncio
async def test_register_sales(sales_adapter: SalesPort, mock_sales):

    expected_data = ResponseObject
    # Mock the requests.post method
    sales_adapter.register_sales = MagicMock(return_value=expected_data)

    # When
    result = sales_adapter.register_sales(mock_sales)

    # Then
    assert result.json() == expected_data.json()


@pytest.mark.asyncio
async def test_update_sales(sales_adapter: SalesPort, mock_sales):
    # Given
    expected_data = ResponseObject
    # Mock the requests.put method
    sales_adapter.update_sales = MagicMock(return_value=expected_data)

    result = sales_adapter.update_sales(mock_sales)

    assert result.json() == expected_data.json()


@pytest.mark.asyncio
async def test_list_sales_by_payment_code(sales_adapter: SalesPort):
    # Given
    payment_code = "12345678901"

    # Mock the requests.get method
    sales_adapter.list_sales_by_payment_code = MagicMock(
        return_value=payment_code)

    # When
    result = sales_adapter.list_sales_by_payment_code(payment_code)

    # Then
    assert result == payment_code


@pytest.mark.asyncio
async def test_delete_sales(sales_adapter: SalesPort):
    # Given
    sales_id = 1
    expected_data = ResponseObject

    # Mock the requests.delete method
    requests.delete = MagicMock(return_value=expected_data)

    # When
    result = await sales_adapter.delete_sales(sales_id)

    # Then
    assert result == 1

@pytest.mark.asyncio
async def test_list_by_sales_id(sales_adapter: SalesPort):
    # Given
    sales_id = 1
    expected_data = ResponseObject

    # Mock the requests.get method
    sales_adapter.list_by_sales_id = MagicMock(return_value=expected_data)

    # When
    result = sales_adapter.list_by_sales_id(sales_id)

    # Then
    assert result.json() == expected_data.json()
