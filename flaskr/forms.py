from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class EquationForm(FlaskForm):
    equation = StringField('Equation')
    operation = StringField('Operation')
    send = SubmitField('Send')

