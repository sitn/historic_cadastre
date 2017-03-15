"""
    See https://code.google.com/p/modwsgi/wiki/VirtualEnvironments#Application_Environments
    for a complete description of the problem.

    With Windows, mod_wsgi always uses the default Python instance,
    thus we have to specify the order of "site-packages" loading.

    It is like in common Windows path environmental variables, first
    arrived, first used
"""

ALLDIRS = ["${python_path.replace("\\", "\\\\")}"]

import sys
import site

# Remember original sys.path.
prev_sys_path = list(sys.path)

# Add each new site-packages directory.
for directory in ALLDIRS:
  site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

from pyramid.paster import get_app, setup_logging

configfile = "${directory.replace("\\", "\\\\")}\\${'development' if development == 'TRUE' else 'production'}.ini"
setup_logging(configfile)
application = get_app(configfile, 'main')