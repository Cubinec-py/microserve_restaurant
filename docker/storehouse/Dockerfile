FROM python:3.8

COPY ./requirements.txt /

RUN pip install -r requirements.txt

COPY ./docker/storehouse/docker-entrypoint.sh ./docker/storehouse/wait-for-command.sh /
RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh

COPY ./storehouse/ /apps

WORKDIR /apps

EXPOSE 8001

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001", "--settings=core.settings.docker"]