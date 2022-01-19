FROM python:3.8-slim

RUN apt-get update
RUN apt-get -y install -qq --force-yes cron

ADD crontab /etc/cron.d/splitwise
RUN chmod 0644 /etc/cron.d/splitwise

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod 0744 app.py

CMD ["cron", "-f"]