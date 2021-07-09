from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    thought = StringField('Negative Thought', validators=[DataRequired()])
    submit = SubmitField('Reframe')
