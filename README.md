```StudentDataGUI/README.md
# StudentDataGUI

Student Data Input GUI using NiceGUI and SQLite3 designed to be platform-independent. This guide also includes instructions for deploying the application using Docker or Podman containers.

---

## Table of Contents
1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
   - [Manual Setup](#manual-setup)
   - [Containerized Setup](#containerized-setup)
3. [File Structure](#file-structure)
4. [Development](#development)
5. [Troubleshooting](#troubleshooting)
6. [Support](#support)
7. [Accessibility](#accessibility)

---

## Overview

The StudentDataGUI application allows users to manage student data efficiently. It uses NiceGUI for the frontend and SQLite3 for the backend database. The application is designed to be deployed exclusively using containers, supporting both Docker and Podman for seamless and consistent operation.

---

## Setup Instructions

### Containerized Setup

#### Prerequisites
- **For Docker**: Docker Engine 20.10+ and Docker Compose 2.0+
- **For Podman**: Podman 3.0+ and podman-compose

#### Quick Start with `start.sh`
Use the provided `start.sh` script for easy deployment:
```bash
chmod +x start.sh
./start.sh start
```

#### Manual Docker Commands
```bash
docker-compose up -d
docker-compose logs -f
docker-compose down
```

#### Manual Podman Commands
```bash
podman-compose up -d
podman-compose logs -f
podman-compose down
```

#### Configuration
- **Environment Variables**:
  - `NICEGUI_HOST`: Host to bind to (default: `0.0.0.0`)
  - `NICEGUI_PORT`: Port to bind to (default: `8080`)
- **Volumes**:
  - `./data`: Application data
  - `./database`: Database files
  - `./logs`: Logs (Podman only)

---

### Containerized Setup

#### Prerequisites
- **For Docker**: Docker Engine 20.10+ and Docker Compose 2.0+
- **For Podman**: Podman 3.0+ and podman-compose

#### Quick Start with `start.sh`
Use the provided `start.sh` script for easy deployment:
```bash
chmod +x start.sh
./start.sh start
```

#### Manual Docker Commands
```bash
docker-compose up -d
docker-compose logs -f
docker-compose down
```

#### Manual Podman Commands
```bash
podman-compose up -d
podman-compose logs -f
podman-compose down
```

#### Configuration
- **Environment Variables**:
  - `NICEGUI_HOST`: Host to bind to (default: `0.0.0.0`)
  - `NICEGUI_PORT`: Port to bind to (default: `8080`)
- **Volumes**:
  - `./data`: Application data
  - `./database`: Database files
  - `./logs`: Logs (Podman only)

---

## File Structure

The application creates the following structure:
```
<path-to-folder>/Documents
├── StudentDatabase
│   ├── errorLogs
│   ├── StudentDataFiles
│   │   ├── Student1
│   │   │   ├── AbacusSkillsProgression.csv
│   │   │   ├── BrailleSkillsProgression.csv
│   │   │   └── ...
│   ├── backups
│   └── students.db
```

---

## Development

### Building Custom Images
- **Docker**:
  ```bash
  docker build -t student-data-gui .
  ```
- **Podman**:
  ```bash
  podman build -f Dockerfile.podman -t student-data-gui .
  ```

### Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Submit a pull request.

### Code Style
Follow the [Black](https://black.readthedocs.io/en/stable/) code formatter.

### Testing Locally
For testing purposes, you can run the container locally:
```bash
docker run -d -p 8080:8080 student-data-gui
```

---

## Troubleshooting

### Common Issues
1. **Permission Denied**:
   ```bash
   sudo chown -R $USER:$USER ./data ./database
   ```
2. **Port Already in Use**:
   ```bash
   export NICEGUI_PORT=8081
   ./start.sh start
   ```
3. **Build Failures**:
   ```bash
   ./start.sh clean
   ./start.sh start -b
   ```

### Logs
```bash
./start.sh logs
```

---
## Support

For container-specific issues:
1. Check logs: `./start.sh logs`
2. Verify status: `./start.sh status`
3. Clean rebuild: `./start.sh clean && ./start.sh start -b`

For application-specific issues, [open an issue on GitHub](https://github.com/mrhunsaker/StudentDataGUI/issues).

---

## Accessibility

### Accessibility Features

- Semantic HTML structure with ARIA landmarks (`header`, `nav`, `main`, `footer`) for improved screen reader navigation.
- "Skip to main content" link for keyboard and assistive technology users.
- All interactive elements (links, buttons, form fields) have visible, high-contrast focus indicators.
- Inline error messages for forms are programmatically associated with fields using ARIA attributes and are announced to screen readers.
- Dialogs and modals have ARIA roles and focus management.
- All images and icons have meaningful alternative text or are marked as decorative.
- Supports keyboard-only navigation and high-contrast mode.

### Known Limitations

- Some advanced focus trapping in modals may require further enhancement for perfect screen reader experience.
- Toast notifications may not always be announced by all screen readers.
- Accessibility testing is ongoing; please report any issues you encounter.

### Reporting Accessibility Issues

If you encounter any accessibility barriers or have suggestions for improvement, please:

- [Open an issue on GitHub](https://github.com/mrhunsaker/StudentDataGUI/issues) and use the "Accessibility" label.
- Or contact the maintainer directly via the email address listed in the repository.

### Further Documentation

- For a detailed accessibility analysis and recommendations, see [AccessibilityReport20250722.md](./AccessibilityReport20250722.md).
- For a step-by-step accessibility testing checklist, see [AccessibilityTesting.md](./AccessibilityTesting.md).


## Customization Instructions

### Changing the Logo
1. Locate the logo file in the project directory. The default logo is `dsd-mark-white`.
2. Replace the file with your desired logo, ensuring it has the same file name and format.
3. Restart the application to see the updated logo.

### Updating the GitHub Logo Target
1. Open the relevant HTML or configuration file where the GitHub logo link is defined.
2. Update the `href` attribute of the GitHub logo anchor tag to point to your desired target URL.
3. Save the changes and restart the application.

### Modifying the Footer Copyright
1. Open the footer component file in the project directory.
2. Locate the copyright text, which typically starts with "©".
3. Update the text to reflect the desired copyright information.
4. Save the changes and restart the application.
```
