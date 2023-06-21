from pydantic import BaseModel, Field, validator
from typing import List, Generic, TypeVar, Optional
from pydantic.generics import GenericModel
from fastapi.responses import JSONResponse

T = TypeVar('T')


class ProductExit(BaseModel):
    product_id:     Optional[int]   = None
    product_name:   Optional[str]   = None
    provider_name:  Optional[str]   = None
    product_price:  Optional[float] = None
    stock_product:  Optional[int]   = None

    class Config:
        orm_mode = True

class ProductIntro(BaseModel):
    product_name:    str
    provider_name:   str
    product_price:    float
    stock_product:     int

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    product_name:   Optional[str]   = None
    provider_name:  Optional[str]   = None
    product_price:  Optional[float] = None
    stock_product:  Optional[int]   = None

    class Config:
        orm_mode = True   

class RequestProduct(BaseModel):
    parameter:  ProductIntro = Field(...)

    class Config:
        orm_mode = True 

class Response(GenericModel, Generic[T]):
    code:       str
    status:     str
    message:    str
    result:     Optional[T]

    class Config:
        orm_mode = True 
'''
class ProdUpdate(JSONResponse):
    media_type = "application/json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    product_name:   Optional[str]   = None
    provider_name:  Optional[str]   = None
    product_price:  Optional[float] = None
    stock_product:  Optional[int]   = None

    class Config:
        orm_mode = True       
'''