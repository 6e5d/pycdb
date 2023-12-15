from . import std, posix

def system_header(file):
	if file in std:
		return "std"
	if file in posix:
		return "posix"
	return "external"
