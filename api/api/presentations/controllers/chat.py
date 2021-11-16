from fastapi import APIRouter

router = APIRouter(
  prefix="/chat",
  tags=["chat"]
)

@router.get('/')
async def getAllChats():
    pass

@router.get('/{chatId}')
async def getChatByChatId(chatId:str):
    pass

@router.post('/')
async def createChat():
    pass

@router.put('/{chatId}')
async def updateChat(chatId: str):
    pass

@router.delete('/{chatId}')
async def deleteChat(chatId:str):
    pass

