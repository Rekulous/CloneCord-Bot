FROM python:alpine
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
COPY gclone /usr/bin/
RUN chmod +x CloneCord.py
CMD [ "python3", "CloneCord.py"]
