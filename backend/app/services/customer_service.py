from fastapi import HTTPException

from app.models.customer import Customer
from app.repositories.customer_repositories import CustomerRepository


class CustomerService:

    @staticmethod
    def create_customer(
        db,
        customer_data
    ):

        existing_customer = (
            CustomerRepository.get_by_email(
                db,
                customer_data.email
            )
        )

        if existing_customer:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

        customer = Customer(
            full_name=customer_data.full_name,
            email=customer_data.email,
            phone_number=customer_data.phone_number
        )

        return CustomerRepository.create(
            db,
            customer
        )

    @staticmethod
    def get_customers(db):
        return CustomerRepository.get_all(db)

    @staticmethod
    def get_customer(
        db,
        customer_id
    ):

        customer = (
            CustomerRepository.get_by_id(
                db,
                customer_id
            )
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return customer

    @staticmethod
    def delete_customer(
        db,
        customer_id
    ):

        customer = (
            CustomerRepository.get_by_id(
                db,
                customer_id
            )
        )

        if not customer:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        CustomerRepository.delete(
            db,
            customer
        )
