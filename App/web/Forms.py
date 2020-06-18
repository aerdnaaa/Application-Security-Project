from wtforms import Form, StringField, TextAreaField, IntegerField, FileField, RadioField, FloatField, validators, PasswordField, SelectField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField,DateField
import datetime

class Register(Form):
    username = StringField("Username", [validators.InputRequired(), validators.Length(min=1, max=150)])
    email = EmailField("Email", [validators.InputRequired(), validators.Email()])
    password = PasswordField("Password", [validators.Length(min=8, max=150), validators.InputRequired()])
    question = SelectField('Secruity Question', [validators.DataRequired()], choices=
                [("What is the middle name of your mother?", "What is the middle name of your mother?"),
                ("What is the name of your pet?", "What is the name of your pet?"), 
                ("What is the first thing you learnt to cook?", "What is the first thing you learnt to cook?"),
                ("What was the first film you saw in cinema?", "What was the first film you saw in cinema?"),
                ("Where was the first place you went to on a plane?", "Where was the first place you went to on a plane?"),
                ("What is the name of your favourite teacher?", "What is the name of your favourite teacher?")], 
                default="What is the middle name of your mother?")
    answer = StringField("Answer", [validators.InputRequired(), validators.Length(min=1, max=150)])

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
