# Buffme API

## Requirements

  - GCP permissions to read/write Bigquery and Storage (environment variable `GOOGLE_APPLICATION_CREDENTIALS`)

## Installation

```
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```
source venv/bin/activate
python main.py
```

## Usage

Simple ping:

```python
>>> import requests
>>> requests.get('http://0.0.0.0:5000/ping')
<Response [204]>
```