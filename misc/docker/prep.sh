#!/bin/sh -xe

mirror='https://mirrors.bangmod.cloud'
ver="$(sed -n 's/.*_PRODUCT_VERSION=//p' /etc/os-release |
	sed 1q | tr -cd 0-9. | sed 's/\..*//')"
chmod 0644 /etc/yum.repos.d/ihep.repo; chmod 0755 /init.sh
case "$ver" in
7)
	(cd /etc/yum.repos.d; rm CentOS-Sources.repo CentOS-Media.repo;
	sed -i '/^\[updates\]/,/^\[centosplus\]/ s/^gpgcheck=1/&\nenabled=0/' \
		CentOS-Base.repo;
	sed -i -e 's/^#baseurl=/baseurl=/' -e 's/^mirrorlist=/#&/' \
		-e "s@http://mirror\\.centos\\.org/centos/@$mirror/centos/@" \
		-e "s@http://vault\\.centos\\.org/@$mirror/centos/@" CentOS-*.repo)
	yum install -y python3
	yum reinstall -y hostname;;
8)
	(cd /etc/yum.repos.d; rm Rocky-Sources.repo Rocky-Media.repo;
	sed -i -e "s@http://dl.rockylinux.org/\\\$contentdir/@$mirror/rocky-linux/@" \
		-e 's/^#baseurl=/baseurl=/' -e 's/^mirrorlist=/#&/' Rocky-*.repo;
	sed -i '/^enabled=/ s/=1$/=0/' Rocky-Extras.repo)
	yum install -y perl python39
	alternatives --set python /usr/bin/python3
	alternatives --set python3 /usr/bin/python3.9;;
*)
	exit 1;;
esac
yum install -y sudo rpm-build yum-utils createrepo less
sed -i '/^%wheel/ s/$/\nbuilder\tALL=(ALL)\tNOPASSWD: ALL/' /etc/sudoers
useradd -u "$1" builder; patch -p0 < /prep.patch
if [ "$ver" -eq 7 ]; then
	sed -i "s@http://mirror\\.centos\\.org/centos/@$mirror/centos/@" \
		/etc/yum.repos.d/CentOS-rt.repo
fi
yum autoremove -y; yum clean all
rm -rf /var/cache/* /prep.patch /prep.sh

