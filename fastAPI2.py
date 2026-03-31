from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Data(BaseModel):
    name:str
    age: int
    grade:str
@app.get("/")
def home():
    return {"Message":"Home page"}
@app.post("/db")
def database(data:Data ):
    return {"Data":data}