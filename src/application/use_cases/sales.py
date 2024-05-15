from fastapi import Depends
from dependency_injector.wiring import Provide, inject

from src.application.ports.sales import SalesPort

from src.adapters.driving.rest.v1.dto.sales import (
    RegisterSalesV1Request,
    RegisterSalesV1Response,
    DeleteSalesV1Response
)
from src.configuration.dependency_injection import Container


@inject
async def use_case_list_sales(
        sales_port: SalesPort = Depends(
            Provide[Container.sales_repository])) -> list[RegisterSalesV1Response]:
    """
    List sales
    """

    sales = await sales_port.list_sales()

    return sales


@inject
async def use_case_create_sales(
    sales_request: RegisterSalesV1Request,
    sales_port: SalesPort = Depends(Provide[Container.sales_repository])
) -> RegisterSalesV1Response:
    """
    Register a sales
    """

    sales = await sales_port.register_sales(sales_request)

    return sales


@inject
async def use_case_update_sales(
        sales_request: RegisterSalesV1Request,
        sales_port: SalesPort = Depends(
            Provide[Container.sales_repository])) -> RegisterSalesV1Response:
    """
    Update a sales
    """

    sales = await sales_port.update_sales(sales_request)

    return sales


@inject
async def use_case_delete_sales(
        sales_id: int,
        sales_port: SalesPort = Depends(
            Provide[Container.sales_repository])) -> DeleteSalesV1Response:
    """
    Delete a sales
    """
    sales = await sales_port.delete_sales(sales_id)

    return sales
