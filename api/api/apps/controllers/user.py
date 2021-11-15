from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def chatRoomLists():
    pass

@router.get('/${roomId}')
async def chatRoomByRoomId(roomId:str):
    pass


