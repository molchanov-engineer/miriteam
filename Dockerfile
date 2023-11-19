FROM python:3.10-alpine3.18
LABEL authors="Красноглазик"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /opt/program

WORKDIR /opt/program

COPY main.py ./main.py

ENTRYPOINT ["python", "./main.py"]