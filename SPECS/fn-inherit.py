#!/usr/bin/python

import os
import os.path
import sys
clsDir = "SPECS/classes"
phases = ["global", "prep", "build", "install", "files"]

try:
	cls = sys.argv[1]
	mode = sys.argv[2] if len(sys.argv) > 2 else "-"
	assert mode in ["+", "-"]
	phases = sys.argv[3:] if mode == "+" else \
		[phase for phase in phases if phase not in sys.argv[3:]]
	specs = ["%s/%s.%s.spec" % (clsDir, cls, phase) for phase in phases]
	specs = [spec for spec in specs if os.path.exists(spec)]
	assert specs
	[sys.stdout.write(open(spec).read()) for spec in specs]
except:
	sys.stdout.write("%prep\n%prep\n")
	raise

