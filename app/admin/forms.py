from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

class ComidaForm(FlaskForm):
    nombre = StringField('Título', validators=[DataRequired(), Length(max=128)])
    categoria = SelectField('Categoria', choices=[])
    precio = IntegerField()
    submit = SubmitField('Enviar')