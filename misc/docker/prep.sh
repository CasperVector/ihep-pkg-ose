#!/bin/sh -xe

mirror='https://mirrors.nju.edu.cn'
ver="$(sed -n 's/^VERSION_ID=//p' /etc/os-release | tr -d \" | sed 's/\..*//')"
chmod 0644 /etc/yum.repos.d/ihep.repo /etc/pip.conf; chmod 0755 /init.sh
case "$ver" in
7)
	py3rel=6
	(cd /etc/yum.repos.d; rm CentOS-Sources.repo CentOS-Media.repo;
	sed -i '/^\[updates\]/,/^\[centosplus\]/ s/^gpgcheck=1/&\nenabled=0/' \
		CentOS-Base.repo;
	#sed -i '/^\[base\]/,/^$/ s@^#baseurl=.*@baseurl=http://172\.17\.0\.1/centos7@' \
	#	CentOS-Base.repo;
	sed -i -e 's/^#baseurl=/baseurl=/' -e 's/^mirrorlist=/#&/' \
		-e "s@http://mirror\\.centos\\.org/centos/\\\$releasever/@$mirror/centos-vault/7.9.2009/@" \
		-e "s@http://vault\\.centos\\.org/@$mirror/centos-vault/@" \
		CentOS-*.repo)
	yum install -y python3
	yum reinstall -y hostname;;
8)
	py3rel=9
	(cd /etc/yum.repos.d; rm Rocky-Sources.repo Rocky-Media.repo;
	#sed -ri 's@^#baseurl=.*\$releasever/([^/]+)/.*@baseurl=http://172\.17\.0\.1/rocky8/\1@' \
	#	Rocky-BaseOS.repo Rocky-AppStream.repo;
	sed -i -e "s@http://dl.rockylinux.org/\\\$contentdir/@$mirror/rocky/@" \
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
	sed -i "s@http://vault\\.centos\\.org/@$mirror/centos-vault/@" \
		/etc/yum.repos.d/CentOS-rt.repo
fi
ln -s /etc/pip.conf /usr/lib64/python3."$py3rel"/distutils/distutils.cfg
yum autoremove -y; yum clean all
rm -rf /var/cache/* /prep.patch /prep.sh

