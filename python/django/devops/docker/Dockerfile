FROM python:3.10.4 as builder

COPY . /build

WORKDIR /build

RUN apt update && \
    apt install -y \
    libldap-common \
    libldap-dev \
    libsasl2-dev \
    libssl-dev \
    python3-dev \
    && pip install -r requirements.txt --no-cache-dir --target /build

FROM python:3.10.4-slim

ENV USER eosantigen

RUN adduser --system --no-create-home --disabled-password ${USER}

RUN apt update && \
    apt install sqlite3

USER ${USER}

WORKDIR /apps/devops-logbook

COPY --from=builder --chown=eosantigen:eosantigen /build/ .
COPY ./docker/entrypoint.sh /apps/devops-logbook/entrypoint.sh

ENTRYPOINT [ "/apps/devops-logbook/entrypoint.sh" ]