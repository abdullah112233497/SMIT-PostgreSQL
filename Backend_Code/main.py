# main.py
from fastapi import FastAPI
from sqlalchemy.orm import Session # ORM Session import karein
import model
from database import engine,Base

app = FastAPI() # 'API' capital karein

# Yeh line database mein tables create karti hai
# Isse pehle models ka import hona zaroori hai
model.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Message": "Home page"}