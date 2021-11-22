from pydantic import BaseModel

class ChatModel(BaseModel):
  title: str
  description: str
  created_at: int
  updated_at: int
