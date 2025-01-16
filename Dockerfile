# Stage 1: Build stage
FROM python:3.10-slim as builder

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
    gir1.2-gtk-3.0 \
    libcairo2-dev \
    python3-cairo-dev \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Create directory for SQLite database
RUN mkdir -p /app/StudentDatabase

# Copy the students.db file to the desired directory
# RUN cp /app/students.db ~/Documents/StudentDatabase/students.db

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

# Add a non-root user for security
RUN useradd -ms /bin/bash appuser && chown -R appuser:appuser /app

# Set non-root user
USER appuser

# Copy the local StudentDataGUI folder into the image
COPY StudentDataGUI /build/StudentDataGUI

# Stage 2: Runtime stage
FROM python:3.10-slim

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set working directory
WORKDIR /app

# Install only required runtime dependencies
RUN apt-get update && apt-get install -y \
    libcairo2 \
    python3-gi \
    python3-gi-cairo \
    gir1.2-gtk-3.0 \
    gobject-introspection \
    libgirepository1.0-dev \
    gir1.2-gtk-3.0 \
    && rm -rf /var/lib/apt/lists/*

# Copy application from builder
COPY --from=builder /build /app

# Create necessary directories and config files
RUN mkdir -p /home/appuser/Documents/StudentDatabase/StudentDataFiles \
    /home/appuser/Documents/StudentDatabase/errorLogs

# Create the target directory
RUN mkdir -p /home/appuser/Documents/StudentDatabase/

# Copy the students.db file
COPY students.db /home/appuser/Documents/StudentDatabase/students.db

# Create initial roster.txt file
RUN echo "'DonaldChamberlain','StudentOne','StudentTwo','StudentN'" > /home/appuser/Documents/roster.txt

# Create workingdirectory config file
RUN echo 'if os.name == "nt":\n\
    try:\n\
        tmp_path = Path(os.environ["USERPROFILE"]).joinpath("/home/appuser", "Documents")\n\
        Path.mkdir(tmp_path, parents=True, exist_ok=True)\n\
        USER_DIR = Path(tmp_path)\n\
    except NameError as e:\n\
        print(f"{e}\\n Cannot find %USERPROFILE")\n\
elif os.name == "posix":\n\
    try:\n\
        tmp_path = Path("/home/appuser/Documents")\n\
        Path.mkdir(tmp_path, parents=True, exist_ok=True)\n\
        USER_DIR = Path(tmp_path)\n\
    except NameError as e:\n\
        print(f"{e}\\n Cannot find $HOME")\n\
return USER_DIR' > /home/appuser/Documents/workingdirectory

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"
ENV NICEGUI_HOST=0.0.0.0
ENV HOME=/root
ENV PYTHONPATH=/app/StudentDataGUI:$PYTHONPATH

# Expose the default NiceGUI port
EXPOSE 8080

# Create volume mount points for persistent data
#VOLUME ["/home/appuser/Documents/StudentDatabase"]

# Set the entrypoint
ENTRYPOINT ["python", "-m", "StudentDataGUI.main"]