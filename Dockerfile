FROM python:3.11-slim

ARG INSTALL_REQUIREMENTS=False

WORKDIR /app

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && if [ "$INSTALL_REQUIREMENTS" = "true" ]; then pip install --no-cache-dir -r /app/requirements.txt; fi

COPY alembic.ini /app/alembic.ini
COPY app/migrations /app/app/migrations
COPY docker-entrypoint.sh /app/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
