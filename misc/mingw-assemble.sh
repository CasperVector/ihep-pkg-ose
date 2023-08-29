#!/bin/sh -xe

root="$PWD"
patches="$root/SPECS/sources"
pkgs='autosave ipac seq calc iocStats asyn busy sscan motor'
ads='ADSupport ADCore'

expand_rename() {
	tar xpf "$root/SOURCES/$1"-*.tar.*
	mv "$1"-* "$(echo "$1" | sed -r 's/-R?[0-9].*//')";
}
norm_release() {
	(cd /opt/epics; make release MOD_="$OLDPWD/$1" MODULE_LIST=MOD_)
}
add_patch() {
	(cd "$1"; cat "$patches"/epics-"$1"-*-"$2".patch | patch -p1)
}

mkdir mingw; cd mingw
# <https://github.com/skvadrik/re2c/releases/download/3.0/re2c-3.0.tar.xz>
expand_rename support; cd support; expand_rename re2c
cp "$patches"/epics-support-*.release utils/support.release
sed "s,@epics_root@,/opt/epics,g; s,@etop_base@,/opt/epics/base,g" \
	< utils/support.release > configure/RELEASE
cp "$root"/misc/mingw-build.sh .

for name in base $pkgs areaDetector; do
	expand_rename "$name"; [ "$name" = base ] || norm_release "$name"; done
sed -i 's/(IOCNAME):/(IOCNAME)/g' iocStats/iocAdmin/Db/*
sed -i '/^IPAC=/ s/^/#!/' motor/configure/RELEASE
sed -i '/BUILD_IOCS/ s/=.*/= YES/' motor/configure/CONFIG_SITE
sed -i '/^INSTALL_LOCATION =/ s/^/#/' \
	motor/configure/CONFIG motor/modules/CONFIG_SITE.local
add_patch ipac config
add_patch calc config
add_patch iocStats files
add_patch iocStats mingw
add_patch asyn files
add_patch busy config
add_patch motor bugs

rmdir motor/modules/motor*/ areaDetector/AD*/; cd areaDetector
for name in $ads; do expand_rename "$name"; done
for name in configure/EXAMPLE_* ADCore/iocBoot/EXAMPLE_*
	do mv "$name" "$(echo "$name" | sed 's/\<EXAMPLE_//')"; done
for name in $ads; do norm_release "$name"; done
cat "$patches"/epics-ADSupport-*-config.patch | patch -p1
add_patch ADSupport mingw
add_patch ADCore bugs
cd ..; norm_release areaDetector

