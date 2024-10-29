#!/bin/sh -xe

pkgs='autosave ipac seq calc iocStats asyn busy sscan motor'
ads='ADSupport ADCore'
make="make -j$(nproc)"
support="$PWD"
mingw="$(cd $(dirname $(which gcc))/..; pwd)"
if grep -q 'command too long' "$mingw"/bin/bash.exe; then
	w64devkit=true
else
	w64devkit=false
fi
if [ -w /etc/profile ]; then
	profile=/etc/profile
else
	profile="$HOME"/.profile
fi

if ! grep -q EPICS "$profile"; then
	if [ "$(uname -m)" = x86_64 ]; then
		build_alias="$(uname -m)-pc-mingw64"
		EPICS_HOST_ARCH=windows-x64-mingw
	else
		build_alias="$(uname -m)-pc-mingw32"
		EPICS_HOST_ARCH=win32-x86-mingw
	fi
	if "$w64devkit"; then cat << EOF >> "$profile"
export ac_executable_extensions=.exe
export build_alias=$build_alias
EOF
	fi
	cat << EOF >> "$profile"
export PATH_SEPARATOR=';'
export EPICS_BASE=$PWD/base
export EPICS_HOST_ARCH=$EPICS_HOST_ARCH
export PATH="\$PATH;\$EPICS_BASE/bin/\$EPICS_HOST_ARCH"
export EPICS_CA_ADDR_LIST=127.255.255.255
export EPICS_CA_AUTO_ADDR_LIST=NO

case "\$PATH" in
	*$mingw/bin*) :;;
	*) PATH="$mingw/bin;\$PATH";;
esac
EOF
fi
. "$profile"

norm_release() {
	(cd "$support"; make release MOD_="$OLDPWD/$1" MODULE_LIST=MOD_)
}
sed "s,@epics_root@,$support,g; s,@etop_base@,$EPICS_BASE,g" \
	< utils/support.release > configure/RELEASE
if ! which re2c; then ./mingw-libbuild re2c; fi
if [ -d pcre ] && ! which pcregrep; then
	sed -i 's/\tln -sf/\t@echo ln -sf/g' pcre/Makefile.*
	./mingw-libbuild pcre
fi
cd base; $make; cd ..
$make MODULE_LIST=
for name in $pkgs areaDetector; do norm_release "$name"; done
cd areaDetector; for name in $ads; do norm_release "$name"; done
cd ..; for name in $pkgs; do $make -C "$name"; done
cd areaDetector; for name in $ads; do $make -C "$name"; done

