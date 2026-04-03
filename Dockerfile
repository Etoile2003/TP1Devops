FROM python:3.14-alpine

WORKDIR /app

COPY ./requirements.txt .
COPY ./Server.py .


RUN apk add --no-cache --update \
    rust cargo build-base


RUN pip install -r requirements.txt

EXPOSE 5050

ENTRYPOINT ["python", "Server.py"]