up:
	docker compose up
build-up:
	docker compose up  --build

down:
	docker compose down

sql:
	docker compose exec db psql -U user 

log:
	docker compose logs
