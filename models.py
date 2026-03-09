from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey
from db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email_id = Column(String(50))
    password = Column(String(255))
    user_age = Column(Integer)
    user_country = Column(String(50))
    role = Column(String(50))


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    product_desc = Column(Text)
    product_price = Column(Numeric)
    product_category = Column(String(100))
    product_discount_price = Column(Numeric)
    image_url = Column(Text)
    stock_quantity = Column(Integer)
    status = Column(String(50))
    brand = Column(String(50))


class Card(Base):
    __tablename__ = "card"

    card_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    card_type = Column(String(50))
    last_4 = Column(String(4))
    card_holder_name = Column(String(50))
    expiry_year = Column(Integer)