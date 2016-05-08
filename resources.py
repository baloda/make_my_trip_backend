from flask import Flask
from flask.ext.restful import Api
from flask.ext.cors import CORS
from flask import request
import os


application = Flask(__name__)
CORS(application)
api=Api(application)
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload_directory')
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
