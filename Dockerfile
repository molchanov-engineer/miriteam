FROM python:3.5-alpine3.10
LABEL authors="Красноглазик"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /opt/program

WORKDIR /opt/program

COPY .env ./.env

COPY main.py ./main.py

ENTRYPOINT ["python", "./main.py"]