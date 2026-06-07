from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.routes.product_routes import router as product_router
from app.routes.customer_routes import router as customer_router
from app.routes.order_routes import router as order_router

app = FastAPI(
    title="Inventory Management API",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)


@app.get("/")
def home():
    return {
        "message": "Inventory Management API Running Successfully"
    }



# from fastapi import FastAPI
#
# from app.database import Base, engine
#
# from app.routes.product_routes import router as product_router
# from app.routes.customer_routes import router as customer_router
# from app.routes.order_routes import router as order_router
#
# app = FastAPI(
#     title="Inventory Management API",
#     version="1.0.0"
# )
#
# Base.metadata.create_all(bind=engine)
#
# app.include_router(product_router)
# app.include_router(customer_router)
# app.include_router(order_router)
#
#
# @app.get("/")
# def home():
#     return {
#         "message": "Inventory Management API Running Successfully"
#     }