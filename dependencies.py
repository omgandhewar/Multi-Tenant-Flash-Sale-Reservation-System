from fastapi import FastAPI, Depends, Request, HTTPException
from jose import jwt, JWTError
from sqlalchemy import text
from utils.jwt import SECRET_KEY, ALGORITHM
from db.database import get_db



def get_current_user(request:Request,db=Depends(get_db)):
    
    token=request.cookies.get("access_token")
    
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Not Authenticated"
        )
    
    try:
        payload=jwt.decode(
        token,
        SECRET_KEY,
        algorithms=ALGORITHM
       )
    
        user_id=payload.get("user_id")
    
        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Not Authenticated"
            )
    
    except JWTError:
        
        raise HTTPException(
            status_code=401,
            detail="invalid token"
        )
        
    
    result=db.execute(
        text("SELECT id FROM users id=user_id"),
        {
            "user_id":user_id
        }
    )
    
    user=result.fetchone()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
        
    return user
    