from flask import render_template, redirect, url_for, abort
from flask_login import login_required
from app.models import Comida, Categoria
from . import admin_bp
from .forms import ComidaForm

@admin_bp.route('/admin/comida/', methods=['GET', 'POST'])
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
        return redirect(url_for('public.index'))
    return render_template('admin/comida_form.html', form=form)


# Editar Comida
@admin_bp.route("/admin/editar/<int:id_comida>/")
def editar_comida(id_comida):
    post = Comida.get_by_id(id_comida)
    if post is None:
        abort(404)
    return "Editar comida ${}".format(id_comida)