#	EXPERT SYSTEM
#
#	ecole 42
#	Joackim Quenel

from src.esmanager import ESManager
from src.tokens import ESTokens
from src.eserrors import TokenError
from src.inference import InferenceNode
from src.logic import Logic_t, LGCT_FACT, LGCT_AND, LGCT_OR, \
				LGCT_XOR, LGCT_NOT, LGCT_HNOT

def expertParser(tokenizedInput : dict) -> ESManager:
	labels = ''
	facts = []
	initFacts, labels = parseInitFacts(tokenizedInput['initFacts'], labels, facts)
	queries, labels = parseQueries(tokenizedInput['queries'], labels, facts)
	rules, labels = parseRules(tokenizedInput['rules'], labels, facts)
	manager = ESManager(rules, initFacts, queries, facts)
	return manager

def parseRules(tokenizedRules : list, labels : str, facts : list) -> tuple:
	rules = []
	return rules, labels

def parseInitFacts(tokenizedInitFacts : list, labels : str, facts : list) -> tuple:
	initFacts = []
	for line in tokenizedInitFacts:
		i = 0
		if line.tokens[i] != ESTokens.initFact:
			raise TokenError(line.tokens[i], line.idx, line.source)
		i += 1
		while i < len(line.tokens):
			if not line.tokens[i] in ESTokens.facts:
				raise TokenError(line.tokens[i], line.idx, line.source)
			if not line.tokens[i] in labels:
				labels += line.tokens[i]
				newFact = InferenceNode(LGCT_FACT, line, label = line.tokens[i]) 
				facts.append(newFact)
				initFacts.append(newFact)
			i += 1
	return initFacts, labels

def parseQueries(tokenizedQueries : list, labels : str, facts : list) -> tuple:
	queries = []
	for line in tokenizedQueries:
		i = 0
		if line.tokens[i] != ESTokens.query:
			raise TokenError(line.tokens[i], line.idx, line.source)
		i += 1
		while i < len(line.tokens):
			if not line.tokens[i] in ESTokens.facts:
				raise TokenError(line.tokens[i], line.idx, line.source)
			if not line.tokens[i] in labels:
				labels += line.tokens[i]
				newFact = InferenceNode(LGCT_FACT, line, label = line.tokens[i]) 
				facts.append(newFact)
				queries.append(newFact)
			i += 1
	return queries, labels
