import re
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, Base64Bytes
import datetime
from base64 import b64encode
from uuid import UUID

class loginBody(BaseModel):
    email: str = Field()

class loginBodyConfirm(BaseModel):
    email: str = Field()
    otp: str = Field()

class user(BaseModel):
    id: int = Field(default=None)
    email: str = Field()
    api_key: str = Field()

class recipient(BaseModel):
    id: UUID = Field(default=None)
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

class goodCategory(BaseModel):
    id: int = Field(default=None)
    title: str = Field()
    description: str = Field()
    parent_id: 'Optional[int]' = Field(default=None)

class good(BaseModel):
    id: UUID = Field(default=None)
    name: str = Field()
    description: str = Field()
    price: int = Field(ge=0)
    categoryId: int = Field()

class paymentMethod(BaseModel):
    id: int = Field()
    title: str = Field()
    description: str = Field()

class deliveryMethod(BaseModel):
    id: int = Field()
    title: str = Field()
    description: str = Field()

class basketItem(BaseModel):
    id: UUID = Field()
    goodId: UUID = Field()
    count: int = Field()
    basket_id: UUID

class basket(BaseModel):
    id: UUID = Field(default="")
    user_id: UUID
    basketItems: list[basketItem] = Field(list())

class checkout(BaseModel):
    id: UUID
    user_id: int = Field()
    recipient_id: UUID = Field()
    basket_id: UUID = Field()
    paymentMethod_id: int = Field()
    deliveryMethod_id: int = Field()
    paymentTotal: int = Field()

class TransactionStatus(str, Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"

class Transaction(BaseModel):
    id: UUID = Field()
    created: datetime.datetime = Field()
    updated: datetime.datetime = Field()
    status: TransactionStatus = Field()
    amount: int = Field()
    checkout_id: UUID = Field()
    providerData: bool

