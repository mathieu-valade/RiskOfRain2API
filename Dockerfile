FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

WORKDIR /riskofrain2api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /riskofrain2api/

#CMD ["python","manage.py", "runserver"]
EXPOSE 8000
CMD ["gunicorn", "riskofrain2api.wsgi"]