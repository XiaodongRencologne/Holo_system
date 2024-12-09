FROM python:3.10

COPY ./requirements.txt /tmp/requirements.txt
COPY deployments/vm-1/secrets/influxdb_token.txt /run/secrets/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./app /app
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
