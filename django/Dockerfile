FROM python:3.9.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg libffi-dev \
    && pip install -r requirements.txt \
    && apk del build-deps

COPY ./entrypoint-dev.sh .

COPY . .

EXPOSE 8005

ENTRYPOINT ["./entrypoint-dev.sh"]
