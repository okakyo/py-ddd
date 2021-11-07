from typing import Any, List
from ..usecases import *
from typing import TypedDict,List,Any
from datetime import datetime

class ReqBuyTickets(TypedDict):
	tickets: List[Any]
	created_at: datetime

def buyTickets(req:ReqBuyTickets):
	try:
		
		print("hello world")
	except:
		print("Error")
	return {
		"status":"ok",
		"data": {

			"people":0,
			"price":0
		}
		

	}

