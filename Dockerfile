FROM python:slim-bullseye
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y tini ca-certificates openssl && rm -rf /var/lib/apt/lists/*
COPY . .
COPY gclone /usr/local/bin/gclone
RUN chmod 0755 /usr/local/bin/gclone
RUN chmod +x CloneCord.py
CMD [ "python3", "CloneCord-Mac-Linux.py"]
