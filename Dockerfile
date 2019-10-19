FROM python:3.7.5-alpine3.10
LABEL maintainer="Patrick Bucher <patrick.bucher@stud.hslu.ch>"

RUN apk add git alpine-sdk
RUN mkdir /dependencies /app

WORKDIR /dependencies
COPY requirements.txt /dependencies/
RUN pip install -r requirements.txt

ARG username
ARG password
RUN git clone https://"${username}":"${password}"@gitlab.enterpriselab.ch/JassBot/jass-kit.git && \
    cd /dependencies/jass-kit/source && \
    pip install .

WORKDIR /app
COPY hello.py /app

CMD python ./hello.py
