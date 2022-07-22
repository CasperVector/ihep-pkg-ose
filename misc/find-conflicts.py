#!/usr/bin/python

import sys
from subprocess import check_output

fdic = {}
for pkg in sys.argv:
	for f in check_output(
		["repoquery", "--enablerepo=ihep", "-l", pkg]
	).splitlines():
		fdic.setdefault(f.decode("UTF-8"), []).append(pkg)
for f in sorted(fdic):
	if len(fdic[f]) > 1:
		print(f + ": " + " ".join(fdic[f]))

