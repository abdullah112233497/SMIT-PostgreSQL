from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from db import engine, get_db

# Create tables in DB if not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Neon PostgreSQL API")

# ---------------- USERS ----------------
@app.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email_id=user.email_id,
        password=user.password,
        user_age=user.user_age,
        user_country=user.user_country,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.patch("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.first_name:
        db_user.first_name = user.first_name
    if user.last_name:
        db_user.last_name = user.last_name
    if user.user_country:
        db_user.user_country = user.user_country

    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# ---------------- PRODUCTS ----------------
@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

# ---------------- CARDS ----------------
@app.get("/cards", response_model=list[schemas.CardResponse])
def get_cards(db: Session = Depends(get_db)):
    cards = db.query(models.Card).all()
    return cards