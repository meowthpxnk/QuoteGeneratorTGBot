FROM python:3.12.2-slim-bookworm

# install google chrome
RUN apt-get -y update
RUN apt-get install -y wget xvfb unzip
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# setup python application
WORKDIR /bot

COPY ./requirements.txt /telegram/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /telegram/requirements.txt

COPY ./app /bot/app
COPY ./static /bot/static
COPY ./run.py /bot/run.py

COPY ./entrypoint.sh /bot/entrypoint.sh
RUN chmod +x /bot/entrypoint.sh

ENTRYPOINT [ "sh", "entrypoint.sh" ]