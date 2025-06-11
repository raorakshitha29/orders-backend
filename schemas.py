from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    customer_name: str
    product_name: str
    quantity: int
    price: float

class OrderCreate(OrderBase):
    pass

class OrderUpdateStatus(BaseModel):
    status: str

class Order(OrderBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
