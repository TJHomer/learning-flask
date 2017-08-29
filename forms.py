from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("You really need to enter your name here.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
    email = StringField('Email', validators=[DataRequired("Your email is requried for our tracking purposes."), Email("That's not a real email, c'mon now.")])
    password = PasswordField('Password', validators=[DataRequired("That's not a very secure password."), Length(min=6, message='You can do better than that (6 chars plz)')])
    submit = SubmitField('Sign up')