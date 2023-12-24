# operator are c0 style(avoid collision)
table = [
	[],
	[".", "->"],
	["*p", "&p", "-n", "+n", "~", "!"],
	["*", "/", "%"],
	["+", "-"],
	["<<", ">>"],
	["<", ">", "<=", ">="],
	["==", "!="],
	["&"],
	["^"],
	["|"],
	["&&"],
	["||"],
	["?:"],
	["=", "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", "&=", "|=", "^="],
	[","],
]

def opprec(op):
	for idx, l in enumerate(table):
		if op in l:
			return idx
	raise Exception(op)
