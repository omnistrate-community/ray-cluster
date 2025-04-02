FROM python:3.9-slim

WORKDIR /app

# Copy the entrypoint script
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

LABEL org.opencontainers.image.source="https://github.com/omnistrate-community/ray-cluster"
