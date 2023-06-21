from sqlalchemy.orm import Session
from src.models.models import Product
from src.schemas.schemas import *

def show_products(db:Session,skip:int=0,limit:int=100):
    return db.query(Product).offset(skip).limit(limit).all()


def read_product_id(db:Session,product_id:int):
    return db.query(Product).filter(Product.product_id==product_id).first()


def create_product(db:Session,Proe:ProductExit):
    _produc = Product(product_name=Proe.product_name, provider_name=Proe.provider_name, product_price=Proe.product_price, stock_product=Proe.stock_product)
    db.add(_produc)
    db.commit()
    db.refresh(_produc)
    return _produc

def delete_product(db:Session,product_id:int):
    _product = read_product_id(db==db, product_id=product_id)
    db.delete(_product)
    db.commit()

def update_product(db:Session, product_id:int, product_name:str, provider_name:str, product_price:float, stock_product:int):
    _product = read_product_id(db=db, product_id=product_id)
    _product.product_name=product_name
    _product.provider_namer=provider_name
    _product.product_price=product_price
    _product.stock_product=stock_product
    db.commit
    db.refresh(_product)


'''
mostar productos
modificar producto
buscar producto
eliminar producto
crear producto
actualizar producto
lee producto
borrar producto

show products
modify product
search product
remove product
create product
update product
read product
delete product
'''

