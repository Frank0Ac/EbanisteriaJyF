import os
from flask import Flask, send_from_directory, request, make_response, abort, redirect, url_for, render_template, flash
from model import db, User
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed
from model import Image
from flask_wtf.csrf import CSRFError, validate_csrf, generate_csrf
from forms import MiFormulario
from werkzeug.utils import secure_filename
import logging
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datosDB.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = '564810'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 
migrate = Migrate(app, db)



# manejo de sesiones de usuario
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Configurar el sistema de registros
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# Configuración de paginación
PER_PAGE = 10  # Número de productos por página
# Definición del modelo Product
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.context_processor
def inject_user():
    return {'current_user': current_user}

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
    return '<img src="' + url_for('static', filename='imagenes/error404.png') + '"/>', 404

@app.route("/error-servidor")
def errorservidor():
    abort(500)

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Error interno del servidor')
    return render_template('error.html', error_code=500), 500

@app.route('/galeria', methods=['GET', 'POST'])
def galeria():
    form = MiFormulario()

    if form.validate_on_submit():
        print("Formulario enviado correctamente")
        print(f"Imagen del usuario actual: {current_user.images}")

    # Filtrar solo las imágenes públicas
    all_images = Image.query.filter_by(is_public=True).all()

    return render_template('galeria.html', form=form, user_images=all_images)

@app.route('/productos')
def productos():
    # Obtener la página actual de la URL
    page = request.args.get(get_page_parameter(), type=int, default=1)

    # Consulta para obtener todos los productos desde la base de datos
    all_products = Product.query.paginate(page=page, per_page=PER_PAGE)

    # Configurar la paginación
    pagination = Pagination(page=page, total=all_products.total, per_page=PER_PAGE, css_framework='bootstrap4')

    return render_template('productos.html', products=all_products.items, pagination=pagination)

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
            login_user(user)  # Asegúrate de llamar a login_user aquí
            return redirect(url_for('profile', username=username))
        else:
            return 'Credenciales inválidas. Por favor, inténtalo de nuevo.'

    return render_template('login.html')

# Cargar configuración para imágenes
uploaded_images = UploadSet('images', IMAGES)
app.config['UPLOADED_IMAGES_DEST'] = 'static/uploads'
app.config['UPLOADED_IMAGES_ALLOW'] = set(['jpg', 'jpeg', 'png', 'gif'])
configure_uploads(app, uploaded_images)

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    if not current_user.is_superuser:
        flash('Solo el superusuario puede cargar imágenes.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        if 'imagen' not in request.files:
            return redirect(request.url)
        
        imagen = request.files['imagen']
        
        if imagen.filename == '':
            return redirect(request.url)
            
        if imagen:
            filename = secure_filename(imagen.filename)    
            imagen.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            new_image = Image(filename=filename, author=current_user, is_public=True)
            db.session.add(new_image)
            db.session.commit()

            return redirect(url_for('galeria'))
    return render_template('galeria.html')

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
@login_required
def profile(username):
    user = User.get(username)
    if user:
        return render_template('profile.html', user=user)
    else:
        return 'Usuario no encontrado'
    
@app.route('/logout')
@login_required  # Esta decoración asegura que solo los usuarios autenticados puedan cerrar sesión
def logout():
    logout_user()
    return redirect(url_for('inicio'))

@app.route('/acercade')
def acerca_de():
    return render_template('acerca_de.html')

@app.route("/about")
def about():
    return redirect("/acercade")

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=9090, debug = True)