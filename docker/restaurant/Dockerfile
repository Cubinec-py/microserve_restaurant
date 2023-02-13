FROM python:3.8

COPY ./requirements.txt /

RUN pip install -r requirements.txt

COPY ./docker/restaurant/docker-entrypoint.sh ./docker/restaurant/wait-for-command.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh

COPY ./restaurant/ /apps
WORKDIR /apps

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]