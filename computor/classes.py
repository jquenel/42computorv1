class TermOperationError(Exception):
	def __init__(self, err):
		self.err = err
	
	def __str__(self):
		return self.err

class PNTerm:
	def __init__(self, coefficient, degree):
		self.coef = coefficient
		self.degree = degree

	def __str__(self):
		return f'{self.coef}*X^{self.degree}'
	
	def __add__(self, other):
		if self.degree != other.degree:
			raise TermOperationError
		return PNTerm(self.coef + other.coef, self.degree)
	
	def __mul__(self, other):
		return PNTerm(self.coef * other.coef, self.degree + other.degree)
	
	def __div__(self, other):
		return PNTterm(self.coef / other.coef, self.degree - other.degree)
