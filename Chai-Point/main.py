from h11._abnf import status_code
from fastapi import FastAPI, Query, HTTPException
from models import MenuItems, MenuResponse
from data import menu_items

app = FastAPI(
    title="Chai Point Menu API",
    description= ("Reads only menu API for kiosk displays and Mobile App."),
    docs_url= "/docs",
    redoc_url= "/redoc", 
    version= "1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Chai Point Menu API!"}

@app.get("/menu", response_model= MenuResponse)
def get_menu(category: str | None= Query(None, description="Filter out menu items by Chai, Coffee, Food, Cold-Drinks ")):

    if category:
        filtered = [item for item in menu_items if item["category"].lower()==category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No item found in the menu with category: {category}")
        
        return MenuResponse(count=len(filtered), items= filtered)

    return MenuResponse(count=len(menu_items), items= menu_items)

@app.get("/menu/{item_id}", response_model= MenuItems)
def get_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item
    
    raise HTTPException (status_code= 404, detail=f"No item found in Menu with item_id: {item_id}")



