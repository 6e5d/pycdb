# operator are c0 style(avoid collision)
table = [
	[],
	[".", "->", "@"],
	["*p", "&p", "-n", "+n", "~", "!", "cast", "sizeof"],
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

# can also used to test if a string is a c0 op
def opprec(op):
	for idx, l in enumerate(table):
		if op in l:
			return idx
	raise Exception(op)
