#!/bin/sh -e

ver="$(basename "$0" | sed -r 's/.*[^0-9]([0-9]+)\.sh$/\1/')"
ddir=misc/docker
pdir=/home/builder/ihep-pkg-ose
istem="ihep-pkg-ose.$(id -nu).$ver"
arch="$(arch)"
pypi=pypi"$ver"
rpms=RPMS"$ver"
drpms="$ddir"/RPMS

build="docker build $dockerargs"
run="docker run $dockerargs --volume=$PWD:$pdir:ro"
run="$run --volume=$PWD/$pypi:$pdir/$pypi"
run="$run --volume=$PWD/$rpms:$pdir/$rpms"
run="$run --volume=$PWD/SOURCES:$pdir/SOURCES"

set -x
[ "$#" -gt 0 ]; image="$1"; shift
mkdir -p "$pypi" "$rpms" SOURCES; [ -t 0 ] && it=-it
[ "$#" -gt 0 ] && exec $run --rm $it "$istem.$image" "$@"

case "$image" in
base)
	parent="$(cat "$ddir"/parent"$ver")"
	$build -t "$istem.$image" --build-arg parent="$parent" \
		--build-arg ver="$ver" --build-arg uid="$(id -u)" "$ddir";;
*)
	pkgs="$(cat "$ddir"/rpms."$image")"
	pypis="$(cat "$ddir"/pypis."$image")"
	rm -rf "$rpms/rpms" "$rpms/pypi" "$drpms"; mkdir "$drpms"
	$run --rm $it "$istem".base rpm_link $pkgs';' pypi_link $pypis
	cp "$ddir"/rpms."$image" "$drpms"/rpms
	cp "$ddir"/pypis."$image" "$drpms"/pypis
	cp misc/dir2pi.py "$drpms"
	mv "$rpms/rpms" "$drpms/$arch"
	mv "$rpms/pypi" "$drpms"/pypi
	$build -t "$istem.$image" -f "$ddir"/Dockerfile.pkgs \
		--build-arg parent="$istem".base "$ddir"
	rm -rf "$drpms";;
esac

