
class CTokens:
	variable =		'X'
	plus_sign =		'+'
	minus_sign =	'-'
	operators = [plus_sign, minus_sign]
	pow_sign =		'^'
	equal_sign =	'='
	numbers =		'0123456789'
	valid_tokens =	[
					variable,
					plus_sign,
					minus_sign,
					mul_sign,
					div_sign,
					pow_sign,
					equal_sign,
					open_par,
					close_par,
					]
	for n in numbers:
		valid_tokens.append(n)
