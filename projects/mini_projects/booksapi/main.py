from fastapi import FastAPI

app=FastAPI()
books=[]
@app.get("/books")
def get_books():
  return{
    "data":books
  }

@app.get("/books/{id}")
def get_book_with_id(id:int):
  return{
    "data":books[id]
  }

@app.post("/books")
def create_books(name:str):
  books.append(name)
  return{
    "massage":f"{name} book created"
  }

@app.delete("/books/{id}")
def delete_book(id:int):
  books.pop(id)
  return{
    "massage":f"deleted"
  }

# @app.put("/books/{id}")
# def update_books(id:int):
