from fastapi import FastAPI, APIRouter
from db.database import sessionlocal
from sqlalchemy import text
from schemas.user import User


router=APIRouter()


@router.post("/reserve")
def reserve(user:User):
    db=sessionlocal()
    
    
    result=db.execute(
        text("SELECT quantity FROM tickets WHERE quantity=:ticket"),
        {
            "ticket":user.quantity
        }
    )
    
    user=result.fetchone()
        
    if user<user.quantity:
        return{
            "message":"tickets are not available"
        }
        
        
    return{
        "message":"ticket are available"
    }