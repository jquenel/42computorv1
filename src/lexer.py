#	EXPERT SYSTEM
#
#	ecole 42
#	Joackim Quenel

from src.rgx import findChar
from src.tokens import CTokens
from src.errors import InputError, TokenError

def computorLexer(expr : str) -> dict:
	if str is None or str == '':
		return None
	expr = ''.join(expr.split())
	try:
		tokens = tokenize(expr, CTokens.valid_tokens)
	except TokenError as err:
		print(err)
		raise InputError()
	try:
		tokens = lexer(tokens)
	except LexError as err:
		print(err)
		raise InputError()
	return tokens

def getNumericToken(line : str, i : int) -> str:
	token = ''
	decimal = False
	j = i
	while j < len(line) and (line[j] in CTokens.numbers or line[j] == '.'):
		if line[j] == '.':
			if decimal:
				raise InputError('Invalid number syntax : "{}"'.format(line[i:j + 1]))
			decimal = True
		token += line[j]
		j += 1
	return token

def tokenize(line : str, valid_tokens : list) -> list:
	tokens = []
	i = 0
	while i < len(line):
		foundToken = None
		for j, token in enumerate(valid_tokens):
			if line[i:].startswith(token):
				if token in CTokens.numbers:
					token = getNumericToken(line, i)
				foundToken = token
				break
		if foundToken:
			tokens.append(foundToken)
			i += len(foundToken)
		else:
			raise TokenError(line[i], source = line[i:])
	return tokens
