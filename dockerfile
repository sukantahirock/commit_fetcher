FROM python:3.10-slim
RUN apt-get update
RUN apt-get install requests
COPY . /fetcher.py
ENTRYPOINT ["python3", "fetcher.py"]