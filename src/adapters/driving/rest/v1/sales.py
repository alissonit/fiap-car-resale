from fastapi import APIRouter, Response, status
from dependency_injector.wiring import inject

from src.adapters.driving.rest.v1.dto.sales import (
    RegisterSalesV1Request,
    RegisterSalesV1Response,
    DeleteSalesV1Response
)

from src.application.use_cases.sales import (
    use_case_list_sales,
    use_case_create_sales,
    use_case_update_sales,
    use_case_delete_sales
)


router = APIRouter()


@router.get("/api/v1/sales", response_model=list[RegisterSalesV1Response])
@inject
async def list_sales() -> list[RegisterSalesV1Response]:
    """
    List all sales
    """

    sales = await use_case_list_sales()

    return sales


@router.post("/api/v1/sales", response_model=RegisterSalesV1Response)
@inject
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


@router.put("/api/v1/sales", response_model=RegisterSalesV1Response)
@inject
async def update_sales(
    sales_request: RegisterSalesV1Request
) -> RegisterSalesV1Response:
    """
    Update a sales
    """

    sales = await use_case_update_sales(sales_request)

    return sales


@router.delete("/api/v1/sales/{sales_id}", response_model=DeleteSalesV1Response)
@inject
async def delete_sales(
    sales_id: int
):
    """
    Delete a sales
    """

    sales = await use_case_delete_sales(sales_id)

    return sales
