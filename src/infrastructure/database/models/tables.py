from sqlalchemy import Column, String, Integer, DateTime, Float, Boolean

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Sales(Base):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer)
    buyer_cpf = Column(String)
    sale_status = Column(String)
    sale_date = Column(DateTime)
    sale_created_at = Column(DateTime)
    sale_updated_at = Column(DateTime)


class Car(Base):
    __tablename__ = "cars"
    car_id = Column(Integer, primary_key=True, index=True)
    car_user_id = Column(Integer)
    car_brand = Column(String)
    car_model = Column(String)
    car_year = Column(Integer)
    car_color = Column(String)
    car_price = Column(Float)
    car_type = Column(String)
    car_condition = Column(String)
    car_transmission = Column(String)
    car_mileage = Column(Float)
    car_engine = Column(Float)
    car_fuel = Column(String)
    car_description = Column(String)
    car_armored = Column(Boolean)
    car_sold = Column(Boolean)
    car_created_at = Column(DateTime)
    car_updated_at = Column(DateTime)
    car_deleted_at = Column(DateTime)
