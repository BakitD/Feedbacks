from flaskm import jsonify

from . import Feedback


class FeedbackTransformer(object):

	@staticmethod
	def transform(model):
		return jsonify(model)