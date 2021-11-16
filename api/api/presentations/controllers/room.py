from fastapi import APIRouter

router = APIRouter(
  prefix="/room",
  tags=["room",]
)


@router.get('/{roomId}')
async def getChatRoomByRoomId(roomId: str):
    return "Done"

@router.post('/')
async def createChatRoom():
  return "Created"

@router.put("/{roomId}")
async def updateChatRoomById(roomId:str):
    return "Updated"

@router.delete("/{roomId}")
async def deleteChatRoom(roomId:str):
  return "Deleted"

