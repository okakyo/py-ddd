from pydantic import BaseModel

class UserModel(BaseModel):
  name: str
  status: int
  email: str
