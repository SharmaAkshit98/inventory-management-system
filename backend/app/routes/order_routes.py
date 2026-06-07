from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.order_schema import (
    OrderCreate,
    OrderResponse
)

from app.services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=201
)
def create_order(
        order: OrderCreate,
        db: Session = Depends(get_db)
):
    return OrderService.create_order(
        db,
        order
    )


@router.get(
    "",
    response_model=list[OrderResponse]
)
def get_all_orders(
        db: Session = Depends(get_db)
):
    return OrderService.get_all_orders(db)


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order_by_id(
        order_id: int,
        db: Session = Depends(get_db)
):
    return OrderService.get_order_by_id(
        db,
        order_id
    )


@router.delete(
    "/{order_id}"
)
def delete_order(
        order_id: int,
        db: Session = Depends(get_db)
):
    return OrderService.delete_order(
        db,
        order_id
    )
