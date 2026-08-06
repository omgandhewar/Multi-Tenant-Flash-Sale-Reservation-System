from fastapi import FastAPI, Depends, APIRouter, HTTPException
from db.database import get_db
from services.reserve_services import user_reserve, usermovie_slot, userget_eventname


router=APIRouter()


@router.post("/reserve")
def reserve(db=Depends(get_db)):
    return user_reserve(db)
    
    
@router.get("/movieslot/{event_name}")
def movie_slot(event_name,db=Depends(get_db)):
    return usermovie_slot(event_name,db)
  

@router.get("/event_name")
def get_eventname(db=Depends(get_db)):
    return userget_eventname(db)