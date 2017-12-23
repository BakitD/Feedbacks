from flask_wtf import FlaskForm
from wtforms import StringField, TextField, validators
from wtforms.fields.html5 import EmailField


class FeedbackForm(FlaskForm):
	name = StringField('Name', [validators.DataRequired('Enter name')])
	email = EmailField('Email', [validators.Email('Enter email')])
	comment = TextField('Comment', [validators.DataRequired('Enter comment')])