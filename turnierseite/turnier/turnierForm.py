from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField ,DateField
from wtforms.validators import DataRequired

class TurnierForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    datumDerAustragung = DateField(label='Datum der Austragung', validators=[DataRequired()])
    submit = SubmitField(label="Update")

class GruppeForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    submit = SubmitField(label="Update")

class TeamForm(FlaskForm):
    gruppe = SelectField('Gruppe', coerce=int, validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Update')

class SpieleForm(FlaskForm):
    toreT1 = IntegerField(label='Tore Team 1')
    toreT2 = IntegerField(label='Tore Team 2')
    submit = SubmitField(label="Update")
