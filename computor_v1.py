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
	polynomial.reduced = polynomial.reduce()
	solutions = solve(polynomial)
	print("Reduced polynomial :")
	print(polynomial.reduced)
	if solutions is not None:
		print(solutions[1])
		if solutions[0] is not None:
			for s in solutions[0]:
				if s[0] is not None:
					if s[1] is not None:
						print(s[0], '		||   ', s[1])
					else:
						print(s[0])
				else:
					print(s[1])

	

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage : ./computorV1 expr')
		sys.exit()
	computorv1(sys.argv[1])
	sys.exit()
