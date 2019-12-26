FROM python:alpine3.10
WORKDIR /app
COPY requirements.txt .
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;
COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--py-autoreload=1", "--protocol=http", "-w", "wsgi:application"]