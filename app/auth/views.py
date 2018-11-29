from flask import render_template,redirect,url_for, flash,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from flask_login import login_user
from ..models import User
from .forms import LoginForm,RegistrationForm
from app import db
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
# from ..email import mail message





@auth.route('/')
def index():
    return render_template('index.html')

@auth.route('/login', methods=['GET','POST'])
# @login_required
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('invalid username or password')
            return redirect(url_for('.index'))
        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc!= '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sig In', form = form)

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password_hash(form.password.data):
#             flash('invalid user or password')
#             return redirect(url_for('auth.login'))

#             if check_password_hash(user.password, form.password.data):
#                 login_user(user, remember=form.remember.data)
            
#         return '<h1>Invalid username or password</h1>'
#         #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

#     return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit(

        )
        return redirect(url_for('auth.login'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('auth/signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


