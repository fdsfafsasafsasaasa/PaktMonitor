from paktmonitor.client.routes import *
from paktmonitor.oauth.routes import *
from paktmonitor.api.routes import *
from paktmonitor.client import client
from paktmonitor.oauth import oauth
from paktmonitor.api import api

from paktmonitor import paktmonitor

paktmonitor.register_blueprint(client)
paktmonitor.register_blueprint(oauth)
paktmonitor.register_blueprint(api)
