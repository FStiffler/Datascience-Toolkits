FROM python:3.8

WORKDIR /app

COPY code/*.py modules/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python modules/main.py
