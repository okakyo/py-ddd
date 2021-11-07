from fastapi import APIRouter
from ..services import payTickets
router = APIRouter()

@router.post("/buy")
async def buyTickets():
	return 
