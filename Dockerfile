ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:latest
FROM $BUILD_FROM

# Copy addon files
COPY run.sh /run.sh
COPY custom_component /app

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

