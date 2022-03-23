#!/bin/sh -e

ddir=misc/docker
pdir=/home/builder/ihep-pkg-ose
istem=ihep-pkg-ose."$(id -nu)"
arch="$(arch)"

build="docker build $dockerargs"
run="docker run $dockerargs --volume=$PWD:$pdir:ro"
run="$run --volume=$PWD/pypi:$pdir/pypi"
run="$run --volume=$PWD/RPMS:$pdir/RPMS"
run="$run --volume=$PWD/SOURCES:$pdir/SOURCES"

set -x
[ "$#" -gt 0 ]; image="$1"; shift
mkdir -p pypi RPMS SOURCES; [ -t 0 ] && it=-it
[ "$#" -gt 0 ] && exec $run --rm $it "$istem.$image" "$@"

case "$image" in
base)
	$build -t "$istem.$image" --build-arg uid="$(id -u)" "$ddir";;
*)
	pkgs="$(cat "$ddir"/pkgs."$image")"
	rm -rf RPMS/"$arch"/link "$ddir"/RPMS
	$run --rm $it "$istem".base pkg_link $pkgs
	mkdir "$ddir"/RPMS
	cp "$ddir"/pkgs."$image" "$ddir"/RPMS/pkgs
	mv RPMS/"$arch"/link "$ddir"/RPMS/"$arch"
	$build -t "$istem.$image" -f "$ddir"/Dockerfile.pkgs \
		--build-arg parent="$istem".base "$ddir"
	rm -rf "$ddir"/RPMS;;
esac

