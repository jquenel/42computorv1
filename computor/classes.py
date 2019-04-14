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

	def __repr__(self):
		return f'PNterm({self.coef}, {self.degree})'
	
	def __add__(self, other):
		if self.degree != other.degree:
			raise TermOperationError
		return PNTerm(self.coef + other.coef, self.degree)
	
	def __mul__(self, other):
		return PNTerm(self.coef * other.coef, self.degree + other.degree)
	
	def __div__(self, other):
		return PNTterm(self.coef / other.coef, self.degree - other.degree)

class PolynomialError(Exception):
	def __init__(self, err):
		self.err = err
	
	def __str__(self):
		return self.err
	
class Polynomial:
	def __init__(self, source):
		self.source = source
		self.reduced = None
		self.terms = None
	
	def __len__(self):
		return len(self.terms)
	
	def reduce(self):
		if self.terms is None:
			raise ReduceError('No terms for reduce. Aborting.')
		for term in self.terms:
			for rt in reversed(self.terms):
				if not (term is rt) and term.degree == rt.degree:
					term.coef += rt.coef
					self.terms.remove(rt)

		self.terms.sort(reverse=True, key=lambda t : t.degree)
		for term in reversed(self.terms):
			if term.coef == int(term.coef):
				term.coef = int(term.coef)
			if term.degree == int(term.degree): 
				term.degree = int(term.degree)
			if term.coef == 0:
				self.terms.remove(term)

	def format_terms(self) -> str:
		reduced = ''
		if len(self.terms) == 0:
			return '0 = 0'
		for i, term in enumerate(self.terms):
			if i > 0 and term.coef > 0:
				reduced += '+ '
			if term.coef < 0:
				reduced += '- ' if i > 0 else '-'
				reduced += f'{abs(term.coef)}'
			else:
				reduced += f'{term.coef}'
			reduced += f'*X^{term.degree} '
		reduced += '= 0'
		return reduced
