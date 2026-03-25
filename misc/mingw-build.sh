#!/bin/sh -xe

pkgs='autosave ipac seq calc iocStats asyn busy sscan motor'
ads='ADSupport ADCore'
make="make -j$(nproc)"
support="$PWD"
w64devkit="$(cd $(dirname $(which gcc))/..; pwd)"
if [ "$platform" = msvc ]; then
	true
elif [ -f "$w64devkit"/bin/bash.exe ]; then
	platform=mingw
else
	platform=linux
fi
if [ "$platform" = linux ]; then
	w64devkit=
elif ! grep -q 'command too long' "$w64devkit"/bin/bash.exe; then
	echo 'MinGW build only supported with w64devkit'
	exit 1
fi
if [ -w /etc/profile ]; then
	profile=/etc/profile
else
	profile="$HOME"/.profile
fi

if ! grep -q EPICS "$profile"; then
	if [ "$platform" = linux ]; then
		EPICS_HOST_ARCH=linux-"$(uname -m)"
	elif [ "$(uname -m)" = x86_64 ]; then
		build_alias="$(uname -m)-pc-mingw64"
		EPICS_HOST_ARCH=windows-x64
	else
		build_alias="$(uname -m)-pc-mingw32"
		EPICS_HOST_ARCH=win32-x86
	fi
	if [ "$platform" = mingw ]; then
		EPICS_HOST_ARCH="$EPICS_HOST_ARCH-mingw"
	fi
	if [ -n "$w64devkit" ]; then
		PATH_SEPARATOR=';'
	else
		PATH_SEPARATOR=':'
	fi
	if [ -n "$w64devkit" ]; then cat << EOF >> "$profile"
export ac_executable_extensions=.exe
export build_alias=$build_alias
EOF
	fi
	if [ "$PATH_SEPARATOR" != ':' ]; then cat << EOF >> "$profile"
export PATH_SEPARATOR=';'
EOF
	fi
	cat << EOF >> "$profile"
export EPICS_BASE=$PWD/base
export EPICS_HOST_ARCH=$EPICS_HOST_ARCH
export PATH="\$PATH$PATH_SEPARATOR\$EPICS_BASE/bin/\$EPICS_HOST_ARCH"
export EPICS_CA_ADDR_LIST=127.255.255.255
export EPICS_CA_AUTO_ADDR_LIST=NO
EOF
	if [ -n "$w64devkit" ]; then cat << EOF >> "$profile"
case "\$PATH" in
	*$w64devkit/bin*) :;;
	*) PATH="$w64devkit/bin$PATH_SEPARATOR\$PATH";;
esac
EOF
	fi
fi
. "$profile"

norm_release() {
	(cd "$support"; make release MOD_="$OLDPWD/$1" MODULE_LIST=MOD_)
}
if [ "$PATH_SEPARATOR" != ':' ]; then
	sed -i "/^sub relPaths/,/^}/ s/':'/'$PATH_SEPARATOR'/g" \
		base/src/tools/convertRelease.pl
fi
sed "s,@epics_root@,$support,g; s,@etop_base@,$EPICS_BASE,g" \
	< utils/support.release > configure/RELEASE
if [ "$platform" != linux ]; then
	if ! which re2c; then platform= ./mingw-libbuild.sh re2c; fi
	if [ -d pcre ] && ! which pcregrep; then
		sed -i 's/\tln -sf/\t@echo ln -sf/g' pcre/Makefile.*
		./mingw-libbuild pcre
	fi
fi
cd base; $make; cd ..
$make MODULE_LIST=
for name in $pkgs areaDetector; do norm_release "$name"; done
cd areaDetector; for name in $ads; do norm_release "$name"; done
cd ..; for name in $pkgs; do $make -C "$name"; done
cd areaDetector; for name in $ads; do $make -C "$name"; done

