FROM python:3.5-slim AS build-env
RUN apt-get update && apt-get install -y build-essential
COPY requirements.txt /
RUN pip install -r /requirements.txt

FROM gcr.io/distroless/python3
COPY --from=build-env /usr/local/lib/python3.5/site-packages /usr/local/lib/python3.5/site-packages
COPY --from=build-env /usr/local/lib/libpython3.5m.so /usr/local/lib/libpython3.5m.so
COPY --from=build-env /usr/local/lib/libpython3.5m.so.1.0 /usr/local/lib/libpython3.5m.so.1.0
COPY --from=build-env /usr/local/lib/libpython3.so /usr/local/lib/libpython3.so
COPY --from=build-env /usr/local/lib/pkgconfig /usr/local/lib/pkgconfig
ENV PYTHONPATH=/usr/local/lib/python3.5/site-packages
WORKDIR /app
ENTRYPOINT ["python"]
