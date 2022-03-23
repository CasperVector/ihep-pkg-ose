#!/bin/sh -xe

[ -d ihep-pkg-ose ] || exec sh -i
ln -s ihep-pkg-ose/* .; ln -s SPECS/rpmmacros .rpmmacros
(cd SOURCES; find ../SPECS/sources -type f -exec ln -snf -t . '{}' '+')
if ! ./misc/boot.sh "$@"; then
	[ -t 0 ] || exit 1
	echo 'Command failed, rescue shell enabled:'
	exec sh -i
fi
find ihep-pkg-ose/SOURCES -type l -delete

