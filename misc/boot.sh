#!/bin/sh -e

pkgs_pre=''
pkgs_epics="$(xargs < misc/epics-boot.txt | tr ' ' '\n' | sed 's/^/epics-/')"
pkgs_post='npreal2'
pkgs_boot="$pkgs_pre $pkgs_epics $pkgs_post"
pkgs_epel='kernel-rt kernel-rt-devel docker-ce re2c hidapi-devel'
pkgs_epel="$pkgs_epel xspress3-autocalib procServ"
pkgs_pypi='bluesky ophyd databroker pyepics h5py hdf5plugin ipython matplotlib'
pkgs_pypi="$pkgs_pypi PyQt5 pyqtgraph pyzmq suitcase-csv suitcase-json_metadata"
pkgs_pip='pip setuptools setuptools-scm wheel build'
pkgs_pyfetch=''
pkgs_nobinary='ipython suitcase-utils'
pipdl_args="--no-binary $(echo "$pkgs_nobinary" | tr ' ' ',')"

mirror='https://mirrors.dotsrc.org'
pubkey_epel='RPM-GPG-KEY-EPEL-7'
mirror_docker='https://download.docker.com/linux/centos'
pubkey_docker='RPM-GPG-KEY-Docker'
mirror_qd='https://quantumdetectors.com/rpm/el7'
pubkey_qd='RPM-GPG-KEY-qd'
rpm_root=RPMS/"$(arch)"

inst() {
	sudo install -o root -g root -m 0644 "$@"
}

yyum() {
	sudo yum install -y "$@"
}

repo_mk() {
	rm -rf "$rpm_root"/repodata; createrepo "$rpm_root"
	sudo yum clean --disablerepo='*' --enablerepo=ihep expire-cache
}

# Hacky, but `--recursive' seems to `--resolve' only once.

pkg_url() {
	repoquery --tree-requires --qf='%{name}@%{repoid}' "$@" |
		sed 's/ *\[.*//; s/.* //; s/@/ /' | awk '$2 != "base" { print $1 }' |
		sort -u | xargs repoquery --location
}

pkg_link() {
	repoquery --enablerepo=ihep --tree-requires \
		--qf='%{nvra}.rpm@%{repoid}' "$@" |
		sed 's/ *\[.*//; s/.* //; s/@/ /' | awk '$2 == "ihep" { print $1 }' |
		sort -u | (mkdir "$rpm_root"/link; cd "$rpm_root"; xargs -r ln -t link)
}

rm_bad() {
	cat "$@" | (cd SOURCES;
		sha512sum -c 2> /dev/null | grep FAILED | xargs rm -vf)
}

src_prune() {
	(cd SOURCES; mkdir .keep; find . -type l -exec mv -t .keep '{}' '+';
	(cd ../misc; awk '{ print $2 }' SHA512SUMS \
		SHA512SUMS-pyfetch SHA512SUMS-iso) | xargs mv -t .keep || true;
	ls | xargs rm -vf; cd .keep; ls | xargs mv -t ..; cd -; rmdir .keep)
}

# `wget -c' on CentOS 7 works badly with GitHub/GitLab/Gitea archives.

iso_get() {
	yyum wget; rm_bad misc/SHA512SUMS-iso
	wget -nc -P SOURCES \
		"$mirror"/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso
	(cd SOURCES; sha512sum -c) < misc/SHA512SUMS-iso
}

src_get() {
	local f; yyum wget rpmdevtools; rm_bad misc/SHA512SUMS
	if [ "$#" -gt 0 ]; then
		for f in "$@"; do spectool SPECS/"$f".spec; done |
			awk '/:\/\// { print $2 }' | sort -u > /tmp/fetch.txt
		./misc/fetch.sh /tmp/fetch.txt
		return; fi
	wget -nc -P SOURCES "$mirror_docker"/docker-ce.repo \
		"$mirror_qd"/qd.repo "$mirror_qd/$pubkey_qd"
	[ -f SOURCES/"$pubkey_docker" ] ||
		wget -O SOURCES/"$pubkey_docker" "$mirror_docker"/gpg
	for f in SPECS/*.spec; do spectool "$f"; done |
		awk '/:\/\// { print $2 }' | sort -u > /tmp/fetch.txt
	./misc/fetch.sh /tmp/fetch.txt
	(cd SOURCES; sha512sum -c) < misc/SHA512SUMS
}

epel_prep() {
	inst misc/CentOS-rt.repo /etc/yum.repos.d
	sudo sed -i -e "s@http://mirror\\.centos\\.org/centos/@$mirror/centos/@" \
		-e "s@http://vault\\.centos\\.org/@$mirror/centos-vault/@" \
		/etc/yum.repos.d/CentOS-*.repo
	sudo sed -i -e '/^\[extras\]/,/^$/ s/^enabled=0/enabled=1/' \
		/etc/yum.repos.d/CentOS-Base.repo
	yyum wget epel-release
	sudo sed -i -e '/baseurl/ s/^#//' -e '/^metalink/ s/^/#/' \
		-e "s@http://download\\.fedoraproject\\.org/pub/epel/@$mirror/epel/@" \
		/etc/yum.repos.d/epel.repo
	inst SOURCES/docker-ce.repo SOURCES/qd.repo /etc/yum.repos.d
	inst SOURCES/"$pubkey_docker" SOURCES/"$pubkey_qd" /etc/pki/rpm-gpg
	(cd /etc/pki/rpm-gpg;
		sudo rpm --import "$pubkey_epel" "$pubkey_docker" "$pubkey_qd")
	sudo yum repolist
}

epel_get() {
	epel_prep; rm -rf "$rpm_root"/epel; mkdir -p "$rpm_root"/epel
	pkg_url $pkgs_epel | xargs wget -nc -P "$rpm_root"/epel
	rpm -K "$rpm_root"/epel/*; repo_mk
}

rpm_prune() {
	rpmspec --define "_topdir $PWD" -q --qf='%{nvra}.rpm\n' SPECS/*.spec |
	(cd "$rpm_root"; mkdir .keep; xargs mv -t .keep || true
	rm -f *.rpm; mv .keep/* .; rmdir .keep); repo_mk
}

build() {
	while [ "$#" -ge 1 ]; do
		sudo yum-builddep -y --enablerepo=ihep \
			--define "_topdir $PWD" SPECS/"$1".spec
		(set +x; . /etc/profile; set -x;
		rpmbuild -bb --clean --define "_topdir $PWD" SPECS/"$1".spec)
	shift; done; repo_mk
}

pypi_prune() {
	(cd pypi; mv orig/* . || true; rm -rf orig simple; mkdir .keep;
	awk '{ print $2 }' < ../misc/SHA512SUMS-pypi | xargs mv -t .keep || true;
	ls | xargs rm -vf; cd .keep; ls | xargs mv -t ..; cd -; rmdir .keep)
}

pypi_get() {
	local f; yyum wget
	if [ "$#" -gt 0 ]; then
		for f in "$@"; do ./misc/pybuild.sh "$f" 'echo $src' 2> /dev/null;
			done | grep '://' | sort -u > /tmp/fetch.txt
		./misc/fetch.sh /tmp/fetch.txt
		return; fi
	yyum python3-pip; sudo pip3 install -U pip
	for f in $pkgs_pyfetch; do ./misc/pybuild.sh "$f" 'echo $src' 2> /dev/null;
		done | grep '://' | sort -u > /tmp/fetch.txt
	./misc/fetch.sh /tmp/fetch.txt
	(cd SOURCES; sha512sum -c) < misc/SHA512SUMS-pyfetch
	#(cd pypi; pip3 download $pipdl_args $pkgs_pypi $pkgs_pip)
	awk '{ print $2 }' < misc/SHA512SUMS-pypi |
		sed -r 's/-([0-9][^-]+).*/==\1/; s/(\.zip|\.tar.[^.]+)$//' |
		(cd pypi; xargs pip3 download --no-deps $pipdl_args)
	(cd pypi; sha512sum -c) < misc/SHA512SUMS-pypi
	./misc/dir2pi.py pypi
}

pypi_prep() {
	yyum python3-pip
	inst misc/pip.conf /etc
	(cd /usr/lib64/python3.*/distutils;
		sudo ln -s /etc/pip.conf distutils.cfg)
	sudo pip3 install ./pypi/pip-[0-9]*.whl
	sudo pip3 install -U setuptools
	sudo pip3 install build wheel
	mkdir -p pypi/orig BUILD
}

pybuild() {
	while [ "$#" -ge 1 ]; do
		./misc/pybuild.sh "$1" do_build
	shift; done; ./misc/dir2pi.py pypi
}

build_pypi() {
	pypi_prep; pybuild $pkgs_pyfetch $pkgs_nobinary
}

set -x
eval "$@"

