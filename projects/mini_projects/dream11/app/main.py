from fastapi import FastAPI
from app.routs.teams_routs import router as team_router

app=FastAPI()
app.include_router(team_router)

# model



@app.get("/health")
def get_health():
  return{
    "status":"ok"
  }
