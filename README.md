# Idea3
Como requisitos necesitamos tener instalado Python 3.x, GIT y sqlite3

1. Clonamos el repositorio con:

``git clone https://github.com/BarConT/idea3.git``

2. Nos posicionamos dentro del proyecto y ejecutamos el siguiente comando para crear un entrono virtual:

``python -m venv idea3env``

3. Abrimos el proyecto en nuestro editor de código y en la carpeta ``idea3env``, dentro de ``Scripts``, en el archivo ``activate.bat``, si estamos en Windows,
agregamos al final las siguientes variables de entorno:

``set "FLASK_APP=entrypoint.py"``

``set "FLASK_ENV=development"``

Luego  guardamos el archivo.

4. Activamos el entorno con el siguiente comando en nuestra consola:

``idea3env\Scripts\activate.bat``

5. Para instalar los requerimientos en la terminal escribimos:

``pip install -r requirements.txt``

6. Creamos la carpeta imagenes dentro de nuestro proyecto:

``mkdir imagenes``

7. En la consola esribimos ```python``` para abrir el intérprete de Python y tipeamos:

    ```
    from app import db
    from app import create_app
    app = create_app()
    app.app_context().push()
    db.create_all()
    ```
Se creara la base de datos. Cerramos el intérprete de Python(Ctrl + z)

8. En la consola ingresamos a la base de datos con el siguiente comando:

``sqlite3 database.db``

Una vez dentro de la base de datos escribimos:

`` INSERT INTO idea3_user(name, password) VALUES ('ADMIN', 'pbkdf2:sha256:150000$5oClIM0i$c155be080802a2299bf20f891ea9e542c8fb11ea4a5927d390c36d2d91252a60');``

``INSERT INTO categoria(nombre_categoria) VALUES ('Pizzas'), ('Empanadas'), ('Bebidas'), ('Postres y helados');``

Para crear el usuario ADMIN y las categorias. Salimos de la base de datos con el comando:
.exit

9. En la consola, levantamos el servidor de Flask con:
flask run

10. Ya podesmos ingresar en nuestro navegador a la url <http://127.0.0.1:5000> o <http://localhost:5000>

11. Para agregar productos debemos iniciar sesión en <http://127.0.0.1:5000/login>

``Nombre: ADMIN``

``Contraseña: 1234``

Ya podemos ir a la pestaña Nueva Comida y empezar agregar nuevas comidas.
