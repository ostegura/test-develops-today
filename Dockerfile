# pull official base image
FROM python:3.7.1
# set work directory
WORKDIR ./newsBoard
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
# understand that this is for linux (I'm using Windows atm)
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev 
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .