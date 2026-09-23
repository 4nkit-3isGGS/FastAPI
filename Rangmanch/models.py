from sqlalchemy import table
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

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

