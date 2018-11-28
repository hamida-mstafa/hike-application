from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    # interests = SelectField('interests', choices=[('Cycling','Cycling'),('Fishing','Fishing'),(('Camping','Camping'),('Hiking','Hiking')], validators=[Required()])

    submit = SubmitField('Submit')

class EventForm(FlaskForm):
    event_title = StringField('Title of your Event', validators=[Required()])
    description = TextAreaField('Describe the Event', validators=[Required()])
    # category = interests = SelectField('category', choices=[('Cycling','Cycling'),('Fishing','Fishing'),(('Camping','Camping'),('Hiking','Hiking')], validators=[Required()])
    organisation = StringField('The name of the organisaion', validators=[Required()])
    contact = StringField('Contact information of the organisation', validators=[Required()])
    location = StringField('The location of the event', validators=[Required()])
    submit = SubmitField('Post Event')
    
class ReviewForm(FlaskForm):
    content = TextAreaField('Leave your reviews on the event', validators=[Required()])
    submit = SubmitField('Review')