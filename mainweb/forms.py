from mainweb.models import Users
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):

    def validate_email(self, check_email):
        emailcheck = Users.query.filter_by(email=check_email.data).first()
        if emailcheck:
            raise ValidationError("Email already exist!")


    username = StringField("Username:", [Length(3, 15, "Username must be at least 3-15 characters long!"), DataRequired()])
    email = StringField("Email:", [Email("Invalid email address!"), DataRequired()])
    password1 = PasswordField("Password:", [Length(6, 1000, "Password must be at least 6 characters long!"), DataRequired()])
    password2 = PasswordField("Confirm Password:", [EqualTo("password1", "Password must match!"), DataRequired()])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):

    username = StringField("Username:", [Length(3, 15, "Username must be at least 3-15 characters long!"), DataRequired()])
    password = PasswordField("Password:", [Length(6, 1000, "Password must be at least 6 characters long!"), DataRequired()])
    submit = SubmitField("Create Account")