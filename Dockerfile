FROM python:3.9-alpine3.13
LABEL maintainer="roycrivolotti"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Package postgresql-client is needed for the PostgreSQL adapter to run
    apk add --update --no-cache postgresql-client jpeg-dev && \
    # The 3 packages below are needed for the PostgreSQL adapter to install, and not afterwards, hence the `--virtual` \
    # which creates a virtual dependency package called `.tmp-build-deps`: See \
    # https://www.psycopg.org/docs/install.html and https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/issues/1
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # Deleting temp folder and virtual dependency package, for which we have no longer any use for
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    # Avoid using the root user to avoid security issues
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts && \
    chmod -R +x /scripts/run.sh

#Updating the PATH env variable within the image, so that every Python command executed runs from the virtual env
ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]
