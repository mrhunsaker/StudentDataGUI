#!/bin/bash

# Student Data GUI Startup Script
# Compatible with both Docker and Podman

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
CONTAINER_ENGINE=""
COMPOSE_FILE="compose.yaml"
PORT=8080
DETACH=false
BUILD=false
CLEAN=false

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to detect container engine
detect_container_engine() {
    if command -v podman >/dev/null 2>&1; then
        CONTAINER_ENGINE="podman"
        print_info "Detected Podman"
    elif command -v docker >/dev/null 2>&1; then
        CONTAINER_ENGINE="docker"
        print_info "Detected Docker"
    else
        print_error "Neither Docker nor Podman found. Please install one of them."
        exit 1
    fi
}

# Function to check if compose is available
check_compose() {
    if [ "$CONTAINER_ENGINE" = "podman" ]; then
        if command -v podman-compose >/dev/null 2>&1; then
            COMPOSE_CMD="podman-compose"
        elif command -v docker-compose >/dev/null 2>&1; then
            COMPOSE_CMD="docker-compose"
        else
            print_error "Neither podman-compose nor docker-compose found."
            print_info "Installing podman-compose..."
            pip3 install podman-compose || {
                print_error "Failed to install podman-compose"
                exit 1
            }
            COMPOSE_CMD="podman-compose"
        fi
    else
        if command -v docker-compose >/dev/null 2>&1; then
            COMPOSE_CMD="docker-compose"
        elif docker compose version >/dev/null 2>&1; then
            COMPOSE_CMD="docker compose"
        else
            print_error "Docker Compose not found"
            exit 1
        fi
    fi
}

# Function to create necessary directories
create_directories() {
    print_info "Creating necessary directories..."
    mkdir -p data database logs
    chmod 755 data database logs
    print_success "Directories created"
}

# Function to clean up containers and images
cleanup() {
    print_info "Cleaning up containers and images..."

    # Stop and remove containers
    $COMPOSE_CMD -f $COMPOSE_FILE down -v --remove-orphans 2>/dev/null || true

    # Remove images
    if [ "$CONTAINER_ENGINE" = "podman" ]; then
        podman rmi studentdatagui_student-data-gui 2>/dev/null || true
        podman rmi localhost/studentdatagui_student-data-gui 2>/dev/null || true
    else
        docker rmi studentdatagui_student-data-gui 2>/dev/null || true
    fi

    print_success "Cleanup completed"
}

# Function to build and start the application
start_app() {
    print_info "Starting Student Data GUI..."

    # Select appropriate compose file based on engine
    if [ "$CONTAINER_ENGINE" = "podman" ] && [ -f "podman-compose.yml" ]; then
        COMPOSE_FILE="podman-compose.yml"
        print_info "Using Podman-specific compose file"
    fi

    # Build if requested
    if [ "$BUILD" = true ]; then
        print_info "Building containers..."
        if [ "$CONTAINER_ENGINE" = "podman" ]; then
            $COMPOSE_CMD -f $COMPOSE_FILE build --no-cache
        else
            $COMPOSE_CMD -f $COMPOSE_FILE build --no-cache
        fi
    fi

    # Start services
    if [ "$DETACH" = true ]; then
        $COMPOSE_CMD -f $COMPOSE_FILE up -d
        print_success "Student Data GUI started in background"
        print_info "Access the application at: http://localhost:$PORT"
        print_info "View logs with: $0 logs"
    else
        print_info "Starting in foreground mode (Ctrl+C to stop)..."
        $COMPOSE_CMD -f $COMPOSE_FILE up
    fi
}

# Function to show logs
show_logs() {
    $COMPOSE_CMD -f $COMPOSE_FILE logs -f
}

# Function to stop the application
stop_app() {
    print_info "Stopping Student Data GUI..."
    $COMPOSE_CMD -f $COMPOSE_FILE down
    print_success "Student Data GUI stopped"
}

# Function to show status
show_status() {
    print_info "Container status:"
    $COMPOSE_CMD -f $COMPOSE_FILE ps
}

# Function to show help
show_help() {
    echo "Student Data GUI Startup Script"
    echo ""
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  start     Start the application (default)"
    echo "  stop      Stop the application"
    echo "  restart   Restart the application"
    echo "  logs      Show application logs"
    echo "  status    Show container status"
    echo "  clean     Clean up containers and images"
    echo "  help      Show this help message"
    echo ""
    echo "Options:"
    echo "  -d, --detach     Run in background (detached mode)"
    echo "  -b, --build      Force rebuild of containers"
    echo "  -p, --port PORT  Set port (default: 8080)"
    echo "  -e, --engine     Force container engine (docker|podman)"
    echo ""
    echo "Examples:"
    echo "  $0 start -d           # Start in background"
    echo "  $0 start -b           # Start with rebuild"
    echo "  $0 restart            # Restart the application"
    echo "  $0 logs               # Show logs"
}

# Parse command line arguments
COMMAND="start"
while [[ $# -gt 0 ]]; do
    case $1 in
        start|stop|restart|logs|status|clean|help)
            COMMAND=$1
            shift
            ;;
        -d|--detach)
            DETACH=true
            shift
            ;;
        -b|--build)
            BUILD=true
            shift
            ;;
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        -e|--engine)
            CONTAINER_ENGINE="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Main execution
case $COMMAND in
    help)
        show_help
        ;;
    clean)
        if [ -z "$CONTAINER_ENGINE" ]; then
            detect_container_engine
        fi
        check_compose
        cleanup
        ;;
    *)
        # Detect container engine if not specified
        if [ -z "$CONTAINER_ENGINE" ]; then
            detect_container_engine
        fi

        # Check compose availability
        check_compose

        # Create directories
        create_directories

        # Execute command
        case $COMMAND in
            start)
                start_app
                ;;
            stop)
                stop_app
                ;;
            restart)
                stop_app
                sleep 2
                start_app
                ;;
            logs)
                show_logs
                ;;
            status)
                show_status
                ;;
        esac
        ;;
esac
