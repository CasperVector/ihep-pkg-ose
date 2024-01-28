#!/bin/sh -e

toppath="$PWD"
buildpath="$toppath"/BUILD
pybuild="$toppath"/misc/pybuild
sysver="$(rpmspec -E '%{rhel}')"

src_pypi() {
	local f g
	f="$(ls "$toppath/pypi/orig/$1"-[0-9]* 2> /dev/null || true)"
	if [ -f "$f" ]; then echo "$f"; return 0; fi
	f="$(ls "$toppath/pypi/$1"-[0-9]*)"
	g=pypi/orig/"$(basename "$f")"
	mv "$f" "$g"; echo "$g"
}

src_fetch() {
	ls "$toppath/SOURCES/$(basename "$1")" 2> /dev/null || echo "$1"
}

do_unpack() {
	local f; f="$(basename "$src")"
	case "$src" in
	*.tar.*)
		[ -n "$workdir" ] || workdir="${f%.tar.*}"
		tar -C "$buildpath" -xpf "$src";;
	*.zip)
		[ -n "$workdir" ] || workdir="${f%.zip}"
		(cd "$buildpath"; unzip -q "$src");;
	*.whl)
		[ -n "$workdir" ] || workdir="$pkg"
		mkdir "$buildpath/$workdir"
		(cd "$buildpath/$workdir"; unzip -q "$src");;
	*) exit 1;;
	esac
	workpath="$buildpath/$workdir"
}

do_prepare() {
	local f; for f in $patches; do
		patch -p1 < "$pybuild/$f"; done
}

do_compile() {
	python3 -m build --no-isolation --wheel
}

do_clean() {
	mv "$workpath"/dist/* pypi
	rm -rf "$workpath"
}

do_build() {
	do_unpack
	(cd "$workpath"; do_prepare; do_compile)
	do_clean
}

set -x
pkg="$1"; shift
. "$pybuild"/"$pkg".sh
eval "$@"

