from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)

    sku: str = Field(
        ...,
        min_length=2
    )

    price: float = Field(
        ...,
        gt=0
    )

    quantity: int = Field(
        ...,
        ge=0
    )


class ProductUpdate(BaseModel):
    name: str = Field(..., min_length=2)

    sku: str = Field(
        ...,
        min_length=2
    )

    price: float = Field(
        ...,
        gt=0
    )

    quantity: int = Field(
        ...,
        ge=0
    )


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    quantity: int

    class Config:
        from_attributes = True
