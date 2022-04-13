FROM python:3.8-buster

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN useradd -m bot && chown -R bot:bot /var/log/supervisor/ /var/run/ /etc/supervisor/
USER bot

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH="/home/bot/.poetry/bin:${PATH}"

WORKDIR /opt/scum-n-villainy/

COPY . ./

RUN poetry update
RUN poetry install


CMD ["supervisord"]
