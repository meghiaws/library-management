FROM python:3.10.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    WORKDIR=/home/appuser/web/

WORKDIR ${WORKDIR}

RUN mkdir ${WORKDIR}/staticfiles

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

RUN pip install --upgrade pip && \
    pip install poetry

COPY pyproject.toml poetry.lock ${WORKDIR}

# Docker containers are already isolated and don't need virtual environments.
# so we turn off the creation of virtualenv.
RUN poetry export -f requirements.txt --output requirements.txt --dev && \
    pip install -r requirements.txt

COPY . ${WORKDIR}

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser ${WORKDIR}

USER appuser

EXPOSE 8000
