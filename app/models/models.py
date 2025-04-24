from app.database import Base, uuid_pk, int_pk, str_pk, str_uniq, str_null_true
from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID

class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    api_key: Mapped[str_uniq]

class Recipient(Base):
    id: Mapped[int_pk]
    userId: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    firstName: Mapped[str]
    lastName: Mapped[str]
    middleName: Mapped[str]
    address: Mapped[str]
    zipCode: Mapped[str]
    phone: Mapped[str]

class GoodCategory(Base):
    id: Mapped[int_pk]
    title: Mapped[str]
    description: Mapped[str]
    parent_id: Mapped[int] = mapped_column(ForeignKey('goodcategorys.id'))

    children: Mapped["GoodCategory"] = relationship('GoodCategory')


class Good(Base):
    id: Mapped[int_pk]
    name: Mapped[str_uniq]
    description: Mapped[str]
    price: Mapped[int]
    categoryId: Mapped[int] = mapped_column(ForeignKey('goodcategorys.id'))


class BasketItem(Base):
    id: Mapped[int_pk]
    goodId: Mapped['Good'] = mapped_column(ForeignKey("goods.id"))
    count: Mapped[int]
    basket_id: Mapped[UUID] = mapped_column(ForeignKey("baskets.id"))
    basket: Mapped["Basket"] = relationship('Basket', back_populates="basket_items")

class Basket(Base):
    id: Mapped[int_pk]
    basket_items: Mapped[list["BasketItem"]] = relationship("BasketItem", back_populates="basket")

class DeliveryMethod(Base):
    id: Mapped[int_pk]
    title: Mapped[str]
    description: Mapped[str]

class PaymentMethod(Base):
    id: Mapped[int_pk]
    title: Mapped[str]
    description: Mapped[str]

class Checkout(Base):
    id: Mapped[str_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship()
    recipient_id: Mapped[int] = mapped_column(ForeignKey("recipients.id"))
    recipient: Mapped["Recipient"] = relationship()
    basket_id: Mapped[UUID] = mapped_column(ForeignKey("baskets.id"))
    basket: Mapped["Basket"] = relationship()
    payment_method_id: Mapped[int] = mapped_column(ForeignKey("paymentmethods.id"))
    payment_method: Mapped["PaymentMethod"] = relationship()
    delivery_method_id: Mapped[int] = mapped_column(ForeignKey("deliverymethods.id"))
    delivery_method: Mapped["DeliveryMethod"] = relationship()
    payment_total: Mapped[int]
