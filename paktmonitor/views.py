from paktmonitor.client.routes import *
from paktmonitor.client import client

from paktmonitor import paktmonitor

paktmonitor.register_blueprint(client)

from paktmonitor.api.routes import *
from paktmonitor.api import api

paktmonitor.register_blueprint(api)
