from fastapi import FastAPI
from datetime import date
app=FastAPI()

@app.get("/today")
def today():
  return{
    "date":str(date.today())
  }