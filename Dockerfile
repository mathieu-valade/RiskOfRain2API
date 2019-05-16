FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN mkdir /riskofrain2api
WORKDIR /riskofrain2api

ADD . /riskofrain2api/

RUN pip install -r requirements.txt
RUN python manage.py runserver