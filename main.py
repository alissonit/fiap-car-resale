from fastapi import FastAPI

from src.adapters.driving.rest.v1.cars import router as cars_router
from src.adapters.driving.rest.v1.sales import router as sales_router
from src.adapters.driving.rest.v1.settings import router as settings_router
from src.configuration.dependency_injection import Container

ROOT_PATH = "/fiap-car-resale/api/v1"

app = FastAPI(
    title="Resale Car API",
    description="API for managing cars for resale",
    version="1.0.0",
    openapi_url=f"{ROOT_PATH}/openapi.json",
    docs_url=f"{ROOT_PATH}/docs",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

container = Container()


@app.get(f"{ROOT_PATH}/health")
async def health():
    return {"status": "ok"}

app.include_router(sales_router, tags=["sales"], prefix=ROOT_PATH)
app.include_router(cars_router, tags=["cars"], prefix=ROOT_PATH)
app.include_router(settings_router, tags=["settings"], prefix=ROOT_PATH)
