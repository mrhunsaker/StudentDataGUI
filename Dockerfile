# Stage 1: Build stage
FROM python:3.11-slim as builder

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
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /build

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Clone the repository
RUN git clone https://github.com/mrhunsaker/StudentDataGUI .

# Install dependencies
RUN pip install --no-cache-dir nicegui && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.11-slim

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
    && rm -rf /var/lib/apt/lists/*

# Copy application from builder
COPY --from=builder /build /app

# Create necessary directories and config files
RUN mkdir -p /root/Documents/StudentDatabase/StudentDataFiles \
    /root/Documents/StudentDatabase/errorLogs

# Create initial roster.txt file
RUN echo "'DonaldChamberlain','StudentOne','StudentTwo','StudentN'" > /root/Documents/roster.txt

# Create workingdirectory config file
RUN echo 'if os.name == "nt":\n\
    try:\n\
        tmp_path = Path(os.environ["USERPROFILE"]).joinpath("/root", "Documents")\n\
        Path.mkdir(tmp_path, parents=True, exist_ok=True)\n\
        USER_DIR = Path(tmp_path)\n\
    except NameError as e:\n\
        print(f"{e}\\n Cannot find %USERPROFILE")\n\
elif os.name == "posix":\n\
    try:\n\
        tmp_path = Path("/root/Documents")\n\
        Path.mkdir(tmp_path, parents=True, exist_ok=True)\n\
        USER_DIR = Path(tmp_path)\n\
    except NameError as e:\n\
        print(f"{e}\\n Cannot find $HOME")\n\
return USER_DIR' > /root/Documents/workingdirectory

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH"
ENV NICEGUI_HOST=0.0.0.0
ENV HOME=/root
ENV PYTHONPATH=/app

# Expose the default NiceGUI port
EXPOSE 8080

# Create volume mount points for persistent data
VOLUME ["/root/Documents/StudentDatabase"]

# Set the entrypoint
ENTRYPOINT ["python", "-m", "StudentDataGUI.main"]
