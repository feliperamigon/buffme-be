#Dockerfile

# Python Alpine as our base image
FROM python:alpine3.7
RUN pip install -U pip
RUN pip install -U setuptools

COPY requirements.txt /

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

COPY entrypoint.py .

CMD ["python3"  , "entrypoint.py"]