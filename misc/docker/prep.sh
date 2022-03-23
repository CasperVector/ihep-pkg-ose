#!/bin/sh -xe

chmod 0644 /etc/yum.repos.d/ihep.repo; chmod 0755 /init.sh
rm /etc/yum.repos.d/CentOS-Sources.repo
sed -i -e '/^\[updates\]/,/^\[centosplus\]/ s/^gpgcheck=1/&\nenabled=0/' \
	-e '/^\[base\]/,/^$/ s@http://mirror\.centos\.org/@https://mirrors.dotsrc.org/@' \
	-e 's/^#baseurl=/baseurl=/' -e 's/^mirrorlist=/#&/' \
	/etc/yum.repos.d/CentOS-Base.repo
yum install -y sudo rpm-build createrepo less
sed -i '/^%wheel/ s/$/\nbuilder\tALL=(ALL)\tNOPASSWD: ALL/' /etc/sudoers
useradd -u "$1" builder; yum clean all; rm -rf /var/cache/* /prep.sh

