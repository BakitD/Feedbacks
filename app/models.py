from . import db

class Feedback(db.Model):

	__tablename__ = 'feedbacks'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	comment = db.Column(db.Text())

	def __init__(self, name, email, comment):
		self.name = name
		self.email = email
		self.comment = comment