from flask import Flask, redirect, render_template, url_for, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from forms import ComidaForm, LoginForm

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Configuración base de datos SQLite
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import User, Comida, Categoria

@app.route('/')
def index():
    comidas = Comida.get_all()
    categorias = Categoria.get_all()
    return render_template('index.html', comidas=comidas, categorias=categorias)

@app.route('/pedido/')
def vista_pedido():
    return render_template('vista_pedido.html')

@app.route('/confirmacion/')
def confirmacion_pedido():
    return render_template('confirmacion_pedido.html')

@app.route('/admin/comida/', methods=['GET', 'POST'])
@login_required
def comida_form():
    form = ComidaForm()
    form.categoria.choices = [(categoria.id, categoria.nombre_categoria)for categoria in Categoria.query.filter_by().all()]
    if form.validate_on_submit():
        categoria_id = Categoria.query.filter_by(id=form.categoria.data).first().nombre_categoria
        nombre = form.nombre.data
        precio = form.precio.data
        comida = Comida(categoria_id=categoria_id, nombre=nombre, precio=precio)
        comida.save()
        return redirect(url_for('index'))
    return render_template('admin/comida_form.html', form=form)

# Login
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_name(form.name.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

# Cerrar sesión
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Editar Comida
@app.route("/admin/editar/<int:id_comida>/")
def editar_comida(id_comida):
    post = Comida.get_by_id(id_comida)
    if post is None:
        abort(404)
    return "Editar comida ${}".format(id_comida)