class TokenError(SyntaxError):
	def __init__(self, token : str, idx : int = None, source : str = None):
		self.errMessage = 'unknown char for token : {}'.format(token)
		if idx is not None:
			self.errMessage += ' on line {}'.format(idx)
		if source is not None:
			self.errMessage += ' : {}'.format(source[:10])
	def __str__(self):
		return self.errMessage

class ParseError(SyntaxError):
	def __str__(self):
		return 'Incorrect sequence while parsing terms. \
Please check your syntax and try again.'

class InputError(SyntaxError):
	def __init__(self, errMessage : str = None):
		self.errMessage = errMessage

	def __str__(self):
		if self.errMessage:
			return self.errMessage
		return """There is a problem with the input.
Please check it before submitting again."""
