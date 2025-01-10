from flask import Blueprint

wells_bp = Blueprint('wells', __name__)

from . import views
