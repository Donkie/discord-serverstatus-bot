FROM python:3-alpine

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /bot/

WORKDIR /bot

RUN pip install -r requirements.txt

COPY *.py /bot/

CMD [ "python", "main.py" ]
