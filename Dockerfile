FROM python:3.10.10

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y upgrade && apt-get install -y --no-install-recommends  \
    jq \
    && apt -y autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /test/output /test/tests /test/docker /test/resources

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && rm /requirements.txt

COPY docker/docker-entrypoint.sh /test/docker/
RUN chmod +x /test/docker/docker-entrypoint.sh

COPY tests /test/tests
COPY resources /test/resources

ENV PYTHONPATH "${PYTHONPATH}:/test"

ENTRYPOINT ["/test/docker/docker-entrypoint.sh"]
