FROM python:3.12.5-slim as base

ENV PKGS_DIR=/install \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

FROM base as builder

RUN pip install --upgrade pip
RUN pip install poetry

RUN mkdir $PKGS_DIR
RUN mkdir /code

WORKDIR /code

COPY poetry.lock pyproject.toml /code/
# Generate requirements.txt from poetry files
RUN poetry export --without-hashes -f requirements.txt --output ./requirements.txt

# Install dependencies to local folder
RUN pip install --target=$PKGS_DIR -r ./requirements.txt
RUN pip install --target=$PKGS_DIR uvicorn

# Main image with service
FROM base
ARG SRC_PATH=./app
ARG LOG_LEVEL=debug

ENV LOG_LEVEL=${LOG_LEVEL}
ENV SERVICE_PORT=8000

ENV PYTHONPATH=/usr/local
COPY --from=builder /install /usr/local

COPY $SRC_PATH /app/
COPY ./config.yml /app/
WORKDIR /app

# Run service
CMD PYTHONPATH=$PYTHONPATH:/ uvicorn main:app --host 0.0.0.0 --port $SERVICE_PORT --workers 1 --log-level $LOG_LEVEL
