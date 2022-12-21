# DjangoBackendDemo

Basic Django boilerplate.

### Test

### View linter warnings

`docker-compose run --rm app sh -c "flake8"`

### Run

`docker compose build && docker compose up`

### Develop

- Run `docker compose run --rm app sh -c "django-admin startproject {PROJECT_NAME} ."` to add a new project within `app/`.