from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# OrderStatus (Enum) -> preparing, picked_up, in_transit, delivered
class OrderStatus(str, Enum):
    PREPARING = "preparing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"

# Database table of Orders
class Orders(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_name: str
    delivery_address: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    status: OrderStatus = Field(default=OrderStatus.PREPARING)
    items: str

# schema for creating new orders
class OrderCreate(SQLModel):
    customer_name: str
    delivery_address: str
    items: str

# schema for updating orders
class OrderUpdate(SQLModel):
    status: Optional[OrderStatus] = None
    delivery_address: Optional[str] = None
    items: Optional[str] = None

# StatusLog schema
class StatusLog(SQLModel):
    order_id: int
    old_status: OrderStatus
    new_status: OrderStatus
    changed_at: datetime = Field(default_factory=datetime.now)
    
class ListOrders(SQLModel):
    id: int
    customer_name: str
    delivery_address: str
    created_at: datetime
    updated_at: datetime
    status: OrderStatus
    items: str



