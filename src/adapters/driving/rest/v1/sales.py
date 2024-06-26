from fastapi import APIRouter, Response, status
from dependency_injector.wiring import inject

from src.adapters.driving.rest.v1.dto.sales import (
    RegisterSalesV1Request,
    RegisterSalesV1Response,
    UpdateSalesV1Request,
    DeleteSalesV1Response,
    PaymentStatus
)

from src.application.use_cases.sales import (
    use_case_list_sales,
    use_case_create_sales,
    use_case_update_sales,
    use_case_delete_sales,
    update_payment_status
)


router = APIRouter()


@router.get("/sales", response_model=list[RegisterSalesV1Response])
async def list_sales() -> list[RegisterSalesV1Response]:
    """
    List all sales
    """

    sales = await use_case_list_sales()

    return sales


@router.post("/sales", response_model=RegisterSalesV1Response)
async def register_sales(
    response: Response,
    sales_request: RegisterSalesV1Request,
) -> RegisterSalesV1Response:
    """
    Register a sales
    """

    sales = await use_case_create_sales(sales_request)

    response.status_code = status.HTTP_201_CREATED

    return sales


@router.put("/sales", response_model=RegisterSalesV1Response)
async def update_sales(
    sales_request: UpdateSalesV1Request
) -> RegisterSalesV1Response:
    """
    Update a sales
    """

    sales = await use_case_update_sales(sales_request)

    return sales


@router.delete("/sales/{sales_id}", response_model=DeleteSalesV1Response)
async def delete_sales(
    sales_id: int
):
    """
    Delete a sales
    """

    sales = await use_case_delete_sales(sales_id)

    return sales


@router.post("/sales/webhook/payment", response_model=RegisterSalesV1Response)
async def webhook_payment(
    requests: PaymentStatus
) -> RegisterSalesV1Response:
    """
    Webhook for payment
    """

    payment = await update_payment_status(requests)

    return payment
