from fastapi import APIRouter, HTTPException
from app.models import Challenge

router = APIRouter(prefix="/challenges", tags=["challenges"])

challenges = []

@router.get("/")  # pragma: no cover
def list_challenges():
    return challenges

@router.post("/", status_code=201)  # pragma: no cover
def create_challenge(challenge: Challenge):
    challenges.append(challenge)
    return challenge
