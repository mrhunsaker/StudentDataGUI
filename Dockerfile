# Universal Dockerfile for Docker and Podman (Ubuntu 24.04 + Python 3.12 + venv)
FROM ubuntu:24.04

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV PATH="/app/venv/bin:$PATH"
ENV NICEGUI_HOST=0.0.0.0
ENV NICEGUI_PORT=8080
ENV MPLCONFIGDIR=/tmp/matplotlib
ENV HOME=/app/home
ENV XDG_RUNTIME_DIR=/tmp/runtime
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    python3.12 \
    python3.12-dev \
    python3.12-venv \
    python3-pip \
    libcairo2-dev \
    libgirepository-2.0-0 \
    libgirepository-2.0-dev \
    gir1.2-girepository-2.0 \
    pkg-config \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    gobject-introspection \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Create symbolic links for python3.12
RUN ln -sf /usr/bin/python3.12 /usr/bin/python3 && \
    ln -sf /usr/bin/python3.12 /usr/bin/python

WORKDIR /app

# Create virtual environment and install Python dependencies
COPY requirements.txt .
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY StudentDataGUI/ ./StudentDataGUI/
COPY __init__.py .

# Create necessary directories with proper permissions
RUN mkdir -p /app/home/.cache/fontconfig \
             /app/data \
             /app/database \
             /app/logs \
             /tmp/matplotlib \
             /tmp/runtime && \
    chmod -R 755 /app && \
    chmod -R 777 /tmp/matplotlib /tmp/runtime

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD /app/venv/bin/python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080')" || exit 1

CMD ["/app/venv/bin/python", "-m", "StudentDataGUI"]
