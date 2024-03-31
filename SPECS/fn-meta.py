#!/usr/bin/python

import re
import sys

def name():
	return "Name: epics-%{repo}\n"

def license(arg):
	if arg == "EPICS":
		arg = "EPICS Open License"
	return "License: %s\n" % arg

def github(proj):
	return "URL: https://github.com/%s/%%{repo}\n" % proj + \
		"Source0: %%{github_archive %s %%{repo} %%{commit}}\n" % proj

def version(ver, rel):
	ret = "Version: %s\n" % ("%(echo %{commit} | sed 's/^[Rv]//; s/-/_/g')\n"
		if ver == "commit" else ver)
	ret += "Release: %s.el%%{rhel}\n" % re.sub(r"\.(commit)$", r".%{\1}", rel)
	return ret

try:
	for farg in sys.argv[1:]:
		farg = farg.split("=", 1)
		fn, args = farg[0], ([] if len(farg) == 1 else farg[1].split(","))
		sys.stdout.write(globals()[fn](*args))
except:
	sys.stdout.write("%prep\n%prep\n")
	raise

