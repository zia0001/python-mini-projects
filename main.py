from fastapi import FastAPI         # framework to build apis
from pydantic import BaseModel      # helps in data validation
from typing import List


app = FastAPI()                     # an app instance of FastAPI class

class Tea(BaseModel):               #a schema/model of tea data (with validation)
  id: int
  name: str
  origin: str

teas: List[Tea] =[]                 # will store multiple Tea objects


@app.get("/")
def read_root():
   return("welcome here")

@app.get("/teas")
def get_teas():
  return teas

@app.post("/teas")
def add_tea(tea: Tea):                   # the request must have all Tea fields now
    teas.append(tea)                     # expect that the request sender will send tea
    return tea
                  

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
       if tea.id == tea_id:
          teas[index] = updated_tea
          return updated_tea
    return{"error":"Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
   for index, tea in enumerate(teas):
      if tea.id ==tea_id:
         deleted = teas.pop(index)
         return deleted
   return {"error": "Tea is not "}
   