class TokenError(SyntaxError):
	def __init__(self, token : str, idx : int = None, source : str = None):
		self.errMessage = 'wrong token for initial fact : {}'.format(token)
		if idx is not None:
			self.errMessage += ' on line {}'.format(idx)
		if source is not None:
			self.errMessage += ' : {}'.format(source[:10])
	def __str__(self):
		return self.errMessage

class InputError(SyntaxError):
	def __init__(self, errMessage : str = None):
		self.errMessage = errMessage

	def __str__(self):
		if self.errMessage:
			return self.errMessage
		return """There is a problem with the input.
Please check it before submitting again."""
