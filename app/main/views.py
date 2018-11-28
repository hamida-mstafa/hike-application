
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import Event,Review,User,Plan
from .forms import UpdateProfile,EventForm,ReviewForm
from datetime import datetime

@main.route('/')
def index():
    posts = Event.query.order_by(Event.posted.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/about')
def about():
     return render_template('about.html')

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Event.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/addpost', methods=['GET','POST'])
def addpost():
    event_title = request.form['title']
    description = request.form['subtitle']
    location = request.form['planner']
    organisation = request.form['details']


    post = Event(event_title=event_title, description=description, location=location, organisation=organisation, posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('.index'))

    