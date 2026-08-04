from fastapi import FastAPI, Depends, APIRouter, HTTPException
from db.database import get_db



auth_router=APIRouter()

@auth_router.post("/login")
def login(db=Depends(get_db)):
    
    return user_login()