from fastapi import FastAPI

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

