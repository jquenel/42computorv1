#	EXPERT SYSTEM
#
#	ecole 42
#	Joackim Quenel

from computor.combinators import *
from computor.classes import PNTerm

def keyword(kw):
	return Reserved(kw, 'RESERVED')
coef = Tag('NUM') ^ (lambda n : float(n))
num = coef ^ (lambda n : (n, float(n) == int(n)))
equal_sep = keyword('=')
term_sign = (keyword('+') | keyword('-')) ^ (lambda v : -1 if v[0] == '-' else 1)
variable = keyword('X') | keyword('x')
degree_expr = keyword('^') + num

def expr_parse(tokens):
	return parser()(tokens, 0)

def parser():
	return Phrase(full_expr())

def full_expr():
	return term_list() + equal_sep + term_list() #^ inverse_coefs)

def inverse_coefs(terms):
	for term in terms:
		if term :
			term.coef *= -1

def term_list():
	return first_term() + Rep(term())

def first_term():
	return (single_coef() \
			| signed_single_coef() \
			| with_var()) ^ build_term

def term():
	return (signed_single_coef() \
			| signed_with_var()) ^ build_term

def single_coef():
	return coef ^ (lambda c : (None, (c, None)))

def signed_single_coef():
	return (term_sign + coef) ^ (lambda c : (s, (c, None)))

def with_var():
	return (Opt(term_sign) + (Opt(coef) + variable + Opt(degree_expr))) 

def signed_with_var():
	return term_sign + (Opt(coef) + variable + Opt(degree_expr))

def build_term(parsed):
	print(parsed)
	(sign, (coef, var_part)) = parsed
	if sign is None:
		sign = 1
	if coef is None:
		coef = 1
	if var_part is None:
		(degree, valid) = (0, True)
	else:
		__, degree_part = var_part
		if degree_part is None:
			(degree, valid) = (1, True)
		else:
			print(degree_part)
			(degree, valid) = degree_part
	if coef == 0 or not valid:
		return None
	return PNTerm(coef * sign, degree)
