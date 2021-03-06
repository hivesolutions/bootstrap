#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Bootstrap Scripts
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Bootstrap Scripts.
#
# Hive Bootstrap Scripts is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Bootstrap Scripts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Bootstrap Scripts. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
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
    "github_ripe" : (
        "git clone --recursive git@github.com:ripe-tech/{0}.git {0} {1}",
        "cd {0} && git submodule init && git submodule update && git submodule foreach git checkout master"
    )
}
""" The list of commands to be used for the bootstrap
operation for a repository """

UPDATE_COMMANDS = {
    "github" : (
        "cd {0} && git pull {1} && git fetch --prune && git submodule init && git submodule update && git submodule foreach git checkout master && git submodule foreach git pull",
    ),
    "bitbucket" : (
        "cd {0} && git pull {1} && git fetch --prune && git submodule init && git submodule update && git submodule foreach git checkout master && git submodule foreach git pull",
    ),
    "github_ripe" : (
        "cd {0} && git pull {1} && git fetch --prune && git submodule init && git submodule update && git submodule foreach git checkout master && git submodule foreach git pull",
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
        "aliyun_api",
        "appier",
        "appier_admin_api",
        "appier_console",
        "appier_extras",
        "appier_extras_api",
        "apnc",
        "armor_api",
        "armor_registers",
        "automium",
        "backup",
        "bagger_adapters",
        "bagger_api",
        "bagger_ios",
        "barcodes",
        "barcodies",
        "binance_admin",
        "binance_api",
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
        "cobeacon",
        "cobeacon_android",
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
        "contentful_api",
        "cronus_config",
        "crossline",
        "cryadapters",
        "crybot",
        "cttpie",
        "design",
        "design_archive",
        "digitalocean_api",
        "digitalriver",
        "dns_registers",
        "docker",
        "docker_api",
        "docker_bot",
        "docker_private",
        "dropbox_api",
        "eadapters",
        "easypay_api",
        "eslint_config_hive",
        "facebook_api",
        "farfetch_api",
        "firstie",
        "flask_quorum",
        "flickr_api",
        "flickr_exposition",
        "frontdoor_site",
        "github_api",
        "git_bot",
        "gonas",
        "google_api",
        "headless",
        "hello_appier",
        "hello_quorum",
        "hitbtc_api",
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
        "kaboom",
        "kibana_bot",
        "layout",
        "layout_demo",
        "legacy",
        "letsencrypt",
        "libao",
        "libs",
        "live_api",
        "loggly_api",
        "logstash_api",
        "mailme",
        "mailme_api",
        "maracujalia",
        "mariachi",
        "mantium",
        "medium",
        "metrium",
        "microsoft",
        "migratore",
        "mysql_dump",
        "netius",
        "netius_extras",
        "nexmo_api",
        "oakis",
        "okex_api",
        "omni",
        "omni_api",
        "omni_chrome",
        "omni_config",
        "omni_dashboard",
        "omni_dashboard_android",
        "omni_dashboard_vue",
        "omni_layout",
        "omni_locales",
        "omni_mobile_set",
        "omni_timeline",
        "omni_toolbox",
        "omnia",
        "omnix",
        "opbeat_api",
        "patches",
        "paypal_api",
        "pconvert",
        "pingu",
        "pingu_ios",
        "pluginus",
        "pluginus_dev",
        "prettier_config_hive",
        "prismic_api",
        "private",
        "proyectos",
        "pushi",
        "pushi_js",
        "pushi_example",
        "rancher_api",
        "rancher_bot",
        "remotia",
        "repos",
        "repos_api",
        "s3_api",
        "schettino",
        "scudum",
        "sematext_api",
        "shopdesk",
        "shopify_api",
        "signatur",
        "slack_api",
        "stacks",
        "static",
        "stylelint_config_hive",
        "story",
        "story_api",
        "stripe_api",
        "take_the_bill",
        "tiberium",
        "tiberium_soul",
        "toolis",
        "tutum_api",
        "twilio_api",
        "twitter_api",
        "unitr",
        "ustore",
        "ustore_neo",
        "utilis",
        "uxf",
        "uxf_bin",
        "uxf_demo",
        "uxf_templates",
        "uxf_webpack",
        "viriatum",
        "viriatum_android",
        "viriatum_handlers",
        "workspaces",
        "yonius",
        "zendesk_api"
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
    "github_ripe" : (
        "3d",
        "3db",
        "automator-xl",
        "builds-static",
        "careers",
        "custom-reports",
        "dev-website",
        "devops",
        "epir-core",
        "epir-core-api-js",
        "epir-papyrus",
        "epir-papyrus-api-js",
        "epir-processor",
        "epir-processor-api-js",
        "growth-static",
        "gucci-demo",
        "hacks",
        "hermes-config",
        "hermes-proxy",
        "jobs",
        "nordstrom-proxy",
        "pconvert-rust",
        "peri-email",
        "peri-templating",
        "peri-templating-api-js",
        "platforme",
        "platforme-neo",
        "platforme-revived",
        "plugin-api",
        "plugin-base",
        "plugin-demos",
        "plugin-farfetch",
        "plugin-karl",
        "plugin-kirkwood",
        "plugin-neon",
        "plugin-redirect",
        "plugin-swear",
        "project-tools",
        "pulse",
        "releases",
        "reps",
        "ripe-analytics",
        "ripe-api",
        "ripe-api-docs",
        "ripe-assets",
        "ripe-blender",
        "ripe-bridge",
        "ripe-building",
        "ripe-bus-api-js",
        "ripe-casper",
        "ripe-config",
        "ripe-commons",
        "ripe-commons-js",
        "ripe-commons-pluginus",
        "ripe-components-react-native",
        "ripe-components-react-native-storybook",
        "ripe-components-vue",
        "ripe-compose",
        "ripe-compose-light",
        "ripe-compose-light-js",
        "ripe-copper",
        "ripe-core",
        "ripe-core-vendors",
        "ripe-csr",
        "ripe-dashboard",
        "ripe-design",
        "ripe-design-large",
        "ripe-docs",
        "ripe-fonts",
        "ripe-id",
        "ripe-id-api",
        "ripe-id-api-js",
        "ripe-id-mobile",
        "ripe-id-radius",
        "ripe-legacy",
        "ripe-maya",
        "ripe-misc",
        "ripe-ops",
        "ripe-orchestra",
        "ripe-orchestra-api-js",
        "ripe-orchestra-ui",
        "ripe-pulse",
        "ripe-push",
        "ripe-rainbow",
        "ripe-registry",
        "ripe-registry-api-js",
        "ripe-registry-ui",
        "ripe-retail",
        "ripe-retail-vendors",
        "ripe-robin",
        "ripe-robin-landing",
        "ripe-robin-revamp",
        "ripe-runner",
        "ripe-sales",
        "ripe-salesforce",
        "ripe-sap",
        "ripe-scripts",
        "ripe-sdk",
        "ripe-sdk-android",
        "ripe-sdk-components-react",
        "ripe-sdk-components-vue",
        "ripe-sdk-ios",
        "ripe-skeleton-vue",
        "ripe-sputnik-device",
        "ripe-sputnik-manager",
        "ripe-sputnik-manager-api-js",
        "ripe-sputnik-ui",
        "ripe-ssr",
        "ripe-static",
        "ripe-tests",
        "ripe-today",
        "ripe-twitch",
        "ripe-twitch-api-js",
        "ripe-twitch-ui",
        "ripe-uploader",
        "ripe-util",
        "ripe-util-vue",
        "ripe-warehouse",
        "ripe-welcome",
        "ripe-white",
        "ripe-white-admin",
        "ripe-white-admin-api-js",
        "ripe-white-admin-ui",
        "ripe-white-demo",
        "ripe-white-pos-demo",
        "ripe-xl",
        "sadapters",
        "simple-proxy",
        "swear",
        "tech",
        "tech-website",
        "tobias-bot",
        "twitch-panel",
        "twitch-panel-manager"
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

    :type minimal: bool
    :param minimal: If the update operation should use
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
else:
    __path__ = []
