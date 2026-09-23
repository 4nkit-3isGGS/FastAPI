from fastapi import APIRouter, Depends
from models import ReadReview, Review, UpdateReview, ReviewCreate
from sqlmodel import Session, select, func
from database import get_session

router = APIRouter(prefix="/api/reviews", tags=["Reviews"])

@router.post("/", response_model= ReadReview)
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):
    db_review = Review(**review.model_dump())

    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review