from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    @staticmethod
    def create_product(db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_all_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_product_by_id(
            db: Session,
            product_id: int
    ):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    @staticmethod
    def get_product_by_sku(
            db: Session,
            sku: str
    ):
        return (
            db.query(Product)
            .filter(Product.sku == sku)
            .first()
        )

    @staticmethod
    def update_product(
            db: Session,
            product: Product
    ):
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(
            db: Session,
            product: Product
    ):
        db.delete(product)
        db.commit()
