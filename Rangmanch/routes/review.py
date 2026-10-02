from fastapi import APIRouter, Depends, Query
from models import ReadReview, Review, UpdateReview, ReviewCreate, no_review_found_handler, NoReviewFound
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


@router.get("/", response_model= list[ReadReview])
def get_reviews(
    play_name: str | None = Query(default= None, description="Filter by Play Name."),
    offset: int = Query(default= 0, ge=0, description="Number of reviews to skip."),
    limit: int = Query(default=10, ge=0, le=100, description="Number of reviews to show."),
    session: Session = Depends(get_session),
):
    query = select(Review).offset(offset).limit(limit)
    if play_name:
        query = query.where(Review.play_name == play_name)

    
    reviews= session.exec(query).all()
    return reviews



@router.get("/average/{play_name}")
def get_average_rating(play_name: str, session: Session = Depends(get_session)):

    result = session.exec(
        select(func.avg(Review.rating), func.count(Review.id)).where(Review.play_name == play_name)
    ).first()

    average_rating, total_reviews = result

    if total_reviews == 0 :
        raise NoReviewFound(play_name= play_name)
    
    return {
        "play_name": play_name,
        "average_rating": round(average_rating, 2),
        "total_reviews": total_reviews
    }

   
