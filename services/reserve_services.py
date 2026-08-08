from fastapi import FastAPI, HTTPException
from db.database import get_db
from sqlalchemy import text
from schemas.user import User_ticket



def user_reserve(user,db):
    
    result=db.execute(
        text("UPDATE tickets SET quantity=quantity- :ticket WHERE event_name=:event_name AND quantity>=:ticket"),
        {
            "event_name":user.event_name,
            "ticket":user.quantity
        }
    )
    
    if result.rowcount == 0:
        db.rollback()
    # Raise an error or return a 400/409 HTTP status indicating sold out/insufficient tickets
        raise HTTPException(status_code=404,detail="tickets are not available")
    
    db.commit()
    
    return{
        "message":f"ticket are booked for {user.event_name}"
    }
    
    
def usermovie_slot(event_name,db):
    
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
    
    if user["quantity"]==0:
        raise HTTPException(
    status_code=404,
    detail={
        "slot":user["quantity"],
        "error": "Booking Unavailable",
        "messages":"Tickets for this event are sold out",
        "event_name": event_name,
        "status": "CLOSED"
    }
)
    
    return{
        "slot":user["quantity"]
    }
    

def userget_eventname(db):
    
    result=db.execute(
        text("SELECT event_name,quantity FROM tickets")
    )
    
    ticket=result.mappings().all()
    
    print(ticket)
     
    return{
        "event_name":ticket
    } 