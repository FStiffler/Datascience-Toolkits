FROM python:3.8

ADD main.py /

WORKDIR /model
COPY . /model

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
