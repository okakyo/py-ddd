from abc import ABC, abstractclassmethod

class ChatRepository(ABC):

    @abstractclassmethod
    async def create():
        pass

    @abstractclassmethod
    async def update():
        pass

    @abstractclassmethod
    async def delete(userId:str):
      pass

