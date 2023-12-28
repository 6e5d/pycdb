from gid import gid2path
def gid2include(target):
	if isinstance(target, tuple):
		target = list(target)
	assert isinstance(target, list)
	if target[:3] != ["com", "6e5d", "syslib"]:
		s = gid2path(target)
		raise Exception(s)
	target = target[3:]
	if target[0] in ["std", "posix"]:
		return "<" + "/".join(target[1:]) + ".h>"
	match target:
		case ["cglm"]:
			return "<cglm/cglm.h>"
		case x:
			raise Exception(x)

def gid2links(target):
	if isinstance(target, tuple):
		target = list(target)
	assert isinstance(target, list)
	if target[:3] != ["com", "6e5d", "syslib"]:
		s = gid2path(target)
		raise Exception(s)
	target = target[3:]
	if target == ["std", "math"]:
		return ["-lm"]
	if target[0] in ["std", "posix"]:
		return []
	match target:
		case ["cglm"]:
			return ["-lm", "-lcglm"]
		case x:
			raise Exception(x)
