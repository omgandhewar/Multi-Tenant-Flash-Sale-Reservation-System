from fastapi import FastAPI, Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import Usersignup, Userlogin
from db.database import get_db
from services.auth_services import user_login, user_signup



auth_router=APIRouter()


@auth_router.post("/signup")
def signup(user:Usersignup,db=Depends(get_db)):
    return user_signup(user,db)


@auth_router.post("/login")
def login(user:Userlogin,db=Depends(get_db)):
    token=user_login(user,db)
    
    response=JSONResponse(
        content={
            "message":"login successful"
        }
    )
    
    response.set_cookie(
        key="access_token",
        value=token["access_token"],
        httponly=True
    )
    
    response.set_cookie(
        key="refresh_token",
        value=token["refresh_token"],
        httponly=True
    )
    
    return response
    