FROM python:3.11.2-alpine3.17

ENV WORKDIR /apps
# Leave APPDIR below with only its name, no relative path relations.
ENV APPDIR web_hook_slack_bridge
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $WORKDIR:${APPDIR}
ENV USER eosantigen

WORKDIR ${WORKDIR}

RUN apk --update add build-base && adduser -H -S -D -u 1000 ${USER} && chown -R ${USER} $WORKDIR

COPY . ${APPDIR}

USER ${USER}

RUN python -m pip install --no-cache-dir --target=$WORKDIR -r ${APPDIR}/requirements.txt

ENTRYPOINT [ "./bin/uvicorn", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info", "--app-dir", ".", "web_hook_slack_bridge:serve" ]

EXPOSE 8000