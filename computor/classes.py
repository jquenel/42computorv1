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
		self.solutions = []
		self.terms = None
	
	def reduce(self) -> str:
		if self.terms is None:
			raise ReduceError('No terms for reduce. Aborting.')
		for rterm in reversed(self.terms):
			for t in self.terms:
				if not (t is rterm) and t.degree == rterm.degree:
					rterm.coef += t.coef
					self.terms.remove(t)
		self.terms.sort(reverse=True, key=lambda t : t.degree)
		for term in reversed(self.terms):
			if term.coef == int(term.coef):
				term.coef = int(term.coef)
			term.degree = int(term.degree)
			if term.coef == 0:
				self.terms.remove(term)
		return self._format_terms()

	def _format_terms(self) -> str:
		reduced = ''
		if len(self.terms) == 0:
			return '0 = 0'
		for i, term in enumerate(self.terms):
			if i > 0 and term.coef > 0:
				reduced += '+ '
			if term.coef < 0:
				reduced += '- ' if i > 0 else '-'
				if term.coef != -1 or term.degree == 0:
					reduced += f'{abs(term.coef)}'
			elif term.coef != 1:
				reduced += f'{term.coef}'
			if term.coef != 1 and term.coef != -1:
				reduced += '*'
			reduced += 'X'
			reduced += f'^{term.degree}'
			reduced += ' '
		reduced += '= 0'
		return reduced
