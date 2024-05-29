from typing import Optional

from fastapi_filter.contrib.sqlalchemy import Filter

from infrastructure.database.models.tables import Car as CarTable


class CarFilter(Filter):
    # filter by all fields
    car_user_id: Optional[int] = None
    car_brand__in: Optional[list[str]] = None
    car_model: Optional[str] = None
    car_color: Optional[str] = None
    car_type: Optional[str] = None
    car_condition: Optional[str] = None
    car_sold: Optional[bool] = None

    class Constants(Filter.Constants):
        model = CarTable
