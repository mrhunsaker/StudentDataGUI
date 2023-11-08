#!/usr/bin/env python3
# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers
of students with Visual Impairments
"""
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.
#    #
#    email: hunsakerconsulting@gmail.com
#    #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");
#    #
#    you may not use this file except in compliance with the License.
#    #
#    You may obtain a copy of the License at
#    #
#                                                                             #
#    http://www.apache.org/licenses/LICENSE-2.0
#    #
#                                                                             #
#    Unless Required by applicable law or agreed to in writing,
#    software      #
#    distributed under the License is distributed on an "AS IS"
#    BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#    implied. #
#    See the License for the specific language governing permissions
#    and      #
#    limitations under the License.
#    #
###############################################################################

import os
from pathlib import Path


def create_user_dir() -> None:
    if os.name == "nt":
        try:
            tmp_path = Path(os.environ["USERPROFILE"]).joinpath(
                "OneDrive - Davis School District", "Documents"
            )
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            USER_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find %USERPROFILE")
    elif os.name == "posix":
        try:
            tmp_path = Path(os.environ["HOME"]).joinpath(
                "OneDrive - Davis School District", "Documents"
            )
            Path.mkdir(tmp_path, parents=True, exist_ok=True)
            USER_DIR = Path(tmp_path)
        except NameError as e:
            print(f"{e}\n Cannot find $HOME")
    return USER_DIR
