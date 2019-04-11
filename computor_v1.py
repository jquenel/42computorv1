#!/usr/bin/env python3.6

import sys
from computor import *

def computorv1(expr : str):
	polynomial = Polynomial(expr)
	try:
		tokens = lexer(expr)
		parsed = expr_parse(tokens)
		if parsed is None or parsed.value is None:
			raise ParseError()
		polynomial.terms = parsed.value
	except (InputError, ParseError) as err:
		print(err)
		sys.exit()
	print(polynomial.terms)
	polynomial.reduced = polynomial.reduce()
	print(polynomial.terms)
	print(polynomial.reduced)
	

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage : ./computorV1 expr')
		sys.exit()
	computorv1(sys.argv[1])
	sys.exit()
