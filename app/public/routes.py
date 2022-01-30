from flask import render_template
from app.models import Comida, Categoria
from . import public_bp

@public_bp.route('/')
def index():
    comidas = Comida.get_all()
    categorias = Categoria.get_all()
    return render_template('public/index.html', comidas=comidas, categorias=categorias)

@public_bp.route('/pedido/')
def vista_pedido():
    return render_template('public/vista_pedido.html')

@public_bp.route('/confirmacion/')
def confirmacion_pedido():
    return render_template('public/confirmacion_pedido.html')