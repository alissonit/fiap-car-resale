from abc import ABC, abstractmethod

from src.application.models.sales import Sales


class SalesPort(ABC):
    """
    Interface for Sales Port
    """

    @abstractmethod
    async def register_sales(self, sales: Sales) -> Sales:
        """
        Register Sales
        """
        pass

    @abstractmethod
    async def list_sales(self) -> list[Sales]:
        """
        List Saless
        """
        pass

    @abstractmethod
    async def list_by_sales_id(self, sales_id: str) -> Sales:
        """
        List Sales by Sales ID
        """
        pass
    
    @abstractmethod
    async def list_sales_by_payment_code(self, sales_id: str) -> Sales:
        """
        List Sales by Sales ID
        """
        pass

    @abstractmethod
    async def update_sales(self, sales: Sales) -> Sales:
        """
        Update Sales
        """
        pass

    @abstractmethod
    async def delete_sales(self, sales_id: str) -> Sales:
        """
        Delete Sales
        """
        pass
