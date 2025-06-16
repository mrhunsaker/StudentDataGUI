#!/usr/bin/env python3

"""
Student Data GUI - A data collection and instructional tool for teachers of students with Visual Impairments.

Copyright 2023-2025 Michael Ryan Hunsaker, M.Ed., Ph.D.
Licensed under the Apache License, Version 2.0

This module provides a web-based interface for tracking student progress across various skills
including braille literacy, technology skills, and mobility assessments.
"""

__version__ = "2024.07.08"
__author__ = "Michael Ryan Hunsaker, M.Ed., Ph.D."
__email__ = "hunsakerconsulting@gmail.com"
__license__ = "Apache-2.0"

# Module metadata
__all__ = [
    "main",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]

def run():
    """Entry point for running the Student Data GUI application."""
    from .main import main
    main()

if __name__ == "__main__":
    run()
