from pathlib import Path
from .precedence import prectable

def file2set(file):
	pp = Path(__file__).resolve().parent
	result = set()
	for line in open(pp / file):
		line = line.strip()
		if not line:
			continue
		result.add(line)
	return result

# c23
std = file2set("std23.txt")
# posix 2008
posix = file2set("posix2008.txt")
# keyword WithOut Underscore
keywords = file2set("keywords23_wou.txt")

# extra c builtin ops(predef func of expr): sizeof
# excluded: ?: , ++ --
binop = set(["+", "-", "*", "/", "%",
	".", "->", ",",
	"<", ">", "<=", ">=", "==", "!=",
	"<<", ">>", "&", "|", "^",
	"&&", "||",
	"=", "+=", "-=", "*=", "/=", "%=",
	"<<=", ">>=", "&=", "|=", "^=",
])
prefixop = set(["*", "&", "~", "!", "+", "-"])

def test_identifier(s):
	assert isinstance(s, str)
	if not s:
		return False
	if not s[0].isalpha() and s[0] != "_":
		return False
	for ss in s[1:]:
		if not ss.isalnum() and ss != "_":
			return False
	return True

btypes = ["size_t",
	"uint8_t", "uint32_t", "uint64_t",
	"int8_t", "int32_t", "int64_t",
	"void", "int", "long", "float", "double", "char", "bool"]
consts = ["NULL", "false", "true"]

# can also used to test if a string is a c0 op
def opprec(op):
	for idx, l in enumerate(prectable):
		if op in l:
			return idx
	return None
