from fastapi import APIRouter

router = APIRouter(
  prefix="/user",
  tags=["user"]
)

@router.get('/{userId}')
async def getUserByUserId(userId:str):
    return []

@router.post("/")
async def createUser(user:str):
  return "J"

@router.put('/{userId}')
async def updateUserById(userId:str):
    return None

@router.delete('/{userId}')
async def deleteUserById(roomId:str):
    return None


