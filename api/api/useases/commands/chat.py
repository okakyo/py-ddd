from typing import Optional
from api.infra.nosql.mongo import ChatDB

def findRoomByRoomId(roomId: str):
  return ChatDB.room.find_one(roomId)

