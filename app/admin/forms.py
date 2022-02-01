from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length

class ComidaForm(FlaskForm):
    nombre = StringField('Título', validators=[DataRequired('El campo es obligatorio'), Length(max=128)])
    categoria = SelectField('Categoria', choices=[])
    precio = IntegerField(validators=[DataRequired('Valor no válido')])
    comida_image = FileField('Imagen comida', validators=[
        FileAllowed(['jpg', 'png'], 'Solo se permiten imágenes')
    ])
    submit = SubmitField('Enviar')