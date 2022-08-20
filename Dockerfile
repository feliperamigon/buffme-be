#Dockerfile

# Python Alpine as our base image
FROM python:alpine3.7

COPY requirements.txt /

# Install dependencies from requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

COPY main.py .

# Run gunicorn with the first “app” parameter as the module
CMD ["gunicorn"  , "-b", "0.0.0.0:8888", "app:app"]