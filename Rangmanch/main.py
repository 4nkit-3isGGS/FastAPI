from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes import review as review_routes
from  models import no_review_found_handler, NoReviewFound

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database Starting up...")
    yield
    print("Shutting Down Database...")

app = FastAPI(
    title= "Rangmanch",
    description= "A Theatre review API for Pune Rangmanch.",
    lifespan=lifespan
)

app.include_router(review_routes.router)
app.add_exception_handler(NoReviewFound, no_review_found_handler)

@app.get("/")
def root():
    return {
        "message": "Welcome to Rangmanch Review API."
    }