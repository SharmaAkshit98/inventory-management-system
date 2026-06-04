from fastapi import HTTPException

from app.models.product import Product
from app.repositories.product_repositories import ProductRepository


class ProductService:

    @staticmethod
    def create_product(db, product_data):

        if product_data.price <= 0:
            raise HTTPException(
                status_code=400,
                detail="Price must be greater than zero"
            )

        if product_data.quantity < 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity cannot be negative"
            )

        existing_product = (
            ProductRepository.get_product_by_sku(
                db,
                product_data.sku
            )
        )

        if existing_product:
            raise HTTPException(
                status_code=409,
                detail="SKU already exists"
            )

        product = Product(
            name=product_data.name,
            sku=product_data.sku,
            price=product_data.price,
            quantity=product_data.quantity
        )

        return ProductRepository.create_product(
            db,
            product
        )

    @staticmethod
    def get_all_products(db):
        return ProductRepository.get_all_products(
            db
        )

    @staticmethod
    def get_product_by_id(
            db,
            product_id
    ):

        product = (
            ProductRepository.get_product_by_id(
                db,
                product_id
            )
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product

    @staticmethod
    def update_product(
            db,
            product_id,
            product_data
    ):

        product = (
            ProductRepository.get_product_by_id(
                db,
                product_id
            )
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if product_data.price <= 0:
            raise HTTPException(
                status_code=400,
                detail="Price must be greater than zero"
            )

        if product_data.quantity < 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity cannot be negative"
            )

        product.name = product_data.name
        product.sku = product_data.sku
        product.price = product_data.price
        product.quantity = product_data.quantity

        return ProductRepository.update_product(
            db,
            product
        )

    @staticmethod
    def delete_product(
            db,
            product_id
    ):

        product = (
            ProductRepository.get_product_by_id(
                db,
                product_id
            )
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        ProductRepository.delete_product(
            db,
            product
        )

        return {
            "message": "Product deleted successfully"
        }


# from fastapi import HTTPException
#
# from app.models.product import Product
# from app.repositories.product_repositories import ProductRepository
#
#
# class ProductService:
#
#     @staticmethod
#     def create_product(db, product_data):
#
#         existing_product = (
#             ProductRepository.get_product_by_sku(
#                 db,
#                 product_data.sku
#             )
#         )
#
#         if existing_product:
#             raise HTTPException(
#                 status_code=409,
#                 detail="SKU already exists"
#             )
#
#         if product_data.quantity < 0:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Quantity cannot be negative"
#             )
#
#         product = Product(
#             name=product_data.name,
#             sku=product_data.sku,
#             price=product_data.price,
#             quantity=product_data.quantity
#         )
#
#         return ProductRepository.create_product(
#             db,
#             product
#         )
#
#     @staticmethod
#     def get_all_products(db):
#         return ProductRepository.get_all_products(
#             db
#         )
#
#     @staticmethod
#     def get_product_by_id(
#             db,
#             product_id
#     ):
#
#         product = (
#             ProductRepository.get_product_by_id(
#                 db,
#                 product_id
#             )
#         )
#
#         if not product:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Product not found"
#             )
#
#         return product
#
#     @staticmethod
#     def update_product(
#             db,
#             product_id,
#             product_data
#     ):
#
#         product = (
#             ProductRepository.get_product_by_id(
#                 db,
#                 product_id
#             )
#         )
#
#         if not product:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Product not found"
#             )
#
#         if product_data.quantity < 0:
#             raise HTTPException(
#                 status_code=400,
#                 detail="Quantity cannot be negative"
#             )
#
#         product.name = product_data.name
#         product.sku = product_data.sku
#         product.price = product_data.price
#         product.quantity = product_data.quantity
#
#         return ProductRepository.update_product(
#             db,
#             product
#         )
#
#     @staticmethod
#     def delete_product(
#             db,
#             product_id
#     ):
#
#         product = (
#             ProductRepository.get_product_by_id(
#                 db,
#                 product_id
#             )
#         )
#
#         if not product:
#             raise HTTPException(
#                 status_code=404,
#                 detail="Product not found"
#             )
#
#         ProductRepository.delete_product(
#             db,
#             product
#         )
#
#         return {
#             "message": "Product deleted successfully"
#         }
#
