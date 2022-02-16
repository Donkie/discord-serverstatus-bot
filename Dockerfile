
# Requirements
FROM python:3-alpine AS builder


RUN apk update && apk add \
    python3-dev \
    gcc \
    libc-dev

COPY requirements.txt /bot/
WORKDIR /bot
RUN pip install --user -r requirements.txt

# Run
FROM python:3-alpine

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONUNBUFFERED=1
COPY *.py /bot/
WORKDIR /bot
CMD [ "python", "main.py" ]
