FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --no-cache -r requirements.txt

COPY  . /app/

EXPOSE 8000

CMD ["python", "-u", "main.py"]
