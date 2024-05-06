DC = docker compose
EXEC = docker exec -it
TESTS = pytest tests/
API_CONTAINER = fastapi-todo-api-1


.PHONY: build
build:
	${DC} up --build --remove-orphans

.PHONY: compose
compose:
	${DC} up --remove-orphans

.PHONY: migrate
migrate:
	${EXEC} ${API_CONTAINER} alembic upgrade head

.PHONY: unit-tests
unit-tests:
	${EXEC} ${API_CONTAINER} pytest tests/unit

.PHONY: e2e-tests
e2e-tests:
	${EXEC} ${API_CONTAINER} pytest tests/e2e

.PHONY: integration-tests
integration-tests:
	${EXEC} ${API_CONTAINER} pytest tests/integration

.PHONY: tests
tests:
	${EXEC} ${API_CONTAINER} pytest tests/
