FROM ubuntu

RUN apt update && apt install python3 -y
WORKDIR /exercise
COPY server.pyc server.pyc
ENTRYPOINT python3 server.pyc