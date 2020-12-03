from flask import Flask, request
import os
import json
from flask_cors import CORS
from instance.config import Config

import sqlite3

import datetime

# from utils import check_password, generate_login_token, hash_password, decode_login_token
import db
import utils

#
# Instantiate the Main Flask Application
#
app = Flask(__name__)
#
# Enable C.O.R.S.
#
CORS(app)
#
# Application Configuration
#
app.config['DEBUG'] = Config.DEBUG
app.config['SECRET_KEY'] = Config.SECRET_KEY


@app.route('/')
def index():
    # message = redis_client.get('ping')
    url_map = app.url_map
    return_data = {
        "status": "OK",
        "message": "All systems online",
        "endpoints": dict(url_map.__dict__['_rules_by_endpoint'])
    }
    return f"<pre>{json.dumps(return_data,default=str)}</pre>"

# import all other routes
import application.routes