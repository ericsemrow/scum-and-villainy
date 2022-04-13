FROM python:3.8-buster

RUN apt-get update && apt-get install -y supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN useradd -m bot
USER bot

WORKDIR /opt/scum-n-villainy/

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH="/bot/.poetry/bin:${PATH}"

COPY . ./

RUN poetry init --no-dev

CMD ["/usr/bin/supervisord"]
