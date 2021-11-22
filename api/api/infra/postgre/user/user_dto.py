from typing import Union
from api.infra.postgre.database import DbBase
from sqlalchemy import Column, Integer, String
from api.domains.user import UserModel
from sqlalchemy.sql.schema import Index

class UserDTO(DbBase):
  "UserDTO is a data transfer object association with User Entity"
  __tablename__ = "user"

  id: Union[str,Column] = Column(String,primary_key=True, autoincrement=False)
  name: Union[str, Column] = Column(String,  nullable=False)
  email: Union[str, Column] = Column(String, nullable=False,unique=True)
  status: Union[int,Column] = Column(Integer, nullable=False, default=1)
  created_at: Union[int,Column] = Column(Integer, Index=True, nullable=False)
  updated_at: Union[int,Column] = Column(Integer, Index=True, nullable=False)

