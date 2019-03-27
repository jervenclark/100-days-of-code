FROM python:3.5-slim AS build-env
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app

FROM gcr.io/distroless/python3
COPY --from=build-env /app /app
COPY --from=build-env /usr/local/lib/python3.5/site-packages /usr/local/lib/python3.5/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.5/site-packages
WORKDIR /app
ENTRYPOINT ["python"]
