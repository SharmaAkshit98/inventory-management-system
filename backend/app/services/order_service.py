from fastapi import HTTPException

from app.models.order import Order
from app.repositories.order_repositories import OrderRepository
from app.repositories.customer_repositories import CustomerRepository
from app.repositories.product_repositories import ProductRepository


class OrderService:

    @staticmethod
    def create_order(
            db,
            order_data
    ):

        customer = CustomerRepository.get_by_id(
            db,
            order_data.customer_id
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        product = ProductRepository.get_product_by_id(
            db,
            order_data.product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if product.quantity < order_data.quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient inventory"
            )

        total_amount = (
                product.price *
                order_data.quantity
        )

        product.quantity = (
                product.quantity -
                order_data.quantity
        )

        order = Order(
            customer_id=order_data.customer_id,
            product_id=order_data.product_id,
            quantity=order_data.quantity,
            total_amount=total_amount
        )

        return OrderRepository.create_order(
            db,
            order
        )

    @staticmethod
    def get_all_orders(db):
        return OrderRepository.get_all_orders(db)

    @staticmethod
    def get_order_by_id(
            db,
            order_id
    ):

        order = (
            OrderRepository.get_order_by_id(
                db,
                order_id
            )
        )

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        return order

    @staticmethod
    def delete_order(
            db,
            order_id
    ):

        order = (
            OrderRepository.get_order_by_id(
                db,
                order_id
            )
        )

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        OrderRepository.delete_order(
            db,
            order
        )
