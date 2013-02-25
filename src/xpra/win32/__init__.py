# This file is part of Parti.
# Copyright (C) 2010 Nathaniel Smith <njs@pobox.com>
# Copyright (C) 2011-2013 Antoine Martin <antoine@devloop.org.uk>
# Parti is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

# Platform-specific code for Win32.

import os
import sys

XPRA_LOCAL_SERVERS_SUPPORTED = False
os.environ["PLINK_PROTOCOL"] = "ssh"
DEFAULT_SSH_CMD = "plink"
GOT_PASSWORD_PROMPT_SUGGESTION = \
   'Perhaps you need to set up Pageant, or (less secure) use --ssh="plink -pw YOUR-PASSWORD"?\n'

def add_client_options(parser):
    from xpra.platform import add_notray_option
    add_notray_option(parser, ", this will also disable notifications!")

def get_machine_id():
    return  u""

def do_init():
    if not getattr(sys, 'frozen', ''):
        return
    #on win32 we must send stdout to a logfile to prevent an alert box on exit shown by py2exe
    #UAC in vista onwards will not allow us to write where the software is installed, so place the log file in "~/Application Data"
    appdata = os.environ.get("APPDATA")
    if not os.path.exists(appdata):
        os.mkdir(appdata)
    log_path = os.path.join(appdata, "Xpra")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = os.path.join(log_path, "Xpra.log")
    sys.stdout = open(log_file, "a")
    sys.stderr = sys.stdout

def get_app_dir():
    if getattr(sys, 'frozen', ''):
        return os.path.dirname(sys.executable)
    from xpra.platform import default_get_app_dir   #imported here to prevent import loop
    return default_get_app_dir()
