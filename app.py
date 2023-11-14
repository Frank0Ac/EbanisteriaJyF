from flask import Flask
from flask import send_from_directory
import os
from flask import request
from flask import make_response
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from model import User

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype = 'image/vnd.microsoft.icon')

@app.route("/home")
def inicio():
    return render_template('home.html')

@app.route("/")
def index():
    print (f"Ruta creada: {url_for('inicio')}")
    return redirect(url_for('inicio'))

@app.route("/entrar-no-permitido")
def no_autorizado():
    abort(401)

@app.errorhandler(401)
def pagina_no_autorizado(error):
    return "Acceso no autorizado. No tienes permiso para ver esta página.", 401

@app.errorhandler(404)
def page_not_found(error):
    # return "Página no encontrada personalizada...", 404
    return '<img src="' + url_for('static', filename='imagenes/error404.png') + '"/>', 404

@app.route('/galeria')
def galeria():
    muebles = [
        {'nombre': 'Mueble', 'imagen': 'mueble.jpg'},
        {'nombre': 'Silla', 'imagen': 'silla.jpg'},
        {'nombre': 'Mesa', 'imagen': 'mesa.jpg'},
        {'nombre': 'Cocina', 'imagen': 'cocina.jpg'},
        {'nombre': 'Armario', 'imagen': 'armario.jpg'},
        {'nombre': 'Gradas', 'imagen': 'gradas.jpg'},
        {'nombre': 'Pasamanos', 'imagen': 'pasamanos.jpg'},
        {'nombre': 'Ventanas', 'imagen': 'ventanas.jpg'},
    ]
    return render_template('galeria.html', muebles=muebles)

@app.route('/blog')
def blog():
    # Muestra una lista de entradas de blog
    return render_template('blog.html')

@app.route('/contacto')
def contacto():
    # Datos de contacto del propietario
    datos_contacto = {
        'nombre': 'Andres Hernandez',
        'correo': 'andreszarama15@gmail.com',
        'telefono': '3167953026',
        'direccion': 'Heraldo Romero, Ipiales',

        'nombre2': 'Juan Rivera',
        'correo2': 'riverajuansebastian273@gmail.com',
        'telefono2': '3164790952',
        'direccion2': 'Heraldo Romero, Ipiales'
    }
    return render_template('contacto.html', datos_contacto=datos_contacto)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.get(username)
        if user and user.check_password(password):
            return redirect(url_for('profile', username=username))
        else:
            return 'Credenciales inválidas. Por favor, inténtalo de nuevo.'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if User.get(username):
            return 'El usuario ya existe. Por favor, elige otro nombre de usuario.'
        else:
            new_user = User(username, password, email)
            User.create(new_user)
            return 'Registro exitoso. <a href="/login">Inicia sesión</a>'

    return render_template('register.html')

@app.route('/profile/<username>')
def profile(username):
    user = User.get(username)
    if user:
        return render_template('profile.html', user=user)
    else:
        return 'Usuario no encontrado'

@app.route('/acercade')
def acerca_de():
    return render_template('acerca_de.html')

@app.route("/about")
def about():
    return redirect("/acercade")

if __name__ == '__main__':
    app.run(port=9090, debug = True)