import os, sys

PROJECT_DIR = '~/Documents/_meridian/appz lab/Genesis-Flask'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from genesisflask import app as application