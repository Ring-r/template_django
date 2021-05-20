FROM python:3.8-slim-buster

RUN \
	export DEBIAN_FRONTEND=nointeractive && \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN \
	pip install --no-cache-dir -r requirements.txt && \
	rm requirements.txt

RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser/

COPY --chown=appuser . .

ENTRYPOINT []
CMD ["gunicorn", \
	"--access-logfile=-", \
	"--bind=0.0.0.0:8000", \
	"--error-logfile=-", \
	"--log-file=-", \
	"--log-level=debug", \
	"--threads=4", \
	"--worker-class=gthread", \
	"--worker-tmp-dir=/dev/shm", \
	"--workers=2", \
	"template_django.wsgi"]
