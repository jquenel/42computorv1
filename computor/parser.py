#	EXPERT SYSTEM
#
#	ecole 42
#	Joackim Quenel

from computor.combinators import *
from computor.classes import PNTerm

coef = Tag('NUM') ^ (lambda n : float(n))
int_ = coef ^ (lambda n : (n, float(n) == int(n)))

def keyword(kw):
	return Reserved(kw, 'RESERVED')

equal_sep = keyword('=')
term_sign = (keyword('+') | keyword('-'))
variable = keyword('X')

def expr_parse(tokens):
	return parser()(tokens, 0)

def parser():
	def process_full_expr(parsed):
		if parsed is None:
			return None
		(((fl, left), __), (fr, right)) = parsed
		if fl and fl == '-':
			left[0].coef *= -1
		if fr and fr == '-':
			right[0].coef *= -1
		for term in right:
			term.coef *= -1
		polynomial = left + right
		for term in reversed(polynomial):
			if term.degree is None:
				return None
			if term.coef == 0:
				polynomial.remove(term)
		return polynomial

	return Phrase(full_expr()) ^ process_full_expr

def full_expr():
	return Opt(term_sign) + term_list() + equal_sep + (Opt(term_sign) + term_list())

def term_list():
	def expr_sep():
		def format_sep(parsed):
			def process_res_list(l, r):
				if parsed == '-':
					r[0].coef *= -1
				return l + r
			return process_res_list
		return term_sign ^ format_sep

	return term() * expr_sep()

def term():
	def format_single_coef(value):
		return (value, 0)
	
	def format_coef(parsed):
		if parsed:
			value, __ = parsed
			return value
		else:
			return 1
	
	def build_term(parsed):
		(coef, degree) = parsed
		return [PNTerm(coef, degree)]
	full_term = (Opt(coef + Opt(keyword('*'))) ^ format_coef) + variable_part()
	single_coef = coef ^ format_single_coef
	return (full_term | single_coef) ^ build_term

def variable_part():
	def check_validity(parsed):
		(__, deg_part) = parsed
		if deg_part is None:
			return 1
		else:
			(value, valid) = deg_part
			return value if valid else None

	return (variable + Opt(degree_expr())) ^ check_validity

def degree_expr():
	def format_degree(parsed):
		(__, value) = parsed
		return value
	
	def format_signed_degree(parsed):
		sign, value = parsed
		if sign == '-':
			(l, r) = value
			value = (l * -1, r)
		return value

	return (keyword('^') + ((term_sign + int_) ^ format_signed_degree | int_)) ^ format_degree
