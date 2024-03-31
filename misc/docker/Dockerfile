ARG parent
FROM "$parent"
ARG ver=8
ARG uid=1000
ADD init.sh prep.sh /
ADD prep"$ver".patch /prep.patch
ADD ihep.repo /etc/yum.repos.d
ADD pip.conf /etc
RUN chmod 0755 /prep.sh && /prep.sh "$uid"
USER builder
WORKDIR /home/builder
ENTRYPOINT ["/init.sh"]

