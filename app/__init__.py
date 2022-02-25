from flask import  Flask
from app import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app=Flask(__name__)
cors=CORS(app)
app.secret_key = os.urandom(24)
app.config['CORS_HEADERS']='Content-Type'


path = os.path.dirname(os.path.abspath(__file__)) + "/static/img/usuarios/" 
app.config['UPLOAD_FOLDER'] = path
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.config.from_object(config.Config)
db=SQLAlchemy(app)

from app import routers,models