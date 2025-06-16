# Use Python 3.11 slim base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV NICEGUI_HOST=0.0.0.0
ENV NICEGUI_PORT=8080
ENV MPLCONFIGDIR=/tmp/matplotlib
ENV HOME=/tmp/home

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2-dev \
    libgirepository1.0-dev \
    pkg-config \
    python3-dev \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    gobject-introspection \
    sqlite3 \
    libsqlite3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY StudentDataGUI/ ./StudentDataGUI/
COPY __init__.py .

# Create necessary directories and set permissions
RUN mkdir -p /tmp/matplotlib /tmp/home/.cache/fontconfig /app/data && \
    chmod -R 777 /tmp/matplotlib /tmp/home/.cache/fontconfig /app/data

# Create non-root user (optional, can be disabled for Podman rootless)
RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g 1000 -m -s /bin/bash appuser

# Set ownership of app directory
RUN chown -R appuser:appuser /app

# Switch to non-root user (comment out for rootless Podman if needed)
USER appuser

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080')" || exit 1

# Set the entrypoint
CMD ["python", "-m", "StudentDataGUI"]
