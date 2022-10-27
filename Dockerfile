#Dockerfile

# Python Alpine as our base image
FROM python:alpine3.10
RUN pip install -U pip
RUN pip install -U setuptools

ADD . /buffme-be
WORKDIR /buffme-be
# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Run gunicorn with the first “entrypoint” parameter as the module
CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "entrypoint:app"]