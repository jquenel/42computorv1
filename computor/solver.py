from computor import Polynomial

def solve(polynomial : Polynomial) -> tuple:
	if len(polynomial) == 0:
		return zero_term_solution()
	elif len(polynomial) == 1:
		return one_term_solution(polynomial)
	elif polynomial.terms[0].degree == 1\
			and not polynomial.terms[-1].degree < 0:
		return first_degree_solution(polynomial)
	elif polynomial.terms[0].degree == 2\
			and not polynomial.terms[-1].degree < 0:
		return second_degree_solution(polynomial)
	else:
		return other_solution(polynomial)

def zero_term_solution():
	return None, 'This is an identity : all real numbers are root.'

def one_term_solution(polynomial):
	if polynomial.terms[0].degree <= 0:
		return [], 'There is no solution.'
	else:
		return [(0, None)], 'The solution is :'

def first_degree_solution(polynomial):
	a = polynomial.terms[0].coef
	b = polynomial.terms[1].coef
	value = -b / a
	if value == int(value):
		value = int(value)
	if int(value) != value and int(b) == b and int(a) == a:
		b = int(b)
		a = int(a)
		if a < 0:
			b = -b
			a = -a
		str_ = f'{-b} / {a}'
	else:
		str_ = None
	sol = (value, str_)
	return [sol], 'Polynomial of degree 1.\nThe solution is :' 

def sqrt(n):
	x = n / 2
	while x * x > n:
		x /= 2
	i = 0
	while x * x != n and i < 100:
		x = (x + (n / x)) / 2
		i += 1
	if x == int(x):
		x = int(x)
	return x

def second_degree_solution(polynomial):
	def positive_dis(a, b, d):
		value_a = (-b + sqrt(d)) / (2 * a)
		if value_a == int(value_a):
			value_a = int(value_a)
		str_a = None
		if int(value_a) != value_a \
			and int(2 * a) == 2 * a and int(b) == b and int(d) == d:
				if int(sqrt(d)) == sqrt(d):
					str_a = f'{-b + sqrt(d)} / {2 * a}'
				else:
					if b != 0:
						str_a = f'({-b} + √({d})) / {2 * a}'
					else:
						str_a = f'√({d}) / {2 * a}'
		sol_a = (value_a, str_a)
		value_b = (-b - sqrt(d)) / (2 * a)
		if value_b == int(value_b):
			value_b = int(value_b)
		str_b = None
		if int(value_b) != value_b \
			and int(2 * a) == 2 * a and int(b) == b and int(d) == d:
				if int(sqrt(d)) == sqrt(d):
					str_b = f'{-b - sqrt(d)} / {2 * a}'
				else:
					if b != 0:
						str_b = f'({-b} - √({d})) / {2 * a}'
					else:
						str_b = f'-√({d}) / {2 * a}'
		sol_b = (value_b, str_b)
		return [sol_a, sol_b], '''Polynomial of degree 2.
With a positive discriminer, the solutions are :'''

	def null_dis(a, b):
		value_a = (-b) / (2 * a)
		if value_a == int(value_a):
			value_a = int(value_a)
		str_a = None
		if int(value_a) != value_a \
				and int(-b) == -b\
				and int(2 * a) == 2 * a:
			str_a = f'{-b} / {2 * a}'
		sol_a = (value_a, str_a)
		return [sol_a], '''Polynomial of degree 2.
With a null discriminer, the solution is :'''

	def negative_dis(a, b, d):
		if b != 0:
			str_a = f'({-b} + i√({-d})) / {2 * a}'
			str_b = f'({-b} - i√({-d})) / {2 * a}'
		else:
			str_a = f'i√({-d}) / {2 * a}'
			str_b = f'-i√({-d}) / {2 * a}'
		sol_a = (None, str_a)
		sol_b = (None, str_b)
		return [sol_a, sol_b], '''Polynomial of degree 2.
With a negative discriminer, the complexe solutions are :'''

	a = 0
	b = 0
	c = 0
	for term in polynomial.terms:
		if term.degree == 2:
			a = term.coef
			if int(a) == a:
				a = int(a)
		elif term.degree == 1:
			b = term.coef
			if int(b) == b:
				b = int(b)
		elif term.degree == 0:
			c = term.coef
			if int(c) == c:
				c = int(c)
	d = b * b - 4 * a * c
	if int(d) == d:
		d = int(d)
	if d > 0:
		return positive_dis(a, b, d)
	elif d == 0:
		return null_dis(a, b)
	else:
		return negative_dis(a, b, d)

def other_solution(polynomial):
	return [], "Other solutions ?"
