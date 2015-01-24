# import modules to get access to many useful functions :)

# Flask - a lightweight web/backend framework for Python lang
from flask import Flask

# create Flask instance
app = Flask(__name__)

# get configuration settings
app.config.from_object('config')

from app import routes
