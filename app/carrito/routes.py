from flask import render_template, request, json, make_response, url_for, redirect
from . import carrito_bp

from ..models import Comida

# Vista Carrito
@carrito_bp.route('/pedido/')
def vista_pedido():
    try:
        carrito = json.loads(request.cookies.get('carrito'))
    except:
        carrito = []
    comidas=[]
    cantidades=[]
    total=0
    for comida in carrito:
        comidas.append(Comida.query.get(comida["id"]))
        cantidades.append(comida["cantidad"])
        total=total+Comida.query.get(comida["id"]).precio*comida["cantidad"]
    comidas=zip(comidas,cantidades)
    return render_template('carrito/vista_pedido.html', comidas=comidas, total=total)

# Agregar comida al carrito
@carrito_bp.route('/carrito/add/<id>',methods=["get","post"])
def carrito_sumar(id):
    response = make_response(redirect(url_for('carrito.vista_pedido')))	
    art=Comida.query.get(id)
    try:
        carrito = json.loads(request.cookies.get('carrito'))
    except:
        carrito = []
    if not carrito:
        carrito = [{"cantidad": 1, "id": art.id}]
    else:
        actualizar = True
        for comida in carrito:
            if comida['id'] == art.id:    
                comida['cantidad'] += 1
                actualizar= False
        if actualizar: 
            carrito.append({"cantidad": 1, "id": art.id})
    response.set_cookie('carrito', json.dumps(carrito))	
    return response

# Restar comida al carrito
@carrito_bp.route('/carrito/delete/<id>',methods=["get","post"])
def carrito_restar(id):
    response = make_response(redirect(url_for('carrito.vista_pedido')))	
    art=Comida.query.get(id)
    try:
        carrito = json.loads(request.cookies.get('carrito'))
    except:
        carrito = []
    for comida in carrito:
        if comida['id'] == art.id:    
            comida['cantidad'] -= 1
            if comida['cantidad'] < 1:
                return redirect(url_for('carrito.carrito_delete', id=id))
    response.set_cookie('carrito', json.dumps(carrito))	
    return response

# Eliminar comida del carrito
@carrito_bp.route('/carrito_delete/<id>')
def carrito_delete(id):
    try:
        carrito = json.loads(request.cookies.get('carrito'))
    except:
        carrito = []
    nuevo_carrito=[]
    for comida in carrito:
        if str(comida["id"])!=id:
            nuevo_carrito.append(comida)
    response = make_response(redirect(url_for('carrito.vista_pedido')))
    response.set_cookie(('carrito'),json.dumps(nuevo_carrito))
    return response

# Vaciar carrito

# @carrito_bp.context_processor
# def contar_carrito():
# 	if not current_user.is_anonymous:
# 		return {'num_articulos':0}
# 	if request.cookies.get('carrito')==None:
# 		return {'num_articulos':0}
# 	else:
# 		datos = json.loads(request.cookies.get(str(current_user.id)))
# 		return {'num_articulos':len(datos)}