from datetime import datetime 

"""
関数：日時判定についてのUseCase を定義
"""

def is_holiday(created_at: datetime)->bool:
	return created_at.weekday()>4

# TODO: 映画館の開館日時を確認する（ 0時の判定も考慮すること ）
def is_night(created_at:datetime)->bool:
	print(created_at.hour)
	return created_at.hour>=20


def is_movie_day(created_at:datetime) ->bool:
	return created_at.day==1
