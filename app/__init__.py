import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ohio_oil.db')   
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init marshmallow
ma = Marshmallow(app)

from app.wells import wells_bp
app.register_blueprint(wells_bp, url_prefix='/wells')

# from app.wells import views