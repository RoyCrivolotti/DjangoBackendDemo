FROM python:3.9-alpine3.13
LABEL maintainer="roycrivolotti"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Package postgresql-client is needed for the PostgreSQL adapter to run
    apk add --update --no-cache postgresql-client && \
    # The 3 packages below are needed for the PostgreSQL adapter to install, and not afterwards, hence the `--virtual` \
    # which creats a virtual dependency package called `.tmp-build-deps`
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
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
        django-user

#Updating the PATH env variable within the image, so that every Python command executed runs from the virtual env
ENV PATH="/py/bin:$PATH"

USER django-user