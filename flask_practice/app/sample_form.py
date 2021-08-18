from werkzeug.utils import validate_arguments
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SampleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    # name is the function
    # 'Name' is the label
    # validators used for valid input
    submit = SubmitField('Submit')
