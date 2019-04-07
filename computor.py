#!/usr/bin/python3

import sys
import src

def computorv1(expr : str):
	try:
		tokens = src.computorLexer(expr)
	except src.InputError as err:
		print(err)
		sys.exit()

	print(tokens)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage : ./computorV1 expr')
		sys.exit()
	computorv1(sys.argv[1])
	sys.exit()
