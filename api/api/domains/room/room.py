from pydantic import BaseModel

class RoomModel(BaseModel):
  title: str
  description: str
  created_at: int
  updated_at: int
