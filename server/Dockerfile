FROM python:latest
ADD server.py /serverdata/
WORKDIR /serverdata/
VOLUME servervol:/serverdata
CMD ["python", "server.py", "5555"]