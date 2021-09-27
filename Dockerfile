FROM python:3.9.7-slim

MAINTAINER Tiaan Conradie

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

CMD ["python", "app.py"]
