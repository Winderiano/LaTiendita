from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Response, status, Depends, Path
from typing import List, Union
from src.config.config import SessionLocal
from src.models import models
from src.models.models import Product
from src.schemas.schemas import *
from src.crud import crud
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT


key = Fernet.generate_key()
f = Fernet(key)

pro = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()


# show Product por Id
def Read_Product_id(db: Session, product_id: Union[int, None, str]) -> Union[models.Product, None]:
    if product_id is None or not isinstance(product_id, int):
        return None
    
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

@pro.get("/products/{product_id}", tags=["Product"], response_model=ProductExit)
def Search_Product(product_id: Union[int, None, str], db: Session = Depends(get_db)):
    if product_id is None or not isinstance(product_id, int):
        raise HTTPException(status_code=400, detail="Invalid value for product_id")
    
    tblProduct = Read_Product_id(db, product_id)
    if tblProduct is None:
        raise HTTPException(status_code=404, detail="product not found")
    
    return tblProduct

#------------------------------------------------#

# show Products
def Read_Product(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

@pro.get("/products/", tags=["Product"], response_model=List[ProductExit])
def Show_Products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tblProduct = Read_Product(db, skip=skip, limit=limit)
    return tblProduct

#------------------------------------------------#

# Create Product
def Create_Product_Record(db: Session, Proe: ProductIntro):
    tblProduct = models.Product(product_name=Proe.product_name, provider_name=Proe.provider_name, product_price=Proe.product_price, stock_product=Proe.stock_product)
    db.add(tblProduct)
    db.commit()
    db.refresh(tblProduct)
    return tblProduct

@pro.post("/products/", tags=["Product"], response_model=ProductIntro)
def Create_Product(Proe: ProductIntro, db: Session = Depends(get_db)):
    return Create_Product_Record(db=db, Proe=Proe)




#--------------------------------------------------#

# Delete Product
def Delete_Product_Record(db: Session, product_id: Union[int, None, str]) -> Union[models.Product, None]:
    if product_id is None or not isinstance(product_id, int):
        return None
    
    tblProduct = Read_Product_id(db=db, product_id=product_id)
    db.delete(tblProduct)
    db.commit()
    
@pro.delete("/products/{product_id}", tags=["Product"], response_model=ProductExit)
def Delete_Product(product_id: Union[int, None, str], db: Session = Depends(get_db)):
    if product_id is None or not isinstance(product_id, int):
        raise HTTPException(status_code=400, detail="Invalid value for product_id")

    tblProduct = Read_Product_id(db, product_id=product_id)
    if not tblProduct:
        raise HTTPException(status_code=404, detail="No record found to delete")
    try:
        Delete_Product_Record(db=db, product_id=product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"cannot be deleted: {e}")
    return {"Deletion status":"Success"}


#------------------------------------------------------#

# Update Product
def Update_Product_Record(db: Session, Proe: ProductUpdate, product_id: Union[int, None, str]) -> Union[models.Product, None]:
    if product_id is None or not isinstance(product_id, int):
        return None

    tblProduct = Read_Product_id(db=db, product_id=product_id)
    if not tblProduct:
        raise HTTPException(status_code=404, detail="No record found to modify")
    tblProduct.product_name = Proe.product_name
    tblProduct.provider_name = Proe.provider_name
    tblProduct.product_price = Proe.product_price
    tblProduct.stock_product = Proe.stock_product
    db.commit()
    db.refresh(tblProduct)
    return tblProduct

@pro.put("/products/{product_id}", tags=["Product"], response_model=ProductUpdate)
def Update_Product(product_id: Union[int, None, str], Proe: ProductIntro, db: Session = Depends(get_db)):
    if product_id is None or not isinstance(product_id, int):
        raise HTTPException(status_code=400, detail="Invalid value for product_id")
    
    try:
        tblProduct = Update_Product_Record(db=db, product_id=product_id, Proe=Proe)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Can't Update: {e}")
    return tblProduct



'''
#--------------------------------------------------------#

# Modificar por Campo de registro
@pro.patch("/productos/{id_producto}", tags=["Producto"], response_model=ProductoSalida)
def modificar_producto_por_campo(id_producto: int, updateProducto: ProductoUpdate, db: Session = Depends(get_db)):
    tblProducto = db.query(models.Producto).filter(models.Producto.id_producto == id_producto)
    if not tblProducto.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado!")
    
    update_data = updateProducto.dict(exclude_unset=True)
    tblProducto.update(update_data)
    
    db.commit()
    db.refresh(tblProducto.first())
    
    return tblProducto.first()

    ---------------------------------------------------------

def leer_producto_id(db: Session, id_producto: int):
    return db.query(models.Producto).filter(models.Producto.id_producto == id_producto).first()

@pro.get("/productos/{id_producto}", tags=["Producto"], response_model=ProductoSalida)
def Mostrar_Producto(id_producto: int, db: Session = Depends(get_db)):
    tblProducto = leer_producto_id(db, id_producto)
    if tblProducto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return tblProducto

-----------------------------------------------------------




'''

