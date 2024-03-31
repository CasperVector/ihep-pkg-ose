#!/bin/sh -xe

rpms="$(cat /home/builder/RPMS/rpms)"
pypis="$(cat /home/builder/RPMS/pypis)"
chmod 0755 /home/builder/RPMS/dir2pi.py
mv /home/builder/RPMS/pypi /home/builder
if [ -n "$rpms" ]; then
	createrepo /home/builder/RPMS/"$(arch)"
	yum install -y --enablerepo=ihep $rpms
fi
if [ -n "$pypis" ]; then
	/home/builder/RPMS/dir2pi.py /home/builder/pypi
	pip3 install -U pip
	pip3 install -U setuptools
	pip3 install $pypis
fi
yum clean --enablerepo=ihep all
rm -rf /var/cache/* /root/.cache /home/builder/RPMS /home/builder/pypi /prep.sh

