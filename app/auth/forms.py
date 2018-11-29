from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo,Length
from ..models import User
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField
    
    
class LoginForm(FlaskForm):
    username = StringField('username', validators=[Required(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[Required(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[Required(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[Required(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[Required(), Length(min=8, max=80)])

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
