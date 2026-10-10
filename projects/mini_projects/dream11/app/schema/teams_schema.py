from pydantic import BaseModel,Field

# team schema
class Team(BaseModel):
  id:int
  name:str=Field(example="my dream team",description="Enter the team",min_lenght=3,max_lenght=50)
  player:str