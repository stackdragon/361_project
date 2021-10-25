from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, NumberRange

class SearchForm(FlaskForm):
    zip = StringField ('Enter Zip Code', validators=[DataRequired()], render_kw={"placeholder": "Enter Zip Code"})
    submit = SubmitField('GO')
