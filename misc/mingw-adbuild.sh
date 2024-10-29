#!/bin/sh -xe

# iocs/*IOC/iocBoot/ioc*/Makefile usually also need tuning on a
# per-module basis to set ${ARCH} correctly.
for mod in "$@"; do cd "$mod"
	case "$mod" in motor*) for d in iocs/*IOC; do
		(cd "$d"/configure; grep -q '^MOTOR_' RELEASE ||
		sed -n '/#!MOTOR_/ { s/^#!//; s@=.*@=$(TOP)/../..@; p }' \
			EXAMPLE_RELEASE.local >> RELEASE)
	done;; esac
	for d in iocs/*IOC/iocBoot/ioc*; do
		(cd "$d"; grep -q relPaths Makefile ||
		sed -i '/TARGETS *=/ s/$/ relPaths.sh/' Makefile)
	done
	make -j"$(nproc)"
cd -; done

