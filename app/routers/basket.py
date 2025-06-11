import uuid

from fastapi import APIRouter
from app.dao.baskets import BasketDAO
from app.dao.basketItems import BasketItemDAO
from app.models.schemas import basket, basketItem
basketRouter = APIRouter(prefix="")
basketItemsRouter = APIRouter(prefix="")


@basketRouter.get("/basket/{basket_id}")
async def get_basket(basket_id):
    return await BasketDAO.find_by_id(basket_id)

@basketRouter.get("/basket")
async def get_basket_by_user_id(user_id):
    return await BasketDAO.find_by_filter(user_id=user_id)
@basketRouter.post("/basket")
async def create_basket(user_id:uuid.UUID):
    basket_id = uuid.uuid4()
    return await BasketDAO.add(id=basket_id, user_id=user_id)

@basketRouter.patch("/basket")
async def patch_basket(basket:basket):
    return BasketDAO.update(basket.dict(),**basket.dict())

@basketRouter.delete("/basket")
async def delete_basket(basket_id: str):
    return BasketDAO.delete( False, id=basket_id)

@basketItemsRouter.get("/basketItem/")
async def get_basketItems(basket_id):
    return await BasketItemDAO.find_all(basket_id=basket_id)


@basketItemsRouter.post("/basketItem")
async def create_basketItems(good_id: str, goods_count: int, basket_id: str):
    basketItem_obj = basketItem(id=uuid.uuid4(), goodId=good_id, count=goods_count, basket_id=basket_id)
    return await BasketItemDAO.add(**basketItem_obj.dict())

@basketItemsRouter.patch("/basketItem")
async def patch_basketItems(basketItems:basketItem):
    return await BasketItemDAO.update(basketItems.dict(),**basketItems.dict())

# @basketItemsRouter.delete("/basketItem")
# async def delete_basketItems(basketItem_id:str):
#     return BasketItemDAO.delete( False,id=basketItem_id)

@basketItemsRouter.delete("/basketItem")
async def delete_basketItems_by_goodId(good_id:str, basket_id:str):
    return await BasketItemDAO.delete( False,goodId=good_id, basket_id=basket_id)