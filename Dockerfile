FROM python:3.9

WORKDIR /bot
COPY . .

RUN apt update -qqy \
    && apt-get install git curl python3-pip ut-dlp -y
    && apt install ffmpeg -qqy --no-install-recommends\
    && pip3 install -r requirements.txt

CMD python3 -m lib
