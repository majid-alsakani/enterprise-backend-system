from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {
        "message": "login success",
        "token": "example_jwt_token_for_demonstration",
        "status": "authorized"
    }
