import os
from flask import Flask
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
from flask.ext.cors import CORS
# import flask.ext.login as flask_login


MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    MONGO_URL = "mongodb://localhost:27017/rest";

#app
app = Flask(__name__)
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)
CORS(app)

app.config['MONGO_URI'] = MONGO_URL

# mongo
mongo = PyMongo(app)

# code is status code, obj is wait for serialization, headers is optional
def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

# to setup the output format
DEFAULT_REPRESENTATIONS = {'application/json': output_json}



#api
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import restful_service.forms
import restful_service.users
import restful_service.experiments
import restful_service.results
