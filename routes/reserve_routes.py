from fastapi import FastAPI, APIRouter
from db.database import sessionlocal
from sqlalchemy import text
from schemas.user import User


router=APIRouter()


@router.post("/reserve")
def reserve(user:User):
    db=sessionlocal()
    
    result=db.execute(
        text("SELECT quantity FROM tickets WHERE quantity LIKE "),
        {
            "ticket":user.quantity
        }
    )
    
    user=result.fetchone()
    
    print(user)
    
    tickets=user[0]
        
    if tickets<user.quantity:
        return{
            "message":"tickets are not available"
        }
        
        
    return{
        "message":"ticket are available"
    }
    
    
@router.get("/movieslot/{event_name}")
def movie_slot(event_name):
    db=sessionlocal()
    
    result=db.execute(
        text("SELECT quantity FROM tickets WHERE event_name=:event_name"),
        {
            "event_name":event_name
        }
    )
    
    user=result.fetchone()
    
    quantity=user[0]
    
    return{
        "slot":quantity
    }