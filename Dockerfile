FROM python:3.10-slim

WORKDIR /mirabot


COPY requitements.txt /mirabot/requirements.txt
COPY . /mirabot/

CMD python3 /mirabot/app.py

