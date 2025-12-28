FROM python:3.12

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
COPY docker/fastapi/scripts /scripts
RUN chmod +x /scripts/entrypoint.sh

WORKDIR /code
COPY backend /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["/scripts/entrypoint.sh"]
