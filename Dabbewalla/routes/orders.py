from fastapi import APIRouter, Depends, HTTPException, Query
from database import get_session
from models import Orders, OrderCreate, OrderStatus, OrderUpdate, StatusLog, ListOrders
from sqlmodel import Session, select

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Orders)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    db_order = Orders(**order.model_dump())

    session.add(db_order)
    session.commit()
    session.refresh(db_order)

    return db_order


@router.get("/list", response_model=list[ListOrders])
def list_orders(
    offset: int = Query(default=0, description= "Number of orders to skip."),
    limit: int = Query(default=10, description= "Number of orders to show."),
    session: Session = Depends(get_session)
):
    query = select(Orders).offset(offset).limit(limit)
    orders = session.exec(query).all()
    
    return orders

 

    