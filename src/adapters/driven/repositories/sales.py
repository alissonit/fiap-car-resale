from datetime import datetime
from sqlalchemy.engine import Engine
from sqlalchemy import text

from src.application.models.sales import Sales
from src.application.ports.sales import SalesPort


class SalesRepository(SalesPort):
    """
    Class Repository for Sales
    """

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    async def register_sales(self, sales: Sales) -> Sales:
        async with self.engine.connect() as conn:
            query = text("INSERT INTO sales (car_id, buyer_cpf, sale_status, sale_date, sale_created_at, sale_updated_at) VALUES (:car_id, :buyer_cpf, :sale_status, :sale_date, :sale_created_at, :sale_updated_at) RETURNING *")
            query = query.bindparams(
                car_id=sales.car_id,
                buyer_cpf=sales.buyer_cpf,
                sale_status=sales.sale_status,
                sale_date=datetime.now(),
                sale_created_at=datetime.now(),
                sale_updated_at=datetime.now()
            )

            result = await conn.execute(query)
            sales_raw = result.fetchone()

            return Sales.model_validate(sales_raw._mapping)

    async def list_sales(self) -> list[Sales]:
        async with self.engine.connect() as conn:
            query = text("""SELECT * FROM sales""")
            result = await conn.execute(query)
            return [dict(row) for row in result]

    async def list_by_sales_id(self, sale_id: int) -> Sales:
        async with self.engine.connect() as conn:
            query = text(
                "SELECT * FROM sales WHERE sale_id = :sale_id")
            query = query.bindparams(sale_id=sale_id)
            result = await conn.execute(query)
            raw_sales = result.fetchone()

            if raw_sales:
                return Sales.model_validate(raw_sales._mapping)
            return None

    async def update_sales(self, sales: Sales) -> Sales:
        async with self.engine.connect() as conn:
            query = text("UPDATE sales SET car_id = :car_id, buyer_cpf = :buyer_cpf, sale_status = :sale_status, sale_updated_at = :sale_updated_at WHERE sale_id = :sale_id RETURNING *")
            query = query.bindparams(
                sale_id=sales.sale_id,
                car_id=sales.car_id,
                buyer_cpf=sales.buyer_cpf,
                sale_status=sales.sale_status,
                sale_updated_at=datetime.now()
            )

            result = await conn.execute(query)

            sales_raw = result.fetchone()

            return Sales.model_validate(sales_raw._mapping)

    async def delete_sales(self, sale_id: str) -> Sales:
        async with self.engine.connect() as conn:
            query = text("DELETE FROM sales WHERE sale_id = :sale_id")
            await conn.execute(query, {"sale_id": sale_id})
            return sale_id
