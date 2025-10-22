from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: int
    description: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
