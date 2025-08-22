FROM ubuntu:22.04
# Copy script
COPY entrypoint.sh /entrypoint.sh
# Grant execution permissions
RUN chmod +x /entrypoint.sh
# Entry point (we use 'sh', what will cause error)
ENTRYPOINT ["sh", "/entrypoint.sh"]
