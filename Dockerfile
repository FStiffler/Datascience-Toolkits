FROM python:3.8

WORKDIR /app

RUN pip install -r requirements.txt

CMD python code/main.py
CMD python Task4.py
