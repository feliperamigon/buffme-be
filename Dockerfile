#Dockerfile

# Python Alpine as our base image
FROM python:alpine3.7
RUN pip install -U pip
RUN pip install -U setuptools

ADD . /buffme-be
WORKDIR /buffme-be
# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

CMD python entrypoint.py