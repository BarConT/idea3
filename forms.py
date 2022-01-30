from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length

class ComidaForm(FlaskForm):
    nombre = StringField('Título', validators=[DataRequired(), Length(max=128)])
    categoria = StringField('Categoría')
    precio = IntegerField()
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar Sesión')