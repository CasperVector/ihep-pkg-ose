#!/bin/sh -xe

# Download the re2c tarball from <https://github.com/skvadrik/re2c/releases/>,
# put it in SOURCES and run this script.  The content generated in $PWD/mingw
# is suitable for use on Windows and non RHEL-7/8 Linux after native build
# with mingw-build.sh; see misc/SHA512SUMS/mingw for the recommended environment
# on Windows.
#
# Prerequisities on RHEL (& Rocky, CentOS, ...) 9:
#   # yum install --enablerepo=extras epel-release
#   # yum install --enablerepo=crb gcc-c++ make perl re2c \
#       rpcgen readline-devel libtirpc-devel libXext-devel
#   $ sed -i 's/\.profile/.bash_profile/' mingw-build.sh
#   $ sed -i '/TIRPC=YES/ s/^# *//' asyn/configure/CONFIG_SITE
# Prerequisites on Debian >= 12 and Ubuntu >= 22.04:
#   # apt-get install build-essential re2c rpcsvc-proto \
#       libreadline-dev libtirpc-dev libxext-dev
#   $ sed -i '/TIRPC=YES/ s/^# *//' asyn/configure/CONFIG_SITE
# Prerequisites on Debian <= 11 and Ubuntu <= 20.04:
#   # apt-get install build-essential re2c libreadline-dev libxext-dev

root="$PWD"
patches="$root/SPECS/sources"
pkgs='autosave ipac seq calc iocStats asyn busy sscan motor'
ads='ADSupport ADCore'

expand_rename() {
	local fname="$1"
	if [ "$fname" = seq ]; then fname=sequencer-mirror; fi
	tar xpf "$root/SOURCES/$fname"-*.tar.*
	mv "$fname"-* "$1"
}
norm_release() {
	(cd /opt/epics; make release MOD_="$OLDPWD/$1" MODULE_LIST=MOD_)
}
add_patch() {
	(cd "$1"; cat "$patches"/epics-"$1"-*-"$2".patch | patch -p1)
}

mkdir mingw; cd mingw
expand_rename support; cd support; expand_rename re2c
cat "$patches"/epics-support-*.release | > configure/RELEASE \
	sed "s,@epics_root@,/opt/epics,g; s,@etop_base@,/opt/epics/base,g"
cp "$root"/misc/mingw-*.* .

for name in base $pkgs areaDetector; do
	expand_rename "$name"; [ "$name" = base ] || norm_release "$name"; done
rm asyn/configure/CONFIG_SITE.*
sed -i 's/(IOCNAME):/(IOCNAME)/g' iocStats/iocAdmin/Db/*
sed -i '/^IPAC=/ s/^/#!/' motor/configure/RELEASE
sed -i '/BUILD_IOCS/ s/=.*/= YES/' motor/configure/CONFIG_SITE
sed -i '/^INSTALL_LOCATION =/ s/^/#/' \
	motor/configure/CONFIG motor/modules/CONFIG_SITE.local
cat "$patches"/epics-support-*-mingw.patch | patch -p1
add_patch base cas_tcp_port
add_patch base client_313
add_patch base msvc
add_patch ipac config
add_patch calc config
add_patch iocStats files
add_patch iocStats mingw
add_patch asyn bugs-files
add_patch asyn centos7
add_patch busy config
add_patch sscan bugs
add_patch motor bugs
add_patch motor asyneres

rmdir motor/modules/motor*/ areaDetector/*/ || true; cd areaDetector
for name in $ads; do expand_rename "$name"; done
for name in configure/EXAMPLE_*.local ADCore/iocBoot/EXAMPLE_*
	do mv "$name" "$(echo "$name" | sed 's/\<EXAMPLE_//')"; done
for name in $ads; do norm_release "$name"; done
cat "$patches"/epics-ADSupport-*-config.patch | patch -p1
add_patch ADSupport mingw
add_patch ADCore bugs
cd ..; norm_release areaDetector
find . -name '*.orig' -delete

