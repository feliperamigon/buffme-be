#Dockerfile

# Python Alpine as our base image
FROM python:alpine3.7
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY requirements.txt /

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

COPY app.py .

# Run gunicorn with the first “app” parameter as the module
CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "app:app"]