from pydantic import BaseModel




class Usersignup(BaseModel):
    name:str
    email:str
    password:str


class Userlogin(BaseModel):
    email:str
    password:str


class User_ticket(BaseModel):
    event_name:str
    quantity:int