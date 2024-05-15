from datetime import datetime
from sqlalchemy.engine import Engine
from sqlalchemy import text

from src.application.models.car import Car
from src.application.ports.car import CarPort


class CarRepository(CarPort):
    """
    Class Repository for Car
    """

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    async def register_car(self, car: Car) -> Car:
        async with self.engine.connect() as conn:
            query = text("INSERT INTO cars (car_user_id, car_brand, car_model, car_year, car_color, car_price, car_type, car_condition, car_transmission, car_mileage, car_engine, car_fuel, car_description, car_armored, car_sold, car_created_at, car_updated_at) VALUES (:car_user_id, :car_brand, :car_model, :car_year, :car_color, :car_price, :car_type, :car_condition, :car_transmission, :car_mileage, :car_engine, :car_fuel, :car_description, :car_armored, :car_sold, :car_created_at, :car_updated_at) RETURNING *")
            query = query.bindparams(
                car_user_id=car.car_user_id,
                car_brand=car.car_brand,
                car_model=car.car_model,
                car_year=car.car_year,
                car_color=car.car_color,
                car_price=car.car_price,
                car_type=car.car_type,
                car_condition=car.car_condition,
                car_transmission=car.car_transmission,
                car_mileage=car.car_mileage,
                car_engine=car.car_engine,
                car_fuel=car.car_fuel,
                car_description=car.car_description,
                car_armored=car.car_armored,
                car_sold=car.car_sold,
                car_created_at=datetime.now(),
                car_updated_at=None
            )
            result = await conn.execute(query)
            user_raw = result.fetchone()

            return Car.model_validate(user_raw._mapping)
    
    async def car_filter(self, query: Car) -> Car:
        async with self.engine.connect() as conn:
            result = await conn.execute(query)
            raw_user = result.fetchall()

            return [Car.model_validate(user._mapping) for user in raw_user]

    async def list_cars(self) -> list[Car]:
        async with self.engine.connect() as conn:
            query = text("""SELECT * FROM cars""")
            result = await conn.execute(query)
            return [dict(row) for row in result]

    async def list_by_user_id(self, user_id: str) -> list[Car]:
        async with self.engine.connect() as conn:
            query = text(
                "SELECT * FROM cars WHERE car_user_id = :car_user_id")
            query = query.bindparams(car_user_id=user_id)

            result = await conn.execute(query)

            raw_user = result.fetchall()

            return [Car.model_validate(user._mapping) for user in raw_user]

    async def list_by_car_id(self, car_id: str) -> Car:
        async with self.engine.connect() as conn:
            query = text("SELECT * FROM cars WHERE car_id = :car_id")
            query = query.bindparams(car_id=car_id)
            result = await conn.execute(query)
            raw_user = result.fetchall()

            return [Car.model_validate(user._mapping) for user in raw_user]

    async def update_car(self, car: Car) -> Car:
        async with self.engine.connect() as conn:
            query = text("UPDATE cars SET car_user_id = :car_user_id, car_brand = :car_brand, car_model = :car_model, car_year = :car_year, car_color = :car_color, car_price = :car_price, car_type = :car_type, car_condition = :car_condition, car_transmission = :car_transmission, car_mileage = :car_mileage, car_engine = :car_engine, car_fuel = :car_fuel, car_description = :car_description, car_armored = :car_armored, car_sold = :car_sold, car_updated_at = :car_updated_at WHERE car_id = :car_id RETURNING *")
            query = query.bindparams(
                car_id=car.car_id,
                car_user_id=car.car_user_id,
                car_brand=car.car_brand,
                car_model=car.car_model,
                car_year=car.car_year,
                car_color=car.car_color,
                car_price=car.car_price,
                car_type=car.car_type,
                car_condition=car.car_condition,
                car_transmission=car.car_transmission,
                car_mileage=car.car_mileage,
                car_engine=car.car_engine,
                car_fuel=car.car_fuel,
                car_description=car.car_description,
                car_armored=car.car_armored,
                car_sold=car.car_sold,
                car_updated_at=datetime.now()
            )
            result = await conn.execute(query)

            raw_car = result.fetchone()

            if raw_car:
                return Car.model_validate(raw_car._mapping)

            return result

    async def delete_car(self, car_id: str) -> Car:
        async with self.engine.connect() as conn:
            query = text("DELETE FROM cars WHERE car_id = :car_id RETURNING *")
            query = query.bindparams(car_id=car_id)
            result = await conn.execute(query)

            raw_car = result.fetchone()

            if raw_car:
                return Car.model_validate(raw_car._mapping)
