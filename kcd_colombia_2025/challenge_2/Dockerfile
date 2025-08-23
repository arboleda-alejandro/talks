FROM python:3.10-slim

RUN mkdir -p /data/custom/services/

RUN useradd -m svc_cloud

COPY server.py /data/custom/services/web.py

RUN chown svc_cloud:svc_cloud /data/custom/services/web.py

USER svc_cloud

EXPOSE 80
CMD ["python", "/data/custom/services/web.py"]
