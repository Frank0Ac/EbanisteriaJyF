from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from flask_wtf.file import FileRequired, FileAllowed

class MiFormulario(FlaskForm):
    campo_nombre = StringField('Nombre')
    imagen = FileField('Imagen')
    boton_enviar = SubmitField('Enviar')