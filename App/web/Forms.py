from wtforms import Form, StringField, TextAreaField, IntegerField, FileField, RadioField, FloatField, validators, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField,DateField
import datetime

class Register(Form):
    username = StringField("Username", [validators.InputRequired(), validators.Length(min=1, max=150)])
    email = EmailField("Email", [validators.InputRequired(), validators.Email()])
    password = PasswordField("Password", [validators.Length(min=8, max=150), validators.InputRequired()])

class SignIn(Form):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])

class ContactUs(Form):
    name = StringField('Name', [validators.Length(max=50), validators.InputRequired()])
    email = EmailField('Email Address', [validators.Email(), validators.InputRequired()])
    subject = StringField('Subject', [validators.Length(min=1,max=150), validators.InputRequired()])
    message = TextAreaField('Messsage', [validators.InputRequired()])

class SearchForm(Form):
    Search=StringField("",[validators.Optional()])
