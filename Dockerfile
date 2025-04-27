FROM python:3.10-slim

WORKDIR /app
#COPY ./requirements.txt .
RUN apt update && apt install -y pkg-config
RUN pip install -U setuptools
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

RUN pip install mysqlclient flask_mysqldb flask

COPY ./ .
RUN mkdir /resource && chmod 777 /resource

EXPOSE 5000
CMD ["python", "app.py"]
