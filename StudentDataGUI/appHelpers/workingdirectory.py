#!/usr/bin/env python3

"""
 Copyright 2023  Michael Ryan Hunsaker, M.Ed., Ph.D.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""

import os
from pathlib import Path

def create_user_dir() -> None:
    """
    Create or retrieve the user directory path.

    This function determines the appropriate user directory path based on the operating system
    (Windows or POSIX) and creates the directory structure if it doesn't exist. The user directory
    path is typically used for storing application-related data.

    Returns
    -------
    Path
        The path to the user directory.

    Raises
    ------
    NameError
        If the environment variable representing the user directory is not found.

    Examples
    --------
    >>> user_directory = create_user_dir()
    >>> # Use user_directory for storing application-related data
    >>> # ...

    Notes
    -----
    The user directory path may vary depending on the operating system:
    - On Windows, it is typically under "%USERPROFILE%\Documents".
    - On POSIX systems, it is typically under "$HOME/Documents".
    """
    if os.name == "nt":
        try:
            tmp_path = Path(os.environ["USERPROFILE"]).joinpath(
                 "Documents"
            )
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            USER_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find %USERPROFILE")
    elif os.name == "posix":
        try:
            tmp_path = Path(os.environ["HOME"]).joinpath(
                "Documents"
            )
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            USER_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find $HOME")
    return USER_DIR
