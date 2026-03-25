#!/bin/sh -xe

# iocs/*IOC/iocBoot/ioc*/Makefile usually also need tuning on a
# per-module basis to set ${ARCH} correctly.
for mod in "$@"; do cd "$mod"
	case "$(basename "$mod")" in motor*) for d in iocs/*IOC; do
		(cd "$d"/configure; grep -q '^MOTOR_' RELEASE ||
		sed -n '/#!MOTOR_/ { s/^#!//; s@=.*@=$(TOP)/../..@; p }' \
			EXAMPLE_RELEASE.local >> RELEASE)
	done;; esac
	case "$EPICS_HOST_ARCH" in win*) for d in iocs/*IOC/iocBoot/ioc*; do
		case "$EPICS_HOST_ARCH" in
		*-mingw)
			(cd "$d"; grep -q relPaths Makefile ||
			sed -i '/TARGETS *=/ s/$/ relPaths.sh/' Makefile);;
		*)
			(cd "$d"; grep -q dllPath Makefile ||
			sed -i '/TARGETS *=/ s/$/ dllPath.bat/' Makefile);;
		esac
	done;; esac
	make -j"$(nproc)"
cd -; done

