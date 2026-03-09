from pydantic import BaseModel

# ---------------- USERS ----------------
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email_id: str
    password: str
    user_age: int
    user_country: str
    role: str

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    user_country: str | None = None

class UserResponse(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email_id: str
    user_age: int
    user_country: str
    role: str

    class Config:
        from_attributes = True

# ---------------- PRODUCTS ----------------
class ProductSchema(BaseModel):
    product_name: str
    product_desc: str
    product_price: float

class ProductResponse(BaseModel):
    product_id: int
    product_name: str
    product_desc: str
    product_price: float
    product_category: str
    product_discount_price: float | None = None
    image_url: str | None = None
    stock_quantity: int
    status: str
    brand: str

    class Config:
        from_attributes = True

# ---------------- CARDS ----------------
class CardSchema(BaseModel):
    user_id: int
    card_type: str
    last_4: str
    card_holder_name: str
    expiry_year: int

class CardResponse(BaseModel):
    card_id: int
    user_id: int
    card_type: str
    last_4: str
    card_holder_name: str
    expiry_year: int

    class Config:
        from_attributes = True