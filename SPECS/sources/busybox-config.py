#!/usr/bin/python3

import re
import sys

def conf_get(f):
	d = {}
	for l in f:
		l = l.strip()
		if l == "":
			continue
		elif l.startswith("#"):
			if l.endswith("is not set"):
				d[re.match(r"# (.*) is not set$", l).group(1)] = None
		else:
			l = l.split("=", 1)
			d[l[0]] = l[1]
	return d

def conf_merge(d, d1):
	for k, v1 in d1.items():
		if d.get(k) == None:
			d[k] = v1

def main(argv):
	d = {}
	for f in argv:
		conf_merge(d, conf_get(open(f)))
	for k, v in [
		("PIE", None), ("SSL_CLIENT", "y"), ("EXTRA_COMPAT", "n")
	]:
		d["CONFIG_%s" % k] = v
	for k in sorted(d):
		v = d[k]
		if v == None:
			print("# %s is not set" % k)
		else:
			print("%s=%s" % (k, v))

if __name__ == "__main__":
	main(sys.argv[1:])

