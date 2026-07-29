from fastapi import FastAPI, Depends, APIRouter, HTTPException
from db.database import get_db
from sqlalchemy import text
from schemas.user import User


router=APIRouter()


@router.post("/reserve")
def reserve(user:User,db=Depends(get_db)):
    
    result=db.execute(
        text("SELECT quantity FROM tickets WHERE event_name=:event_name AND quantity>=:ticket "),
        {                     
            "event_name":user.event_name,
            "ticket":user.quantity
        }
    )
    
    user=result.fetchone()
    
    if not user:
        raise HTTPException(status_code=404,detail="tickets are not available")
    
    tickets=user[0]
        
    return{
        "message":"ticket are available"
    }
    
    
@router.get("/movieslot/{event_name}")
def movie_slot(event_name,db=Depends(get_db)):
    
    result=db.execute(
        text("SELECT quantity FROM tickets WHERE event_name=:event_name"),
        {
            "event_name":event_name
        }
    )
    
    user=result.mappings().first()
    
    if user is None:
        return{
            "message":"event is not available"
        }
    
    print(user)
    print(type(user))
    
    return{
        "slot":user["quantity"]
    }
    

@router.get("/event_name")
def get_eventname(db=Depends(get_db)):
    
    result=db.execute(
        text("SELECT event_name FROM tickets")
    )
    
    event_name=result.mappings().all()
    
    print(event_name)
     
    return{
        "event_name":event_name
    }