from sqlalchemy.orm import Session
import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        customer_name=order.customer_name,
        product_name=order.product_name,
        quantity=order.quantity,
        price=order.price
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def list_orders(db: Session, skip: int = 0, limit: int = 10, status: str = None):
    query = db.query(models.Order)
    if status:
        query = query.filter(models.Order.status == status)
    return query.offset(skip).limit(limit).all()

def update_order_status(db: Session, order_id: int, status: str):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order 