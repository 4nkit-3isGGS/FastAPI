from pydantic import BaseModel, Field

class MenuItems(BaseModel):
    id: int
    item: str
    price: int
    category: str
    description: str
    available: bool

class MenuResponse(BaseModel):
    status: str = "Success"
    count: int
    items: list[MenuItems]

