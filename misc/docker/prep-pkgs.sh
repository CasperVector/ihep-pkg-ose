#!/bin/sh -xe

createrepo /home/builder/RPMS/"$(arch)"
yum install -y --enablerepo=ihep $(cat /home/builder/RPMS/pkgs)
yum clean --enablerepo=ihep all
rm -rf /var/cache/* /home/builder/RPMS /prep.sh

