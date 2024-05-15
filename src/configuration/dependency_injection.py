from dependency_injector import containers, providers
from sqlalchemy.ext.asyncio import create_async_engine

from src.adapters.driven.repositories.cars import CarRepository
from src.adapters.driven.repositories.sales import SalesRepository
from src.configuration.settings import get_db_settings


class Container(containers.DeclarativeContainer):
    """
    Application Container
    """

    wiring_config = containers.WiringConfiguration(
        modules=["src.adapters.driving.rest.v1.cars",
                 "src.adapters.driving.rest.v1.sales",
                 "src.adapters.driving.rest.v1.settings"]
    )

    config = providers.Configuration()
    config.from_dict(get_db_settings().model_dump())

    db_settings = providers.Singleton(get_db_settings, config=config)

    engine = providers.Singleton(
        create_async_engine,
        config.get("db_uri"),
        pool_size=config.get("db_max_pool_size"),
        isolation_level="AUTOCOMMIT"
    )

    car_repository = providers.Factory(
        CarRepository, engine=engine
    )

    sales_repository = providers.Factory(
        SalesRepository, engine=engine
    )
