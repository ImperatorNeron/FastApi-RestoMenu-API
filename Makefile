DC = docker compose
DL = docker logs
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app

.PHONY: app
app:
	${DC} -f ${APP_FILE} up --build -d

.PHONY: app-logs
app-logs:
	${DL} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} down