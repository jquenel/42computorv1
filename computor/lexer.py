#	EXPERT SYSTEM
#
#	ecole 42
#	Joackim Quenel

from computor.errors import InputError, TokenError

def lexer(expr : str) -> dict:
	valid_tokens = {
		'RESERVED' : 	'Xx+-*/^=',
		'NUM' : 		'0123456789.'
	}
	if str is None or str == '':
		return None
	expr = ''.join(expr.split())
	try:
		tokens = tokenize(expr, valid_tokens)
	except TokenError as err:
		print(err)
		raise InputError()
	return tokens

def get_numeric_token(line : str, i : int, chars : list) -> str:
	token = ''
	decimal = False
	j = i
	while j < len(line) and (line[j] in chars or line[j] == '.'):
		if j - i > 12:
			raise InputError('Number phrase too large to compute with precision')
		if line[j] == '.':
			if decimal:
				raise InputError(f'Invalid number syntax : "{line[i : j + 1]}"')
			decimal = True
		token += line[j]
		j += 1
	return token

def tokenize(line : str, valid_tokens : dict) -> list:
	tokens = []
	i = 0
	while i < len(line):
		found_token = None
		for k, chars in valid_tokens.items():
			if line[i] in chars:
				if k == 'NUM':
					token = get_numeric_token(line, i, chars)
					found_token = token
				else:
					found_token = line[i]
				break
		if found_token:
			tokens.append((found_token, k))
			i += len(found_token)
		else:
			raise TokenError(line[i], source = line[i:])
	return tokens
