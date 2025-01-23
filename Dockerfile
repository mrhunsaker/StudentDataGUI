# Stage 1: Build stage
FROM python:3.11-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libcairo2-dev \
    pkg-config \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    git \
    gobject-introspection \
    libgirepository1.0-dev \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /build

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install nicegui

# Copy application source code
COPY StudentDataGUI /build/StudentDataGUI

# Stage 2: Runtime stage
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libcairo2 \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    gobject-introspection \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /opt/venv

# Copy application source code from the builder stage
COPY --from=builder /build /app

# Update UID/GID range in login.defs
RUN sed -i 's/^UID_MIN.*/UID_MIN 524288/' /etc/login.defs && \
    sed -i 's/^UID_MAX.*/UID_MAX 589823/' /etc/login.defs && \
    sed -i 's/^GID_MIN.*/GID_MIN 524288/' /etc/login.defs && \
    sed -i 's/^GID_MAX.*/GID_MAX 589823/' /etc/login.defs

# Add a user with the specified UID and GID, ignoring warnings
#RUN groupadd --gid 524288 appuser && \
#    useradd --no-log-init --uid 524288 --gid 524288 --home-dir /home/appuser --create-home appuser

# Switch to the new user
# USER appuser
# Expose the default NiceGUI port
EXPOSE 8080

# Define the volume for persistent storage
VOLUME ["/home/appuser/Documents/StudentDatabase"]

# Set the entrypoint for the application
ENTRYPOINT ["sh", "-c", "pip show nicegui && python -m StudentDataGUI.main"]

