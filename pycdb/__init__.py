from pathlib import Path

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
	".", "->",
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
