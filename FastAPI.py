# from fastapi import FastAPI
# app=FastAPI()
# @app.get("/")
# def Home():
#     return {"message":"Home page hy ya..."}
# @app.get("/profile")
# def Profile():
#     return {"message":"Profile page hy ya..."}
# @app.get("/contact")
# def Contact():
#     return {"message":"Contact page hy ya..."}
# @app.post("/login")
# def Login():
#     return {"message":"Login page hy ya..."}
# @app.put("/update")
# def Update():
#     return {"message":"Update page hy ya..."}
# @app.delete("/delete")
# def Delete():
#     return {"message":"Delete page hy ya..."}


# Methods:
# Get Method:
# Post Method:
# Put Method:
# Delete Method:


# Get: (Path and Query Parameters)
# Path parameters: User ID, Product ID, etc.
# Query parameters: Optional parameters, filters, etc.

# Path Parameters:
from fastapi import FastAPI
app=FastAPI()
@app.get("/User/{id}")
def user(id: int):
    return {"Message":"User page hy ya... ", "ID": id}
@app.get("/Order/{sort}/{date}/{price}")
def order(sort: int, date:str, price:float):
    return{"Message":"Order Details: ","Sort":sort,"Date": date, "price":price}

# Query Parameters:
from typing import Optional
@app.get("/person")
def personaldetails(fName:str,age: Optional[int]=10):
    return{"Message ":"Personal Information" , "Father Name":fName, "Age":age}


# POST:
# Path:
@app.post("/gya/{id}")
def postkrdi(id: Optional[int]):
    return {"Message":"YAAYAYYA","ID":id}
# Query:
@app.post("/oola")
def oye(name:str):
    return {"Message":"Hello,","Name":name}