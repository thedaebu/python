from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SampleForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')
    #  'Name' is the label
    #  name is the function