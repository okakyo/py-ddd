from pydantic import BaseModel
from datetime import date, datetime
from abc import ABCMeta, abstractmethod
from utils import is_holiday,is_movie_day,is_night

class TicketModel(BaseModel):
	id: int
	course: int # 0~9
	created_at: datetime

class ITicket(metaclass =ABCMeta):
	@abstractmethod
	def res_price(self,req):
		pass 

	def is_night(self,created_at:datetime):
		return is_night(created_at)

	def is_holiday(self,created_at:datetime):
		return is_holiday(created_at)
		
	def is_movie_day(self,created_at:datetime):
		return is_movie_day(created_at)


