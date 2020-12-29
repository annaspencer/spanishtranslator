from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class RegisterForm(FlaskForm):

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class NewVocabForm(FlaskForm):

    title =  StringField("Title", validators=[InputRequired()])

class AddWords(FlaskForm):

    
    word =StringField("Word", validators=[InputRequired()])
    translation =StringField("Translation", validators=[InputRequired()])



