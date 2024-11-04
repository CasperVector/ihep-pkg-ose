#!/bin/sh -

_rm_extras() {
	find "$1" '(' -name '*.orig' -o '(' \
		-not '(' '(' -name '*Support' -o -name '*Sup' ')' -prune ')' \
	-name '*.a' ')' ')' -exec rm -f '{}' '+'
	find "$1" '(' -name O.Common -o -name 'O.linux-*' ')' -exec rm -rf '{}' '+'
}
_file_list() {
	(cd "$1"; shift;
		find $(echo "$@" | tr ' ' '\n' | sed 's@^/@@') -not -type d) |
	sed 's@^@"/@; s/$/"/'
}

_iocboot_makefiles() {
	local d
	cp "$1"/utils/iocBoot.mk "$2"/Makefile
	for d in "$2"/ioc*/; do cp "$1"/utils/ioc.mk "$d"/Makefile; done
}

_fix_perm() {
	find "$@" '(' -type d -o -type f -perm -0100 ')' -exec chmod 0755 '{}' ';'
	find "$@" -type f -not -perm -0100 -exec chmod 0644 '{}' ';'
}
_mv_commit() {
	local d="$(echo "$1" | tr A-Z a-z)"
	if [ -d "$d" ]; then
		[ "$d" == "$1" ] || mv "$d" "$1"
	else
		mv "$1"-"$2"* "$1"
	fi
	chmod -R go-w "$1"
}
_mv_build() {
	if [ -d "$2" ]; then sudo rmdir "$2"; fi
	sudo mv "$1" "$2"
}
_mv_dest() {
	mkdir -p "$2"; sudo mv "$1" "$2"; sudo mkdir "$1"
}
_mv_me() {
	local dest="$1" d; shift
	for d in "$@"; do
		mkdir -p "$dest$d"
		find "$d" -mindepth 1 -maxdepth 1 -not -user root \
			-exec mv -t "$dest$d" '{}' '+'
		sudo chown root:root "$d"
	done
}

_patch_cmd() {
	find "$1" '(' \
		-name '*.cmd' -o -name '*.cmd.*' -o -name '*.iocsh' -o -name '*.iocsh.*' \
	')' -exec sed -i '/^create_monitor_set/ s/^/#/' '{}' '+'
	grep -rl '^set_savefile_path' --exclude-dir autosave "$1" | xargs -r sed -i \
		'/^set_savefile_path/ s@".*"@"$(HOME)/iocBoot/autosave/$(IOC)"@'
}
_link_ops() {
	local ft
	for ft in adl bob edl opi ui; do
		mkdir -p "$1/$ft"
		find "$2" -type f -name '*.'"$ft" -not -user root \
			-exec ln -s '{}' "$1/$ft" ';'
	done
}
_fix_arch() {
	local arch; arch=$1; shift
	if [ "$#" -eq 1 -a ! -f "$1" ]; then return; fi
	sed -i "/^ARCH/ s/^/#/; /$arch\$/ s/^#ARCH/ARCH/" "$@"
}

_link_so() {
	while [ "$#" -gt 0 ]; do
		local dirname="$(dirname "$1")" basename="$(basename "$1")"
		local soname="$(objdump -p "$1" | awk '/SONAME/ { print $2 }')"
		local barename="$(echo "$basename" | sed 's/\.so\..*/.so/')"
		if [ -z "$soname" ]; then soname="$basename"; fi
		[ "$basename" = "$soname" ] || ln -s "$basename" "$dirname/$soname"
		[ "$soname" = "$barename" ] || ln -s "$soname" "$dirname/$barename"
	shift; done
}

