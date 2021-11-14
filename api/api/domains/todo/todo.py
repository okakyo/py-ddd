from pydantic import BaseModel

class TodoModel(BaseModel):
  title: str
  description: str
  created_at: int
  updated_at: int
