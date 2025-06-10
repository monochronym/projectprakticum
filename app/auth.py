import uuid

from starlette import status
from starlette.responses import JSONResponse

from app.models.schemas import loginBody, loginBodyConfirm, user
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import get_auth_data
from fastapi import APIRouter, HTTPException
from app.dao.users import UserDAO
from fastapi.responses import RedirectResponse
# from config import redis_client
import smtplib
from email.mime.text import MIMEText
import random
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)




def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt


authRouter = APIRouter(prefix="/auth")


@authRouter.post("/register")
async def register_user(loginBodyrequest: loginBody):
    user = await UserDAO.find_by_filter(email=loginBodyrequest.email)
    if user:
        content = {"message": "User found"}
        response = JSONResponse(content=content)
        return response
    user_dict = loginBodyrequest.dict()
    user_dict['password'] = get_password_hash(loginBodyrequest.password)
    user_dict["api_key"] = create_access_token(user_dict)
    user_dict["id"] = uuid.uuid4()
    user_create = await UserDAO.add(**user_dict)
    content = {"api_key":str(user_create.api_key)}
    response = JSONResponse(content=content)
    response.set_cookie(key="api_key", value=str(user_create.id))
    return response


@authRouter.post("/login")
async def authenticate_user(loginBodyrequest: loginBody):
    user = await UserDAO.find_by_filter(email=loginBodyrequest.email)
    if not user or verify_password(plain_password=loginBodyrequest.password, hashed_password=user.password) is False:
        content = {"message": "User not found"}
        response = JSONResponse(content=content)
        return response
    content = {"api_key":str(user.id)}
    response = JSONResponse(content=content)
    response.set_cookie(key="api_key", value=str(user.id))
    return response

# async def login(loginBody: loginBody):
#     user = await UserDAO.find_by_filter(**loginBody.dict())
#     if user == None:
#         otp = random.randint(1000, 9999)
#         msg = MIMEText(f"Code to register in site is {otp}")
#         msg['Subject'] = 'Login access'
#         msg['From'] = 'paiy180624@gmail.com'
#         msg['To'] = loginBody.email
#
#         # Send the message via our own SMTP server, but don't include the
#         # envelope header.
#         s = smtplib.SMTP("localhost", 1025)
#         s.sendmail('paiy180624@gmail.com', [loginBody.email], msg.as_string())
#         s.quit()
#         redis_client.setex(f"{loginBody.email}", timedelta(minutes=5), value=f"{otp}")
#         return RedirectResponse("/confirm_user")
#     response = RedirectResponse("/")
#     response.set_cookie(key="api_key", value=user.id)
#     return response
#
# @authRouter.post("/confirm")
# async def confirm(loginbodyconfirm: loginBodyConfirm):
#     otp = redis_client.get(loginbodyconfirm.email).decode("utf-8")
#     if loginbodyconfirm.otp == otp:
#         api_key = create_access_token(loginbodyconfirm.dict())
#         user_obj = user(email=loginbodyconfirm.email, api_key=api_key)
#         response = await UserDAO.add(**user_obj.dict())
#         return response
#     else: return None