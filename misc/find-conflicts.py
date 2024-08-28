#!/usr/bin/python3

import sys
from subprocess import check_output

fdic = {}
for pkg in sys.argv:
	for f in check_output(
		["repoquery", "--enablerepo=ihep", "-l", pkg]
	).splitlines():
		if f.startswith(b"/usr/lib/.build-id/") or \
			f == b"/usr/lib/.build-id":
			continue
		fdic.setdefault(f.decode("UTF-8"), []).append(pkg)
for f in sorted(fdic):
	if len(fdic[f]) > 1:
		print(f + ": " + " ".join(fdic[f]))

