class Term:
	def __init__(self, coefficient, degree):
		self.coef = coefficient
		self.degree = degree

	def __str__(self):
		return f'{self.coef}*X^{self.degree}'
