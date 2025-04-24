from app.models.schemas import LoginBody, LoginBodyConfirm
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import get_auth_data
from fastapi import APIRouter
from app.dao.users import UserDAO
from fastapi.responses import RedirectResponse
from app.models.schemas import User
from app.config import redis_client
import smtplib
from email.mime.text import MIMEText
import random
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    to_encode.update({"exp": expire})
    auth_data = get_auth_data()
    encode_jwt = jwt.encode(to_encode, auth_data['secret_key'], algorithm=auth_data['algorithm'])
    return encode_jwt


authRouter = APIRouter(prefix="/auth")


@authRouter.post("/login")
async def login(loginBody: LoginBody):
    user = await UserDAO.find_by_filter(**loginBody.dict())
    if user == None:
        otp = random.randint(1000, 9999)
        msg = MIMEText(f"Code to register in site is {otp}")
        msg['Subject'] = 'Login access'
        msg['From'] = 'paiy180624@gmail.com'
        msg['To'] = loginBody.email

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP("localhost", 1025)
        s.sendmail('paiy180624@gmail.com', [loginBody.email], msg.as_string())
        s.quit()
        redis_client.setex(f"{loginBody.email}", timedelta(minutes=5), value=f"{otp}")
        return RedirectResponse("/confirm_user")
    response = RedirectResponse("/")
    response.set_cookie(key="api_key", value=user.api_key)
    return response

@authRouter.post("/confirm")
async def confirm(loginbodyconfirm: LoginBodyConfirm):
    otp = redis_client.get(loginbodyconfirm.email).decode("utf-8")
    if loginbodyconfirm.otp == otp:
        api_key = create_access_token(loginbodyconfirm.dict())
        user = User(email=loginbodyconfirm.email, api_key=api_key)
        response = await UserDAO.add(**user.dict())
        return response
    else: return None