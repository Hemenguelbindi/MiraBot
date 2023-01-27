FROM python:3.10-slim

WORKDIR /mirabot


COPY requirements.txt /mirabot/requirements.txt
RUN pip install -r requirements.txt
COPY . /mirabot/



