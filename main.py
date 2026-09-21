from fastapi import FastAPI

users=["user1","user2","user3"]

app=FastAPI()
@app.get("/hello")
def say_hello():
  return {"msg":"hello"}

@app.get("/health")
def check_health():
  return {"status":"server is running!"}

@app.get("/users")
def get_users():
  return {"users":users}

@app.get("/users/{id}")
def get_users(id:int):
  return{
    "users":users[id]
  }

@app.post("/users/{name}")
def create_user(name:str):
  users.append(name)
  return{
    "message":f"user {name} created successfully"
  }