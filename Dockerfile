FROM python:3.9.7-slim

MAINTAINER Tiaan Conradie

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

EXPOSE 5000
CMD ["python", "app.py", "-h", "0.0.0.0", "-p", "5000"]
