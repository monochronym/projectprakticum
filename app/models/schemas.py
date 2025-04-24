import re
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
import datetime
from uuid import UUID

class LoginBody(BaseModel):
    email: str = Field()

class LoginBodyConfirm(BaseModel):
    email: str = Field()
    otp: str = Field()

class User(BaseModel):
    id: int = Field(default=None)
    email: str = Field()
    api_key: str = Field()

class Recipient(BaseModel):
    id: int = Field(default=None)
    userId: int = Field()
    firstName: str = Field()
    lastname: str = Field()
    middleName: str = Field()
    address: str = Field()
    zipCode: str = Field()
    phone: str = Field()
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

class GoodCategory(BaseModel):
    id: int = Field(default=None)
    title: str = Field()
    description: str = Field()
    parentId: 'Optional[GoodCategory]' = Field(default=None)

class Good(BaseModel):
    id: int = Field(default=None)
    name: str = Field()
    description: str = Field()
    price: int = Field(ge=0)
    categoryId: int = Field()

class PaymentMethod(BaseModel):
    id: int = Field()
    title: str = Field()
    description: str = Field()

class DeliveryMethod(BaseModel):
    id: int = Field()
    title: str = Field()
    description: str = Field()

class BasketItem(BaseModel):
    id: int = Field()
    goodId: Good = Field()
    count: int = Field()

class Basket(BaseModel):
    id: UUID = Field()
    basketItems: list[BasketItem] = Field()

class Checkout(BaseModel):
    id: str
    user: User = Field()
    recipient: Recipient = Field()
    basket: Basket = Field()
    paymentMethod: PaymentMethod = Field()
    deliveryMethod: DeliveryMethod = Field()
    paymentTotal: int = Field()

class TransactionStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

class Transaction(BaseModel):
    id: str = Field()
    created: datetime.datetime = Field()
    updated: datetime.datetime = Field()
    status: TransactionStatus = Field()
    amount: int = Field()
    checkout: Checkout = Field()
    providerData: bool

