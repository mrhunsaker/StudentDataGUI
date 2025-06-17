#!/usr/bin/env python3

"""
Student Data GUI - A data collection and instructional tool for teachers of students with Visual Impairments.
"""

__version__ = "2025.06.16"
__author__ = "Michael Ryan Hunsaker, M.Ed., Ph.D."
__email__ = "hunsakerconsulting@gmail.com"
__license__ = "Apache-2.0"

def run():
    """Entry point for running the Student Data GUI application."""
    from .main import main
    main()

from . import main
from . import appHelpers
from . import appPages
from . import appTheming
from . import visualScan

__all__ = [
    "main",
    "appHelpers",
    "appPages",
    "appTheming",
    "visualScan",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]

if __name__ == "__main__":
    run()
