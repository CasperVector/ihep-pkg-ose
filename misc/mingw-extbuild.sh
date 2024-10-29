#!/bin/sh -xe

# configure/RELEASE usually also needs tuning on a per-module basis
# to set ${EPICS_BASE} correctly.
for ext in "$@"; do cd "$ext"
	rimg="$ext-image"; aimg="$EPICS_BASE/$rimg"
	make -j"$(nproc)" DESTDIR="$rimg" INSTALL_LOCATION="$aimg"/ install
	rm -rf "$aimg"/configure; cp -a "$aimg"/* "$EPICS_BASE"; rm -rf "$aimg"
cd -; done

