from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# MOCK comidas
from mock_comidas import comidas
from forms import ComidaForm, LoginForm
from models import users, get_user

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

@app.route('/')
def index():
    return render_template('index.html', comidas=comidas)

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
    if form.validate_on_submit():
        categoria = form.categoria.data
        nombre = form.nombre.data
        precio = form.precio.data
        comida = {'categoria': categoria, 'nombre': nombre, 'precio': precio }
        comidas.append(comida)
        return redirect(url_for('index'))
    return render_template('admin/comida_form.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.name.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))