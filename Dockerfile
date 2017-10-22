FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

ADD . /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8000
