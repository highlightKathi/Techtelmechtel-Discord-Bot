FROM python:3.7-slim

RUN apt update && apt install -y python3-pip git
RUN mkdir -p /opt/discord
RUN git clone https://github.com/Y0ngg4n/Techtelmechtel-Discord-Bot.git /opt/discord/techtelmechtel
RUN cd /opt/discord/techtelmechtel && pip install -r requirements.txt
WORKDIR /opt/discord/techtelmechtel
ENV DISCORD_TOKEN ""
CMD ["python /opt/discord/techtelmechtel/Main.py'"]