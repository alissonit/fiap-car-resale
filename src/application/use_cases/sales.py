from fastapi import Depends, HTTPException
from dependency_injector.wiring import Provide, inject

from src.application.ports.sales import SalesPort
from src.application.ports.car import CarPort

from src.adapters.driving.rest.v1.dto.sales import (
    RegisterSalesV1Request,
    RegisterSalesV1Response,
    DeleteSalesV1Response,
    PaymentStatus
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
    sales_id = await sales_port.delete_sales(sales_id)

    return {"message": "Sales deleted", "sale_id": sales_id}


@inject
async def update_payment_status(
        payment_status: PaymentStatus,
        sales_port: SalesPort = Depends(
            Provide[Container.sales_repository]),
        car_port: CarPort = Depends(Provide[Container.car_repository])):
    """
    Update a sales
    """

    # get sales by payment code
    sales = await sales_port.list_sales_by_payment_code(payment_status.payment_code)

    if sales:
        # update sales status
        sales.sale_status = payment_status.status
        sales = await sales_port.update_sales(sales)
        if payment_status.status == "COMPLETED":
            car = await car_port.list_by_car_id(sales.car_id)
            car[0].car_sold = True
            await car_port.update_car(car[0])
        else:
            car = await car_port.list_by_car_id(sales.car_id)
            car[0].car_sold = False
            await car_port.update_car(car[0])
        return sales
    raise HTTPException(status_code=404, detail="Payment code not found")
