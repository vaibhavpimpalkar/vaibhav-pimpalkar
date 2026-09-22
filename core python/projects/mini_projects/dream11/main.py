from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
  id:int
  username:str
  teams:list[str]

user=[{
  "id":10,
  "username":"Alice",
  "teams":["Team A","Team B"]
},
{
   "id":20,
    "username":"bob",
    "teams":["Team C","Team D"]
}]

@app.post("/user")
def create_user(new_user:User):
  user.append(new_user)
  return{
    "massage":"user created successfull",
    "user" : new_user
  }

@app.get("/users")
def get_user():
  return {
    "massage":user
  }

@app.get("/users/{user_id}")
def get_user(user_id:int):
  for i in user:
    if i["id"]==user_id:
      return {"user":i}
  return {"massage":"not found"}