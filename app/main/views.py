from flask import render_template, request, jsonify

from . import main
from .. import models
from .. import db
from .forms import FeedbackForm
from .transformers import FeedbackTransformer


@main.route('/', methods=['GET'])
def index():
	return render_template('feedback.html', form=FeedbackForm())


@main.route('/feedbacks', methods=['POST'], defaults={'feedback_id': None})
@main.route('/feedbacks/<int:feedback_id>', methods=['GET'])
def feedback(feedback_id):
	form = FeedbackForm(request.form)
	if request.method == 'POST':
		feedback = models.Feedback(form.name.data, form.email.data, form.comment.data)
		db.session.add(feedback)
		db.session.commit()
		response = FeedbackTransformer.transform(feedback)
	elif request.method == 'GET':
		feedback = models.Feedback.query.filter_by(id=feedback_id).first()
		response = FeedbackTransformer.transform(feedback)
	return response

