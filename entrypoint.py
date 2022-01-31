import os
from app import create_app
from flask import send_from_directory

app = create_app()

@app.route('/imagenes/<filename>')
def media_comida(filename):
    dir_path = os.path.join(app.config['COMIDAS_IMAGES_DIR'])
    return send_from_directory(dir_path, filename)