from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RegisterRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(data: RegisterRequest):
    return {"msg": f"Registered {data.email} (simulated)"}
