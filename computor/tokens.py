
class CTokens:
	variable =		'X'
	variable_alt =	'x'
	addop =		'+'
	subop =		'-'
	mulop =		'*'
	divop =		'/'
	operators = [addop, subop, mulop, divop]
	pow_sign =		'^'
	equal_sign =	'='
	numbers =		'0123456789'
	valid_tokens =	[
					variable,
					variable_alt,
					pow_sign,
					equal_sign,
					open_par,
					close_par,
					]
	valid_tokens += operators
	for n in numbers:
		valid_tokens.append(n)
