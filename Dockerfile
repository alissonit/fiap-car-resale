FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

LABEL VENDOR="FIAP"
LABEL NAME="Fiap"
LABEL VERSION="1.0"
LABEL MAINTAINER="alissoncastroskt@gmail.com"

ENV APP_HOME "/opt/app"

# ENV FOR PYTEST
ENV DB_USER=postgres
ENV DB_PASSWORD=""
ENV DB_HOST=""
ENV DB_PORT=5432
ENV DB_NAME=fiapdbadmin
ENV DB_URI=""
ENV DB_MAX_POOL_SIZE=10

WORKDIR ${APP_HOME}

COPY . ./

RUN python -m pip install -r requirements.txt

ENV PORT 8000
EXPOSE $PORT

WORKDIR $APP_HOME

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]