from fastapi import FastAPI
from database import create_tables, get_session
from contextlib import asynccontextmanager
from routes import orders as order_routes
from routes import stats as stats_routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database Starting up...")
    yield
    print("Shutting Down Database...")

app = FastAPI(
    title="Dabbewalla",
    description="A Dabbewalla API for Mumbai Dabbe-Walla.",
    lifespan=lifespan
)

app.include_router(order_routes.router)
# app.include_router(stats_routes.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Dabbewalla API."
    }
