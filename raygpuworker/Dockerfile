FROM rayproject/ray:latest

# Install dependencies
RUN pip install --upgrade pip

# Setup startup script
COPY ./start.sh /

LABEL org.opencontainers.image.source="https://github.com/omnistrate-community/ray-cluster"
