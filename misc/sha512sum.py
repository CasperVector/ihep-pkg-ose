#!/usr/bin/python3

import hashlib
import sys

sums = [l.strip().split("  ") for l in open(sys.argv[1])]
files, sums = [], dict((k, v) for v, k in sums)
for f in sys.argv[2:]:
    files.append(f.split("/")[-1])
    sums[files[-1]] = hashlib.sha512(open(f, "rb").read()).hexdigest()
open(sys.argv[1], "w").write("".join("%s  %s\n" % (v, k)
    for k, v in sorted(sums.items(), key = lambda kv: (kv[0].lower(), kv[0]))))
sys.stdout.write("".join("%s  %s\n" % (sums[f], f) for f in files))

