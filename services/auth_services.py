from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from utils.jwt import create_access_token, create_refresh_token
from utils.password import hashed_password, verify_password



def user_signup(user,db):
    
    name=user.name
    email=user.email
    password=user.password
    
    result=db.execute(
        text("SELECT * FROM users WHERE email=:email"),
        {
            "email":email
        }
    )
    
    user_obj=result.fetchone()
    
    if user_obj:
        raise HTTPException(
            status_code=409,
            detail="user already exists"
        )
        
    
    hashed_password1=hashed_password(password)
    
    db.execute(
        text("INSERT INTO users(username,email,password) VALUES(:username,:email,:password)"),
        {
            "username":name,
            "email":email,
            "password":hashed_password1
        }
    )
    
    db.commit()
    
    return{
        "message":"user added successfully"
    }


def user_login(user,db):
    
    email=user.email
    password=user.password
    
    if not email or not password:
        raise HTTPException(
            status_code=400,
            detail="email and password are required"
        )  
        
    result=db.execute(
        text("SELECT id,email,password FROM users WHERE email=:email"),
        {
            "email":email
        }
    )

    user_obj=result.fetchone()
    
    
    if not user_obj:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    
    
    is_valid=verify_password(
        password,
        user_obj.password
    )

    if not is_valid:
        raise HTTPException(
            status_code=401,
            detail="invalid cresential"
        )
        
    access_token=create_access_token({
        "user_id":user_obj.id
    })
    
    refresh_token=create_refresh_token({
        "user_id":user_obj.id
    })
    
    return{
        "message":"login successful",
        "access_token":access_token,
        "refresh_token":refresh_token        
    }
        
    