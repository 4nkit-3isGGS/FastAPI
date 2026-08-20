from fastapi import FastAPI, Request, Response
import uvicorn

app = FastAPI(
    title= "Swiggy Order Services",
    description= (
        "Handles the Backend Servises of Swiggy delivery."
        " The API handle of all Orders"
    ),
    version= "1.2.0",
    docs_url= "/docs",
    redoc_url= "/redoc",
    openapi_url= "/openapi"

)

@app.get("/")
def read_root():
    """Root end-point ----> This is the Root endpoint"""
    # FastAPI converts this into .JSON automatically
    return {
        "message": "Welcome to Swiggy Order Services.",
        "status": "Healthy"
}

@app.get("/about")
def about():
    """This is API metadata"""

    return {
        "service": "Swiggy Order Service",
        "region": "ap-south-asia-1",
        "team": "backend-ult",
        "version": "1.2.2"
    }

@app.get("/orders", tags=["orders"])
def get_orders():
    """Gets the List of All orders"""
    return {
        "orders":[

        {"id": 1, "item": "Butter Chicken", "status": "delivered"},
        {"id": 2, "item": "Paneer Bhurji", "status": "preparing"},
        {"id": 3, "item": "Masala Chai", "status": "setting to priority"}

    ]
}

@app.get("/orders/status", tags=["orders"])
def get_order_status():
    """Gets the Status of orders"""
    return {
        "total_today": 2_45_78,
        "top_city": "Bengaluru"
    }

@app.get("/request-infos")
async def get_request_infos(request: Request):
    """Gets the raw requests object"""
    return {
        "method": request.method,
        "url": str(request.base_url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params)
    }

@app.get(
    "/orders/active",
    summary= "This GETS the orders that are currently active.",
    description= (
        "Returns all orders that are currently being prepared"
        " or out for delivery"
    ),
    tags= ["orders"],
    deprecated= False
)
def get_active_orders():
    """also can be seen in the docs"""
    return {
        "active_orders" : [
        {"id": 1, "item":"Butter Chicken", "status": "preparing"},
        {"id": 2, "item":"Masala Dosa", "status": "out for delivery"},
        {"id": 3, "item":"chowmein", "status": "preparing"}
        ]
    }