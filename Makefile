install:
	pip install -e '.[dev]'
test:
	pytest
lint:
	ruff check .
	mypy app
run:
	uvicorn app.main:app --reload
docker:
	docker compose up --build
