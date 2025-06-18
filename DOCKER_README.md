# Student Data GUI - Docker/Podman Deployment Guide

This guide provides instructions for running the Student Data GUI application using Docker or Podman containers.

## Prerequisites

### For Docker
- Docker Engine 20.10 or later
- Docker Compose 2.0 or later

### For Podman
- Podman 3.0 or later
- podman-compose (will be automatically installed if missing)

## Quick Start

### Using the Start Script (Recommended)

The easiest way to get started is using the provided `start.sh` script:

```bash
# Make the script executable (if not already)
chmod +x start.sh

# Start the application
./start.sh start

# Start in background mode
./start.sh start -d

# Start with rebuild
./start.sh start -b

# View logs
./start.sh logs

# Stop the application
./start.sh stop

# Show help
./start.sh help
```

### Manual Docker Commands

```bash
# Build and start with Docker Compose
docker-compose up -d

# Or using docker compose (newer syntax)
docker compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Manual Podman Commands

```bash
# Build and start with Podman Compose
podman-compose up -d

# Or use the Podman-specific compose file
podman-compose -f podman-compose.yml up -d

# View logs
podman-compose logs -f

# Stop
podman-compose down
```

## Configuration Options

### Environment Variables

The following environment variables can be configured:

- `NICEGUI_HOST`: Host to bind to (default: 0.0.0.0)
- `NICEGUI_PORT`: Port to bind to (default: 8080)
- `PYTHONPATH`: Python path (default: /app)
- `MPLCONFIGDIR`: Matplotlib config directory (default: /tmp/matplotlib)

### Ports

- Default application port: `8080`
- Access the application at: `http://localhost:8080`

### Volumes

The application uses the following volumes for persistent data:

- `./data`: Application data storage
- `./database`: Database files
- `./logs`: Application logs (Podman only)

## File Structure

```
StudentDataGUI/
├── Dockerfile              # Standard Docker build file
├── Dockerfile.podman       # Podman-optimized build file
├── compose.yaml            # Main Docker Compose file
├── podman-compose.yml      # Podman-specific Compose file
├── docker-compose.override.yml  # Override configurations
├── start.sh               # Startup script for both engines
├── requirements.txt       # Python dependencies
└── StudentDataGUI/        # Application source code
```

## Container Engine Differences

### Docker
- Uses standard Docker networking
- Requires explicit user mapping for file permissions
- Standard volume mounts

### Podman
- Rootless by default
- Automatic user namespace mapping
- SELinux-compatible volume mounts (`:Z` flag)
- May require additional security options

## Troubleshooting

### Common Issues

1. **Permission Denied Errors**
   ```bash
   # For Docker, ensure proper user permissions
   sudo chown -R $USER:$USER ./data ./database

   # For Podman rootless, this is usually handled automatically
   ```

2. **Port Already in Use**
   ```bash
   # Change the port in compose file or use environment variable
   export NICEGUI_PORT=8081
   ./start.sh start
   ```

3. **Container Build Failures**
   ```bash
   # Clean rebuild
   ./start.sh clean
   ./start.sh start -b
   ```

4. **Podman Socket Issues**
   ```bash
   # Enable Podman socket (if needed)
   systemctl --user enable --now podman.socket
   ```

### Health Checks

The container includes health checks that verify the application is running:
- Interval: 30 seconds
- Timeout: 10 seconds
- Retries: 3
- Start period: 10-15 seconds

### Logs

View application logs:
```bash
# Using start script
./start.sh logs

# Manual Docker
docker-compose logs -f

# Manual Podman
podman-compose logs -f
```

## Development

### Building Custom Images

```bash
# Build with Docker
docker build -t student-data-gui .

# Build with Podman
podman build -t student-data-gui .

# Build Podman-optimized image
podman build -f Dockerfile.podman -t student-data-gui .
```

### Volume Mounts for Development

For development, you can mount the source code:

```bash
# Add to compose file volumes section:
- ./StudentDataGUI:/app/StudentDataGUI:ro
```

## Security Considerations

### Docker
- Container runs as non-root user (uid: 1000)
- Limited capabilities
- Read-only root filesystem where possible

### Podman
- Rootless containers by default
- User namespace isolation
- SELinux compatibility
- No privileged containers required

## Performance Tuning

### Resource Limits

Add resource limits to compose files:

```yaml
services:
  student-data-gui:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
```

### Tmpfs Mounts

For better performance, tmpfs mounts are configured for temporary directories:
- `/tmp`: 500M-1G
- `/var/tmp`: 100M

## Backup and Persistence

### Data Backup

```bash
# Backup data directory
tar -czf student-data-backup-$(date +%Y%m%d).tar.gz data/ database/

# Restore data
tar -xzf student-data-backup-YYYYMMDD.tar.gz
```

### Database Backup

```bash
# SQLite database backup
sqlite3 database/students20252026.db ".backup database/students20252026-backup.db"
```

## Support

For issues specific to containerized deployment:
1. Check container logs: `./start.sh logs`
2. Verify container status: `./start.sh status`
3. Try clean rebuild: `./start.sh clean && ./start.sh start -b`

For application-specific issues, refer to the main project documentation.
