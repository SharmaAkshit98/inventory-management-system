from fastapi import FastAPI

from app.database import Base, engine
from app.models.product import Product
from app.routes.product_routes import router as product_router

app = FastAPI(
    title="Inventory Management API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(product_router)


@app.get("/")
def home():
    return {
        "message": "Inventory Management API Running Successfully"
    }
