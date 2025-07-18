FROM python:3.10-slim
RUN pip install requests
COPY fetcher.py .
ENTRYPOINT ["python3", "fetcher.py"]