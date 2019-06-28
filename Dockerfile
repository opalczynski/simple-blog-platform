FROM python:3.7-alpine3.9 as application
ENV PYTHONUNBUFFERED 1
RUN set -e;

RUN apk update
RUN apk add --no-cache --virtual .build-deps \
    gcc linux-headers libc-dev make

WORKDIR /app

RUN pip install pipenv

ADD Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system

RUN apk del .build-deps

ADD . /app/
CMD ["python", "-m", "sanic", "app.app", "--host=0.0.0.0", "--port=8031", "--workers=3"]
