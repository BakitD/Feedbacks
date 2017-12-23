from flask import jsonify

from ..models import Feedback


class FeedbackTransformer(object):

	@staticmethod
	def transform(feedback):
		if feedback:
			response = jsonify({'id': feedback.id,
						'email': feedback.email,
						'name': feedback.name,
						'comment': feedback.comment})
		else:
			response = jsonify(message='Not found'), 404
		return response