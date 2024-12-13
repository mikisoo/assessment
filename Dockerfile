FROM python:3.13.1-slim

ARG APP_DIR=/opt/docker/scripts
ENV APP_DIR=$APP_DIR
ENV USER=appuser

WORKDIR $APP_DIR

COPY lookup-cli.py $APP_DIR/lookup-cli.py
COPY people_data.yaml $APP_DIR/people_data.yaml

RUN groupadd -g 1000 $USER && \
    useradd -u 1000 -g 1000 $USER && \
    chmod +x $APP_DIR/lookup-cli.py

RUN pip install pyyaml 

USER $USER

ENTRYPOINT ["./lookup-cli.py"]