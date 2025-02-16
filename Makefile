build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down && docker-compose up -d

logs:
	docker compose logs -f 

ps:
	docker compose ps

start app:
	uvicorn main:app --reload

migrations:
		alembic revision --autogenerate

migrate:
	alembic upgrade head