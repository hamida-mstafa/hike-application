from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    interests =SelectField('interests' choices=[('Cycling','Cycling'),('Fishing','Fishing'),('Camping','Camping'),('Hiking','Hiking')])
    submit = SubmitField('Submit')

class EventForm(FlaskForm):
    event_title = StringField('Title of your Event', validators=[Required()])
    description = TextAreaField('Describe the Event', validators=[Required()])
    category = SelectField('interests' choices=[('Cycling','Cycling'),('Fishing','Fishing'),('Camping','Camping'),('Hiking','Hiking')])
    submit = SubmitField('Pitch It!')

class CommentForm(FlaskForm):
    details = TextAreaField('Leave your comments', validators=[Required()])
    submit = SubmitField('Comment')