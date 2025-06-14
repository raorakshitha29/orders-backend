from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
from typing import List, Optional

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Order Management API"}

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.get("/orders/", response_model=List[schemas.Order])
def list_orders(skip: int = 0, limit: int = 10, status: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.list_orders(db=db, skip=skip, limit=limit, status=status)

@app.patch("/orders/{order_id}/status", response_model=schemas.Order)
def update_order_status(order_id: int, status: schemas.OrderUpdateStatus, db: Session = Depends(get_db)):
    updated_order = crud.update_order_status(db=db, order_id=order_id, status=status.status)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order 