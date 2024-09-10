DC = docker compose
DL = docker logs

APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app

STORAGES_FILE = docker_compose/storages.yaml
STORAGES_CONTAINER = postgresql-container

ENV = --env-file .env

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: storages-logs
storages-logs:
	${DL} ${STORAGES_CONTAINER} -f

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} ${ENV} down

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: app-logs
app-logs:
	${DL} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} down

