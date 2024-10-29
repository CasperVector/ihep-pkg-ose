#!/bin/sh -xe

mingw="$(cd $(dirname $(which gcc))/..; pwd)"
if grep -q 'command too long' "$mingw"/bin/bash.exe; then
	w64devkit=true
else
	w64devkit=false
fi
if ! "$w64devkit"; then
	archdir=
elif [ "$(uname -m)" = x86_64 ]; then
	archdir="$mingw"/x86_64-w64-mingw32
else
	archdir="$mingw"/i686-w64-mingw32
fi
confargs="--prefix=$mingw --bindir=$mingw/bin"
if [ -n "$archdir" ]; then
	confargs="$confargs --libdir=$archdir/lib --includedir=$archdir/include"; fi

for lib in "$@"; do cd "$lib"
	if "$w64devkit"; then
		# <https://github.com/skeeto/w64devkit/issues/50>
		sed -i \
			's/func_convert_file_msys_to_w32/func_convert_file_noop/' configure
		if [ -f ltmain.sh ]; then sed -i 's@=\.\./bin@=../../bin@' ltmain.sh; fi
	fi
	./configure $confargs
	make -j$(nproc); make install
cd -; done

