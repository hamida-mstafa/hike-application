from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import create_app
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),index = True)
    bio = db.Column(db.String(255))
    interests = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    events = db.relationship('Event',backref = 'user',lazy = "dynamic")
    review = db.relationship('Review',backref = 'user',lazy = "dynamic")


    @property
    def password(self):
        raise AttributeError('You Cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Event(db.Model):
    __tablename__= 'events'

    id = db.Column(db.Integer,primary_key = True)
    event_title = db.Column(db.String())
    description = db.Column(db.String())
    category = db.Column(db.String())