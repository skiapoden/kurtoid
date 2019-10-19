FROM python:3.7.5-alpine3.10
LABEL maintainer="Patrick Bucher <patrick.bucher@stud.hslu.ch>"

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY fakekit/ /app/fakekit
COPY hello.py /app

EXPOSE 8000

CMD gunicorn hello:app --log-file=-
