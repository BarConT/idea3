from flask import Blueprint
carrito_bp = Blueprint('carrito', __name__, template_folder='templates')
from . import routes