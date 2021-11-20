FROM python:3.8

WORKDIR /app

COPY code/task4 *.py modules/
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN docker run --name=postgre_vol -d -v ~/postgre_vol:/var/lib/postgresql/data -p 5050:80 postgres

CMD python modules/main.py
CMD Task4.py
