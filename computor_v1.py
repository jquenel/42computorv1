#!/usr/bin/env python3.6

import sys
import computor
from computor.parser import expr_parse

def computorv1(expr : str):
	try:
		tokens = computor.lexer(expr)
		parsed = expr_parse(tokens)
		print(parsed)
	except computor.InputError as err:
		print(err)
		sys.exit()

	print(tokens)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage : ./computorV1 expr')
		sys.exit()
	computorv1(sys.argv[1])
	sys.exit()
