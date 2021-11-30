FROM python:3
ENV PYTHONUNBUFFERED=1 RAPIDAPIKEY=8659b00868mshb462f0af996f52cp12343ejsnc12aba3fe4db
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/