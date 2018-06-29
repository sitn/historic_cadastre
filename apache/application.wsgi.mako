import sys
import os

root = "${directory}"

sys.path = ["${python_path.replace("\\", "\\\\")}"] + sys.path

from pyramid.paster import get_app, setup_logging

configfile = os.path.join(root, "${'development' if development == 'TRUE' else 'production'}.ini")
setup_logging(configfile)
application = get_app(configfile, 'main')
