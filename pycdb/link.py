from . import header

data = {
	"wayland-util.h": [],
	"math.h": ["m"],
	"tgmath.h": ["m"],
	"cglm/cglm.h": ["cglm", "m"],
}

def link_lookup(path):
	if path in data:
		return [f"-l{x}" for x in data[path]]
	if path in header.std or path in header.posix:
		return []
	path = path.removesuffix(".h")
	path = path.split("/")[0]
	if path == "sys":
		return []
	return [f"-l{path}"]
