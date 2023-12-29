from gid import gid2path
from syslib import add_sysdep

def gid2file(target):
	if isinstance(target, tuple):
		target = list(target)
	assert isinstance(target, list)
	name = target[-1]
	if target[:3] != ["com", "6e5d", "syslib"]:
		s = gid2path(target)
		incl = s / "build" / f"{name}.h"
		return (
			[f'"{incl}"'],
			[s / "build" / f"lib{name}.so"],
		)
	links = []
	includes = []
	if target[3] in ["std", "posix"]:
		if target[3:] == ["std", "math"]:
			links = ["-lm"]
		includes = ["<" + "/".join(target[4:]) + ".h>"]
	else:
		d = add_sysdep(target)
		links = d["links"]
		includes = d["includes"]
	return (includes, links)
