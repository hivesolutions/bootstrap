#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Bootstrap Scripts
# Copyright (C) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Bootstrap Scripts.
#
# Hive Bootstrap Scripts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Bootstrap Scripts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Bootstrap Scripts. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os
import subprocess

BOOTSTRAP_COMMANDS = [
    "git clone git@github.com:hivesolutions/{0}.git {0}",
    "cd {0} && git submodule init && git submodule update && git submodule foreach git checkout master"
]
""" The list of commands to be used for the boostrap
operation for a repository """

UPDATE_COMMANDS = [
    "cd {0} && git pull && git submodule foreach git pull"
]
""" The list of commands to be used for the update
operation for a repository """

REPOSITORIES = [
    #"colony",
    #"colony_config",
    #"colony_plugins",
    #"hive_blog",
    #"hive_site",
    #"omni",
    #"uxf",
    #"uxf_bin",
    #"viriatum"
    "viriatum"
]
""" The list of repositories that will be used
for the operation of bootstrap and update  """

def bootstrap():
    # iterates over each of the repositories
    # and executes the commands for the bootstrap
    # operation on each of them
    for repository in REPOSITORIES: _bootstrap(repository)

def _bootstrap(repository):
    # iterates over each of the bootstrap commands
    # and creates the "final" command value using
    # the repository value and then executes it
    for update_command in BOOTSTRAP_COMMANDS:
        command = update_command.format(repository)
        subprocess.call(command, shell = True)

def update():
    """
    "Runs" the virtual update operation under
    the current directory for all of the repositories
    registered in the current script.
    """

    # iterates over each of the repositories
    # and executes the commands for the update
    # operation on each of them
    for repository in REPOSITORIES: _update(repository)

def _update(repository):
    # iterates over each of the update commands
    # and creates the "final" command value using
    # the repository value and then executes it
    for update_command in UPDATE_COMMANDS:
        if not os.path.exists(repository): _bootstrap(repository)
        command = update_command % repository
        subprocess.call(command, shell = True)

update()
