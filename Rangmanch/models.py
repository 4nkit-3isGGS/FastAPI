from sqlalchemy import table
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi import Request

class Review(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    play_name: str = Field(index=True)
    reviewer_name: str 
    rating: float = Field(ge=0.0, le=10.0)
    comment: str
    created_at: datetime = Field(default_factory= datetime.now)

# Creating some validation, but not with Pydantic
class ReviewCreate(SQLModel):
    play_name: str
    reviewer_name: str 
    rating: float = Field(ge=0.0, le=10.0)
    comment: str

class ReadReview(SQLModel):
    id: int
    play_name: str 
    reviewer_name: str 
    rating: float = Field(ge=0.0, le=10.0)
    comment: str
    created_at: datetime 

class UpdateReview(SQLModel):
    rating: Optional[float] = Field(default=None, ge=0.0, le=10.0)
    comment: Optional[str]

# Creating some custom exceptions
class NoReviewFound(Exception):
    def __init__(self, play_name: str):
        self.play_name = play_name

class NoReviewFoundById(Exception):
    def __init__(self, id: int):
        self.id = id


# Exception handlers for custom exceptions
async def no_review_found_handler(request: Request, exc: NoReviewFound):
     return JSONResponse(
        status_code= 404,
        content= {
            "error": "No Review found!",
            "message": f"There are no reviews for {exc.play_name} yet.",
            "play_name": exc.play_name
        }
    )

async def no_review_found_by_id_handler(request: Request, exc: NoReviewFoundById):
    return JSONResponse(
        status_code= 404,
          content= {
            "error": "No Review found!",
            "message": f"No reviews are found for ID: {exc.id}",
            "id": exc.id
        }
    )