FROM python:3.12-slim

# Install system tools that benchmarks might need
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

