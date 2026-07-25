from fastapi import FastAPI, APIRouter
from db.database import sessionlocal
from sqlalchemy import text
from schemas.user import User


router=APIRouter()


@router.post("/reserve")
def reserve(user:User):
    db=sessionlocal()
    
    result=db.execute(
        text("SELECT quantity FROM tickets WHERE event_name=:event_name AND quantity>=:ticket "),
        {                     
            "event_name":user.event_name,
            "ticket":user.quantity
        }
    )
    
    user=result.fetchone()
    
    if not user:
        return{
            "message":"tickets are not available"
        }
    
    tickets=user[0]
        
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
    

@router.get("/event_name")
def get_eventname():
    db=sessionlocal()
    
    result=db.execute(
        text("SELECT event_name FROM tickets")
    )
    
    event_name=result.mappings().all()
    
    print(event_name)
     
    return{
        "event_name":event_name
    }