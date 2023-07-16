from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField(validators=[Length(min=1, max=100), DataRequired()])
    submit = SubmitField(label="Log In")