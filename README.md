# DjangoBackendDemo

Django project following [this Udemy course](https://udemy.com/course/django-python-advanced).

### Test

`docker compose run --rm app sh -c "python manage.py test"`

### View linter warnings

`docker compose run --rm app sh -c "flake8"`

### Run

- Create the `.env` file in the root of the project, using the `.env.sample` file as an example
- Use `docker compose build && docker compose up` to start the app
    - Access the sit through `http://127.0.0.1/:8000`
- Use `docker-compose run --rm app sh -c "python manage.py createsuperuser"` to create a new admin to log in to the
  admin page of the app (`0.0.0.0:8000/admin`)

**To run the production version locally:**

- First go to the `docker-compose-deploy.yaml` and modify the following
  line `ports: "80:8000"` to `ports: "8000:8000"`, since port `80` will probably be in use.
- Then run `docker compose -f docker-compose-deploy.yaml down`

### Develop

- Run `docker compose run --rm app sh -c "django-admin startproject {PROJECT_NAME} ."` to create a new project
- Later,
  use `docker compose run --rm app sh -c "python manage.py startapp {PROJECT_NAME}"` to create a new app within your
  project. [See docs regarding the difference between these two command here](https://docs.djangoproject.com/en/dev/ref/django-admin/).
    - Remember to add the new app to the `INSTALLED_APPS` list within `app/app/settings.py`
