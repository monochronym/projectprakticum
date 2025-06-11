from fastapi import APIRouter
from app.routers.goods import goodsRouter
from app.routers.users import usersRouter
from app.routers.goodsCategories import goodsCategoryRouter
from app.routers.basket import basketRouter, basketItemsRouter
from app.auth import authRouter
import base64
import uuid
import requests
from requests.auth import HTTPBasicAuth
from fastapi.responses import RedirectResponse
import json
api = APIRouter(prefix="/api/v1")

api.include_router(goodsRouter)
api.include_router(authRouter)
# api.include_router(usersRouter)
api.include_router(goodsCategoryRouter)
api.include_router(basketRouter)
api.include_router(basketItemsRouter)

@api.get('/payOrder')
async def payment(price:int):
    username = "1105152"
    password = "test_d7j4GCtpZdAHGD_R9GKTdE6GabPMyHsNTx8BQyeuIak"

    auth = HTTPBasicAuth(username, password)
    headers = {"Idempotence-Key": str(uuid.uuid4())}
    data = {"amount": {
       "value": str(float(price)),
       "currency": "RUB"
   },
   "capture": True,
   "confirmation": {
       "type": "redirect",
       "return_url": "test"
   },
   "description": "Заказ №" + str(uuid.uuid4()) +" (тест)",
   "metadata": {
       "order_id": "37"
   }
    }
    yoomoney_req = requests.post("https://api.yookassa.ru/v3/payments", headers=headers, json=data, auth=auth)
    dec = json.JSONDecoder()
    res = dec.decode(yoomoney_req.text)
    return RedirectResponse(url=res['confirmation']['confirmation_url'])