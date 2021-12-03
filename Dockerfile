FROM python:3.8

WORKDIR /app

COPY requirements.txt .
COPY docker_entrypoint.sh . 
COPY code/*.py modules/

RUN pip install -r requirements.txt

ENTRYPOINT ["sh","docker_entrypoint.sh"]

CMD python modules/wandb_test.py
