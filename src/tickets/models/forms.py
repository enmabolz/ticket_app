from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo, InputRequired
from tickets.models.models import Users


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField(validators=[Length(min=1, max=100), DataRequired()])
    submit = SubmitField(label="Log In")


class RegisterForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    lastname = StringField(validators=[DataRequired()])
    birthdate = DateField(validators=[InputRequired()], format='%Y-%m-%d')
    is_admin = BooleanField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    password_confirmation = PasswordField(validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Register")

    def validate_email(self, email_to_check):
        if Users.query.filter_by(email=email_to_check.data).first():
            raise ValidationError("Email already exist. Please try another one")