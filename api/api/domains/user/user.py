from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
  id: int
  name: str
  status: int = 0
  email: str
  password: str
  created_at: Optional[int] = None,
  updated_at: Optional[int] = None,

