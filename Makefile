install:
	python -m pip install -e ".[dev]"
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
test:
	pytest -q
lint:
	ruff check .
format:
	ruff format .
check:
	python -m compileall -q app tests && ruff check . && pytest -q
migrate:
	alembic upgrade head
docker-up:
	docker compose up --build -d
docker-down:
	docker compose down -v
