from jose import jwt
import uuid
from datetime import datetime, timedelta

SECRET_KEY="abc123"

ALGORITHM="HS256"

ACCESS_TOKEN_EXPIRE_TIME=30



def access_token(data:dict):
    
    to_encode=data.copy()
    
    token_expire_time=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    
    to_encode.update({"exp":token_expire_time})
    
    token=jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return token


def refresh_token(data:dict):
    
    to_encode=data.copy()
    
    token_expire_time=datetime.utcnow()+timedelta(days=7)
    
    jti={
        uuid.uuid4()
    }
    
    to_encode.update({
        "exp":token_expire_time,
        "jti":jti
    })
    
    token=jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return token

