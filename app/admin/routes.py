import os
from os import remove
from flask import render_template, redirect, url_for, current_app
from flask_login import login_required
from werkzeug.exceptions import NotFound
from werkzeug.utils import secure_filename

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
        file = form.comida_image.data
        image_name = None
        if file:
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['COMIDAS_IMAGES_DIR']
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)
        comida = Comida(categoria_id=categoria_id, nombre=nombre, precio=precio)
        comida.imagen = image_name
        comida.save()
        return redirect(url_for('public.index'))
    return render_template('admin/comida_form.html', form=form)


# Editar Comida
@admin_bp.route("/admin/editar/<int:id_comida>/", methods=['GET', 'POST'])
def editar_comida(id_comida):
    comida = Comida.get_by_id(id_comida)
    if comida is None:
        raise NotFound(id_comida)
    form = ComidaForm(obj=comida)
    form.categoria.choices = [(categoria.id, categoria.nombre_categoria)for categoria in Categoria.query.filter_by().all()]
    if form.validate_on_submit():
        comida.categoria_id = Categoria.query.filter_by(id=form.categoria.data).first().nombre_categoria
        comida.nombre = form.nombre.data
        comida.precio = form.precio.data
        file = form.comida_image.data
        image_name = comida.imagen
        if file:
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['COMIDAS_IMAGES_DIR']
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)
        comida.imagen = image_name
        comida.save()
        return redirect(url_for('public.index'))
    return render_template('admin/comida_edit.html', form=form, comida=comida)

# Eliminar Comida
@admin_bp.route("/admin/eliminar/<int:id_comida>/", methods=['POST', 'GET'])
def eliminar_comida(id_comida):
    comida = Comida.get_by_id(id_comida)
    if comida is None:
        raise NotFound(id_comida)
    images_dir = current_app.config['COMIDAS_IMAGES_DIR']
    remove(os.path.join(images_dir, comida.imagen))
    comida.delete()
    return redirect(url_for('public.index'))
