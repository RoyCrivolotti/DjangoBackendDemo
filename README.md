# DjangoBackendDemo

Basic Django boilerplate.

### Test

`docker compose run --rm app sh -c "python manage.py test"`

### View linter warnings

`docker compose run --rm app sh -c "flake8"`

### Run

`docker compose build && docker compose up`

### Develop

- Run `docker compose run --rm app sh -c "django-admin startproject {PROJECT_NAME} ."` to create a new project.
- Later,
  use `docker compose run --rm app sh -c "python manage.py startapp {PROJECT_NAME}"` to create a new app within your
  project. [See docs regarding the difference between these two command here](https://docs.djangoproject.com/en/dev/ref/django-admin/).
    - Remember to add the new app to the `INSTALLED_APPS` list within `app/app/settings.py`.