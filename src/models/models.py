from sqlalchemy import Column, Integer, String, Numeric
from src.config.config import Base

class Product(Base):
    __tablename__ = "products"

    product_id =    Column(Integer,     primary_key=True,    index=True)
    product_name =  Column(String(50),  nullable=False,      unique=True)
    provider_name = Column(String(50),  nullable=False)
    product_price = Column(Numeric,     nullable=False)
    stock_product = Column(Integer,     nullable=False)