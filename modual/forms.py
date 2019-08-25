from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(message='please input your name'),Length(1,20)])
    password = StringField('password',validators=[DataRequired(message='please input your password'),Length(3,16)])
    remember_me = BooleanField('remember me')
    submit = SubmitField('login in')

class Regiestr(FlaskForm):
    username = StringField('username',validators=[DataRequired(message='please input your name'),Length(1,20)])
    password = StringField('password',validators=[DataRequired(message='please input your password'),Length(3,16)])
    #remember_me = BooleanField('remember me')
    submit = SubmitField('confirm Regiest')