# StudentDataGUI

StudentDataGUI is a user-friendly application for managing student data, designed to be easy to set up and use—even for those with little technical experience. It runs inside containers for maximum reliability and simplicity. This guide provides detailed, step-by-step instructions for building, running, and troubleshooting the application, with a focus on using **Podman** (recommended), and **Docker** as an alternative.

---

## Table of Contents

1. [Overview](#overview)
2. [Quick Start (Podman Recommended)](#quick-start-podman-recommended)
3. [Detailed Setup Instructions](#detailed-setup-instructions)
   - [Podman Setup](#podman-setup)
   - [Docker Setup (Alternative)](#docker-setup-alternative)
4. [Troubleshooting](#troubleshooting)
5. [Support](#support)
6. [Accessibility](#accessibility)
7. [Customization](#customization-instructions)
8. [Contributing](#contributing)
9. [File Structure](#file-structure)

---

## Overview

StudentDataGUI provides a graphical interface for entering and managing student data. It uses NiceGUI for the interface and SQLite3 for the database. The application is designed to run inside containers, so you don’t need to worry about installing or configuring complicated software.

---

## Quick Start (Podman Recommended)

If you are new to containers, **Podman** is a modern, rootless alternative to Docker. It is safe, secure, and easy to use.

### 1. Install Podman and podman-compose

- **Fedora/Red Hat:**
  ```bash
  sudo dnf install podman podman-compose
  ```
- **Ubuntu/Debian:**
  ```bash
  sudo apt-get install podman podman-compose
  ```
- For other systems, see the [Podman installation guide](https://podman.io/getting-started/installation).

### 2. Download the Application

- Download or clone the StudentDataGUI repository to your computer.

### 3. Start the Application

- Open a terminal in the project folder.
- Make the start script executable (only needed once):
  ```bash
  chmod +x start.sh
  ```
- Start the application:
  ```bash
  ./start.sh start
  ```
- The application will build and run in a container.
  When ready, open your web browser and go to:
  [http://localhost:8080](http://localhost:8080)

---

## Detailed Setup Instructions

### Podman Setup

- **Start the Application**
  Use the provided script for the easiest experience:
  ```bash
  ./start.sh start
  ```

- **Manual Podman Commands**
  If you prefer, you can use these commands:
  To start the application, Type the following command and then optn http://localhost:8080 in the browser of your choice:

  ```bash
  podman-compose up -d && podman-compose logs -f
  ```

  To end the application: Close the browser tab or window and then stop the container:
  ```bash
  podman-compose down
  ```

- **Configuration**
  - The application uses port 8080 by default.
    If this port is busy, you can change it:
    ```bash
    export NICEGUI_PORT=8081
    ./start.sh start
    ```
  - Data is stored in the `./data`, `./database`, and `./logs` folders.

### Docker Setup (Alternative)

If you prefer Docker, follow these steps:

- **Install Docker and Docker Compose**
  - [Docker installation guide](https://docs.docker.com/get-docker/)
- **Start the Application**
  ```bash
  ./start.sh start
  ```
- **Manual Docker Commands**
  ```bash
  docker-compose up -d
  docker-compose logs -f
  docker-compose down
  ```
- **Configuration**
  - Uses the same environment variables and folders as Podman.

---

## Troubleshooting

If you run into problems, try these solutions:

1. **Permission Denied Errors**
   - Make sure you own the data folders:
     ```bash
     sudo chown -R $USER:$USER ./data ./database ./logs
     ```

2. **Port Already in Use**
   - Change the port:
     ```bash
     export NICEGUI_PORT=8081
     ./start.sh start
     ```

3. **Build Failures or Application Won't Start**
   - Clean and rebuild:
     ```bash
     ./start.sh clean
     ./start.sh start -b
     ```

4. **Viewing Logs**
   - To see what's happening inside the application:
     ```bash
     ./start.sh logs
     ```

5. **Checking Status**
   - To check if the application is running:
     ```bash
     ./start.sh status
     ```

---

## Support

- For container issues, use the troubleshooting steps above.
- For application issues, [open an issue on GitHub](https://github.com/mrhunsaker/StudentDataGUI/issues).
- For accessibility or usability questions, see the Accessibility section below.

---

## Accessibility

StudentDataGUI is designed to be accessible for all users, including those using screen readers or keyboard navigation.

- Uses ARIA landmarks and semantic HTML for easy navigation.
- "Skip to main content" link for keyboard users.
- All buttons and forms have visible, high-contrast focus indicators.
- Error messages are announced to screen readers.
- Dialogs and modals are accessible and manage focus correctly.
- All images and icons have meaningful alternative text or are marked decorative.
- Supports keyboard-only navigation and high-contrast mode.

**Known Limitations:**
- Some advanced focus trapping in modals may need further improvement.
- Toast notifications may not always be announced by all screen readers.

**Reporting Accessibility Issues:**
- [Open an issue on GitHub](https://github.com/mrhunsaker/StudentDataGUI/issues) with the "Accessibility" label.
- Or contact the maintainer directly via the email address in the repository.

**Further Documentation:**
- See [AccessibilityReport20250722.md](./AccessibilityReport20250722.md) for a detailed analysis.
- See [AccessibilityTesting.md](./AccessibilityTesting.md) for a step-by-step testing checklist.

---

## Customization Instructions

- **Changing the Logo:**
  Replace the logo file (`dsd-mark-white`) in the project directory with your own, using the same name and format. Restart the application.

- **Updating the GitHub Logo Target:**
  Edit the relevant HTML or configuration file, change the `href` for the GitHub logo, save, and restart.

- **Modifying Footer Copyright:**
  Edit the footer component file, update the copyright text, save, and restart.

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Submit a pull request.

- Follow the [Black](https://black.readthedocs.io/en/stable/) code formatter for Python code.

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

## Additional Notes

- **Data Safety:** All student data is stored locally on your computer, inside the container’s mapped folders. Regularly back up the `StudentDatabase` folder to prevent data loss.
- **Updates:** To update the application, pull the latest version from GitHub and restart the container.
- **Security:** Only run the application on trusted computers and networks, especially when handling sensitive student information.

---

If you have any questions or need further help, please reach out via GitHub or the contact information in this repository.
