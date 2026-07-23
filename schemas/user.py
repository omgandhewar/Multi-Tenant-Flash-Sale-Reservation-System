from pydantic import BaseModel


class User(BaseModel):
    event_name:str
    quantity:int