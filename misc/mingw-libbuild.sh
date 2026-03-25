#!/bin/sh -xe

w64devkit="$(cd $(dirname $(which gcc))/..; pwd)"
if [ "$platform" = msvc ]; then
	echo 'MSVC unsupported by this script'
	exit 1
elif ! [ -f "$w64devkit"/bin/bash.exe ]; then
	echo 'On Linux, use your package manager instead of this script'
	exit 1
fi
if ! grep -q 'command too long' "$w64devkit"/bin/bash.exe; then
	echo 'MinGW build only supported with w64devkit'
	exit 1
fi
if [ "$(uname -m)" = x86_64 ]; then
	archdir="$w64devkit"/x86_64-w64-mingw32
else
	archdir="$w64devkit"/i686-w64-mingw32
fi
if [ -n "$w64devkit" ]; then
	confargs="--prefix=$w64devkit --bindir=$w64devkit/bin"
	confargs="$confargs --libdir=$archdir/lib --includedir=$archdir/include"
fi

for lib in "$@"; do cd "$lib"
	if [ -n "$w64devkit" ]; then
		# <https://github.com/skeeto/w64devkit/issues/50>
		sed -i \
			's/func_convert_file_msys_to_w32/func_convert_file_noop/' configure
		if [ -f ltmain.sh ]; then sed -i 's@=\.\./bin@=../../bin@' ltmain.sh; fi
	fi
	./configure $confargs
	make -j$(nproc); make install
cd -; done

