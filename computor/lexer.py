#	EXPERT SYSTEM
#
#	ecole 42
#	Joackim Quenel

from computor.rgx import findChar
from computor.tokens import CTokens
from computor.errors import InputError, TokenError

def lexer(expr : str) -> dict:
	if str is None or str == '':
		return None
	expr = ''.join(expr.split())
	try:
		tokens = tokenize(expr, CTokens.valid_tokens)
		#tokens = lex(tokens)
	except TokenError, LexError as err:
		print(err)
		raise InputError()
	return tokens

def get_numeric_token(line : str, i : int) -> str:
	token = ''
	decimal = False
	j = i
	while j < len(line) and (line[j] in CTokens.numbers or line[j] == '.'):
		if line[j] == '.':
			if decimal:
				raise InputError(f'Invalid number syntax : "{line[i : j + 1]}"')
			decimal = True
		token += line[j]
		j += 1
	return token

def tokenize(line : str, valid_tokens : list) -> list:
	tokens = []
	i = 0
	while i < len(line):
		found_token = None
		for j, token in enumerate(valid_tokens):
			if line[i:].startswith(token):
				if token in CTokens.numbers:
					token = get_numeric_token(line, i)
				found_token = token
				break
		if found_token:
			tokens.append(found_token)
			i += len(found_token)
		else:
			raise TokenError(line[i], source = line[i:])
	return tokens
