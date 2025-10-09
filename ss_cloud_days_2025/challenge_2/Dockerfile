FROM ubuntu:22.04
RUN mkdir -p /data/utils/custom/scripts
COPY custom_script.sh /data/utils/custom/scripts/custom_script.sh
RUN chmod +x /data/utils/custom/scripts/custom_script.sh
ENTRYPOINT ["sh", "/data/utils/custom/scripts/custom_script.sh"]
