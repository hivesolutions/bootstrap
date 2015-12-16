#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Bootstrap Scripts
# Copyright (c) 2008-2015 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os
import sys
import stat
import subprocess

import urllib #@UnusedImport

try: import urllib2
except ImportError: urllib2 = None

try: import urllib.request
except ImportError: urllib.request = None

PYTHON_3 = sys.version_info[0] >= 3
""" Global variable that defines if the current python
interpreter is at least python 3 compliant, this is used
to take some of the conversion decision for runtime """

VERBOSE = True
""" The default verbosity level to be used during the
execution of the bootstrap commands """

BASE_ADDRESS = "https://github.com/hivesolutions/bootstrap/raw/master/%s"
""" The base address to the remote location
of the repository to retrieve the file """

BOOTSTRAP_COMMANDS = {
    "github" : (
        "git clone --recursive git@github.com:hivesolutions/{0}.git {0} {1}",
        "cd {0} && git submodule init && git submodule update && git submodule foreach git checkout master"
    ),
    "bitbucket" : (
        "git clone --recursive git@bitbucket.org:hivesolutions/{0}.git {0} {1}",
        "cd {0} && git submodule init && git submodule update && git submodule foreach git checkout master"
    ),
    "github_myswear" : (
        "git clone --recursive git@github.com:myswear/{0}.git {0} {1}",
        "cd {0} && git submodule init && git submodule update && git submodule foreach git checkout master"
    )
}
""" The list of commands to be used for the bootstrap
operation for a repository """

UPDATE_COMMANDS = {
    "github" : (
        "cd {0} && git pull {1} && git submodule init && git submodule update && git submodule foreach git checkout master && git submodule foreach git pull",
    ),
    "bitbucket" : (
        "cd {0} && git pull {1} && git submodule init && git submodule update && git submodule foreach git checkout master && git submodule foreach git pull",
    ),
    "github_myswear" : (
        "cd {0} && git pull {1} && git submodule init && git submodule update && git submodule foreach git checkout master && git submodule foreach git pull",
    )
}
""" The list of commands to be used for the update
operation for a repository """

FILES = {
    "nt" : (
        "lib/bootstrap.py",
        "win32/bootstrap.bat",
        "win32/update.bat"
    ),
    "unix" : (
        ("lib/bootstrap.py", stat.S_IEXEC) ,
        ("unix/bootstrap.sh", stat.S_IEXEC),
        ("unix/update.sh", stat.S_IEXEC)
    )
}
""" The map that defines the various sequences of files
to be used for retrieval under each of the os names """

REPOSITORIES = {
    "github" : (
        "admin",
        "admin_scripts",
        "appier",
        "appier_extras",
        "apnc",
        "armor_api",
        "armor_registers",
        "automium",
        "backup",
        "bagger_adapters",
        "bagger_api",
        "bagger_ios",
        "barcodes",
        "bootstrap",
        "budy",
        "budy_api",
        "builds",
        "cameo",
        "cameo_android",
        "cameria",
        "cameria_android",
        "cameria_ios",
        "camito",
        "campaigner",
        "capsule",
        "cloud_print",
        "colony",
        "colony_config",
        "colony_examples",
        "colony_npapi",
        "colony_plugins",
        "colony_print",
        "colony_site",
        "commons_py",
        "concordia",
        "config",
        "cronus_config",
        "crossline",
        "design",
        "design_archive",
        "digitalocean_api",
        "digitalriver",
        "dns_registers",
        "docker",
        "docker_private",
        "easypay_api",
        "facebook_api",
        "farfetch_api",
        "flask_quorum",
        "flickr_api",
        "flickr_exposition",
        "frontdoor_site",
        "github_api",
        "gonas",
        "google_api",
        "hello_quorum",
        "hive_blog",
        "hive_nature",
        "hive_openid",
        "hive_site",
        "ifriday",
        "instagram_api",
        "instashow",
        "internus",
        "ios_skeleton",
        "jquery",
        "jquery_util",
        "jquery_util_ui",
        "js_util",
        "layout",
        "layout_demo",
        "legacy",
        "libao",
        "libs",
        "live_api",
        "mariachi",
        "mantium",
        "medium",
        "metrium",
        "microsoft",
        "migratore",
        "mongo_api_cs",
        "mysql_dump",
        "netius",
        "nexmo_api",
        "omni",
        "omni_api",
        "omni_chrome",
        "omni_config",
        "omni_dashboard",
        "omni_dashboard_android",
        "omni_layout",
        "omni_locales",
        "omni_mobile_set",
        "omni_timeline",
        "omni_toolbox",
        "omnia",
        "omnix",
        "patches",
        "pingu",
        "pingu_ios",
        "private",
        "proyectos",
        "pushi",
        "pushi_js",
        "pushi_example",
        "remotia",
        "repos",
        "schettino",
        "scudum",
        "shopdesk",
        "shopify_api",
        "take_the_bill",
        "tiberium",
        "tiberium_soul",
        "twilio_api",
        "twitter_api",
        "unitr",
        "ustore",
        "utilis",
        "uxf",
        "uxf_bin",
        "uxf_demo",
        "viriatum",
        "viriatum_android",
        "viriatum_handlers"
    ),
    "bitbucket" : (
        "hive_neo",
        "myswear_ios",
        "oibiquini",
        "oibiquini_extras",
        "pas",
        "webook",
        "websites"
    ),
    "github_myswear" : (
        "building",
        "myswear",
        "sadapters",
        "swear"
    )
}
""" The map of services associated with a list of repositories
that will be used for the operation of bootstrap and update """

REPOSITORIES_MINIMAL = {
    "github" : (
        "colony",
        "colony_config",
        "colony_plugins"
    )
}
""" The map of services associated with a list of repositories
that will be used for the operation of bootstrap and update, these
commands will only be used in the minimal mode """

if PYTHON_3: STRINGS = (str,)
else: STRINGS = (str, unicode) #@UndefinedVariable

def urlopen(*args, **kwargs):
    if PYTHON_3: return urllib.request.urlopen(*args, **kwargs)
    else: return urllib2.urlopen(*args, **kwargs) #@UndefinedVariable

def bootstrap(minimal = False):
    # retrieves the proper repositories list according
    # to the value of the minimal flag
    repositories = minimal and REPOSITORIES_MINIMAL or REPOSITORIES

    # iterates over each of the repositories
    # and executes the commands for the bootstrap
    # operation on each of them
    for service, names in repositories.items():
        for repository in names:
            is_sequence = type(repository) in (list, tuple)
            if is_sequence: repository, extra = repository
            else: extra = ""
            exists = os.path.exists(repository)
            if not exists: _bootstrap(service, repository, extra = extra)

def _bootstrap(service, repository, extra = ""):
    # iterates over each of the bootstrap commands
    # and creates the "final" command value using
    # the repository value and then executes it
    bootstrap_commands = BOOTSTRAP_COMMANDS.get(service, ())
    for bootstrap_command in bootstrap_commands:
        command = bootstrap_command.format(repository, extra)
        execute(command)

def update(minimal = False):
    """
    "Runs" the virtual update operation under
    the current directory for all of the repositories
    registered in the current script.

    @type minimal: bool
    @param minimal: If the update operation should use
    the minimal repositories list for operation.
    """

    # retrieves the proper repositories list according
    # to the value of the minimal flag
    repositories = minimal and REPOSITORIES_MINIMAL or REPOSITORIES

    # iterates over each of the repositories
    # and executes the commands for the update
    # operation on each of them
    for service, names in repositories.items():
        for repository in names:
            is_sequence = type(repository) in (list, tuple)
            if is_sequence: repository, extra = repository
            else: extra = ""
            _update(service, repository, extra = extra)

def _update(service, repository, extra = ""):
    # iterates over each of the update commands
    # and creates the "final" command value using
    # the repository value and then executes it
    update_commands = UPDATE_COMMANDS.get(service, ())
    for update_command in update_commands:
        if not os.path.exists(repository): _bootstrap(service, repository)
        command = update_command.format(repository, extra)
        execute(command)

def execute(command, verbose = VERBOSE):
    # in case the verbose flag is set prints the command
    # string then creates a new subprocess with the shell
    if verbose: print(command)
    subprocess.call(command, shell = True)

def download():
    # retrieves the normalized version of the
    # operative system name (normalized to unix)
    # then uses it to retrieve the list of files
    os_name = os.name == "nt" and "nt" or "unix"
    files = FILES.get(os_name, [])

    # iterates over each of the files to retrieve
    # it from the remote location
    for _file in files:
        # checks the file type and in case it's a string
        # default the file structure into a tuple with the
        # file (name) and an unset (invalid) mode
        file_type = type(_file)
        if file_type in STRINGS: _file = (_file, None)

        # unpacks the file structure into the name of the file
        # and the file (execution) mode
        name, mode = _file

        # opens the remove location retrieving the data
        # and then uses it to populate the associated file
        remote = urlopen(BASE_ADDRESS % name)
        contents = remote.read()
        base = os.path.basename(name)
        file = open(base, "wb")
        try: file.write(contents)
        finally: file.close

        # in case the mode value is not set nothing more
        # to be done, must continue the loop
        if not mode: continue

        # retrieves the current state from the file and
        # uses it to retrieve its current mode and or it
        # with the requested mode value and set it
        _stat = os.stat(base)
        _mode = _stat.st_mode
        os.chmod(base, _mode | mode)

if __name__ == "__main__":
    if len(sys.argv) < 2: exit(0)
    command = sys.argv[1]
    if command == "--bootstrap": bootstrap()
    if command == "--update": update()
    if command == "--download": download()
    if command == "--update-minimal": update(minimal = True)
    if command == "--download-minimal": download(minimal = True)
