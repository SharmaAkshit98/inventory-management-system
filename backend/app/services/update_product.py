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