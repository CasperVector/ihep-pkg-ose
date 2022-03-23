# CentOS 7.9.2009.
FROM centos@sha256:e4ca2ed0202e76be184e75fb26d14bf974193579039d5573fb2348664deef76e
ARG uid=1000
ADD init.sh prep.sh /
ADD ihep.repo /etc/yum.repos.d
RUN chmod 0755 /prep.sh && /prep.sh "$uid"
USER builder
WORKDIR /home/builder
ENTRYPOINT ["/init.sh"]

