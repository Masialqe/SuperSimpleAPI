FROM python:3.9-alpine

WORKDIR /app

COPY ./requirements.txt /app/

RUN apk --no-cache add shadow \
    && addgroup -S api && adduser -S -G api api \
    && pip install --no-cache -r requirements.txt

COPY  . /app/

RUN chown -R api:api /app

USER api

EXPOSE 8000

CMD ["python", "-u", "main.py"]
