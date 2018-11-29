from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import create_app,login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
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

    def check_password_hash(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Event(db.Model):
    __tablename__= 'events'

    id = db.Column(db.Integer,primary_key = True)
    event_title = db.Column(db.String())
    description = db.Column(db.String())
    location = db.Column(db.String())
    organisation = db.Column(db.String())
    contact = db.Column(db.String())
    category = db.Column(db.String())
    pic_path = db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    plan = db.relationship('Plan',backref = 'event',lazy = "dynamic")
    review = db.relationship('Review',backref = 'event',lazy = "dynamic")

    author = db.Column(db.Integer,db.ForeignKey("users.id"))
    

    def save_event(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_event(cls,id):
        events = Event.query.filter_by(id=id)
        return events

    def __repr__(self):
        return f'Pitch {self.pitch_title}'

class Review(db.Model):
    __tablename__='reviews'

    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String())
    event_id = db.Column(db.Integer,db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(pitch_id=id).all()
        return reviews

class Plan(db.Model):
    __tablename__='plans'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),index = True)
    Address = db.Column(db.String())
    organisation = db.Column(db.String())

    password_hash = db.Column(db.String(255))
   
    event_id = db.Column(db.Integer,db.ForeignKey('events.id'))
    

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
