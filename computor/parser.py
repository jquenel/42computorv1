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
		return left + right

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
	
	def build_term(parsed):
		(coef, degree) = parsed
		return [PNTerm(coef, degree)]
	full_term = Opt(coef) + variable_part()
	single_coef = coef ^ format_single_coef
	return (full_term | single_coef) ^ build_term

def variable_part():
	def check_validity(parsed):
		(__, deg_part) = parsed
		if deg_part is None:
			return 0
		else:
			(value, valid) = deg_part
			return value if valid else None

	return (variable + Opt(degree_expr())) ^ check_validity

def degree_expr():
	def format_degree(parsed):
		(__, value) = parsed
		return value
	return (keyword('^') + int_) ^ format_degree
