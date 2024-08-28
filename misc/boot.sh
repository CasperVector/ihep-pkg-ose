#!/bin/sh -e

ver="$(rpmspec -E '%{rhel}')"

vcat() {
	cd "$1"; cat "$2" "$2.$ver" | sed 's/#.*//'
}

# Hacky, but `--recursive' seems to `--resolve' only once at least on CentOS 7.

if [ "$ver" -eq 7 ]; then
py3rel=6
repoqlimit=''
repoqtree='--tree-requires'
else
py3rel=9
repoqlimit='--latest-limit=1'
repoqtree='--tree --requires'
fi

pkgs_pre="$(vcat misc/pkgs pre)"
pkgs_epics="$(vcat misc/pkgs epics | xargs |
	tr ' ' '\n' | sed 's/^/epics-/' | xargs)"
pkgs_post="$(vcat misc/pkgs post)"
pkgs_boot="$pkgs_pre $pkgs_epics $pkgs_post"
pkgs_epel="$(vcat misc/pkgs epel)"
pkgs_pip='pip setuptools setuptools-scm wheel build'
pkgs_pypi="$(vcat misc/pkgs pypi)"
pkgs_pyfetch="$(vcat misc/pkgs pyfetch)"
pkgs_nobinary="$(vcat misc/pkgs nobinary)"
pipdl_args="--no-binary $(echo $pkgs_nobinary | tr ' ' ',')"

mirror='https://mirrors.nju.edu.cn'
pubkey_epel="RPM-GPG-KEY-EPEL-$ver"
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

spec_expand() {
	rpmspec --define "_topdir $PWD" -P "$1" > /tmp/expanded.spec
}

repo_mk() {
	rm -rf "$rpm_root"/repodata; createrepo "$rpm_root"
	sudo yum clean --disablerepo='*' --enablerepo=ihep expire-cache
}

rpm_url() {
	repoquery $repoqlimit $repoqtree --qf='%{name}@%{repoid}' "$@" |
		sed 's/ *\[.*//; s/.* //; s/@/ /' |
		awk '$2 != "base" && $2 != "baseos" && $2 != "appstream" { print $1 }' |
		sort -u | xargs -r repoquery $repoqlimit --location
}

rpm_link() {
	if [ "$#" -eq 0 ]; then mkdir RPMS/rpms; return; fi
	repoquery $repoqlimit $repoqtree --enablerepo=ihep \
		--qf='%{name}-%{version}-%{release}.%{arch}.rpm@%{repoid}' "$@" |
		sed 's/ *\[.*//; s/.* //; s/@/ /' | awk '$2 == "ihep" { print $1 }' |
		sort -u | (mkdir RPMS/rpms; cd "$rpm_root"; xargs -r ln -t ../rpms)
}

chk_bad() {
	vcat misc/SHA512SUMS "$2" | (cd "$1"; sha512sum -c)
}

rm_bad() {
	vcat misc/SHA512SUMS "$2" | (cd "$1";
		sha512sum -c 2> /dev/null | grep FAILED | xargs rm -vf)
}

src_prune() {
	(cd SOURCES; mkdir .keep; find . -type l -exec mv -t .keep '{}' '+';
	(cd ../misc/SHA512SUMS; cat main* pyfetch* iso*) |
		awk '{ print $2 }' | xargs mv -t .keep || true;
	ls | xargs rm -vf; cd .keep; ls | xargs mv -t ..; cd -; rmdir .keep)
}

# `wget -c' works badly with GitHub/GitLab/Gitea archives.

iso_get() {
	yyum wget; rm_bad SOURCES iso
if [ "$ver" -eq 7 ]; then
	wget -nc -P SOURCES \
		"$mirror"/centos-vault/7.9.2009/isos/x86_64/CentOS-7-x86_64-Everything-2009.iso
else
	wget -nc -P SOURCES \
		"$mirror"/rocky/8.7/isos/x86_64/Rocky-8.7-x86_64-dvd1.iso
fi
	chk_bad SOURCES iso
}

src_get() {
	local f; yyum wget rpmdevtools; rm_bad SOURCES main
	if [ "$#" -gt 0 ]; then
		for f in "$@"; do
			spec_expand SPECS/"$f".spec; spectool /tmp/expanded.spec
		done | awk '/:\/\// { print $2 }' | sort -u > /tmp/fetch.txt
		./misc/fetch.sh /tmp/fetch.txt
		return; fi
	wget -nc -P SOURCES "$mirror_docker"/docker-ce.repo \
		"$mirror_qd"/qd.repo "$mirror_qd/$pubkey_qd"
	[ -f SOURCES/"$pubkey_docker" ] ||
		wget -O SOURCES/"$pubkey_docker" "$mirror_docker"/gpg
	for f in $pkgs_boot; do
		spec_expand SPECS/"$f".spec; spectool /tmp/expanded.spec
	done | awk '/:\/\// { print $2 }' | sort -u > /tmp/fetch.txt
	./misc/fetch.sh /tmp/fetch.txt; chk_bad SOURCES main
}

epel_prep() {
	(cd /etc/yum.repos.d;
if [ "$ver" -eq 7 ]; then
	sudo sed -i 's/^enabled=0/enabled=1/' CentOS-rt.repo
else
	sudo sed -i 's/^enabled=0/enabled=1/' Rocky-RT.repo Rocky-PowerTools.repo
fi
	)
	yyum --enablerepo=extras wget epel-release
	inst SOURCES/docker-ce.repo /etc/yum.repos.d
	inst SOURCES/"$pubkey_docker" /etc/pki/rpm-gpg
	(cd /etc/pki/rpm-gpg; sudo rpm --import "$pubkey_epel" "$pubkey_docker")
if [ "$ver" -eq 7 ]; then
	sudo sed -i -e '/baseurl/ s/^#//' -e '/^metalink/ s/^/#/' \
		-e "s@http://download\\.fedoraproject\\.org/pub/epel/@$mirror/epel/@" \
		/etc/yum.repos.d/epel.repo
	inst SOURCES/qd.repo /etc/yum.repos.d
	inst SOURCES/"$pubkey_qd" /etc/pki/rpm-gpg
	(cd /etc/pki/rpm-gpg; sudo rpm --import "$pubkey_qd")
else
	sudo sed -i -e '/baseurl/ s/^#//' -e '/^metalink/ s/^/#/' \
		-e "s@https://download\.example/pub/epel/@$mirror/epel/@" \
		/etc/yum.repos.d/epel.repo
fi
sudo yum repolist -v
}

epel_get() {
	if [ "$#" -gt 0 ]; then
		rpm_url "$@" | xargs wget -nc -P "$rpm_root"/epel
		rpm -K "$rpm_root"/epel/*; repo_mk
		return; fi
	epel_prep; rm -rf "$rpm_root"/epel; mkdir -p "$rpm_root"/epel
	rpm_url $pkgs_epel | xargs wget -nc -P "$rpm_root"/epel
	rpm -K "$rpm_root"/epel/*; repo_mk
}

rpm_prune() {
	echo $pkgs_boot | tr ' ' '\n' | sed 's@^@SPECS/@; s/$/.spec/' |
	xargs rpmspec --define "_topdir $PWD" -q --qf='%{nvra}.rpm\n' |
	(cd "$rpm_root"; mkdir .keep; xargs mv -t .keep || true;
	rm -f *.rpm; mv .keep/* .; rmdir .keep); repo_mk
}

build() {
	while [ "$#" -gt 0 ]; do
		spec_expand SPECS/"$1".spec
		sudo yum-builddep -y --enablerepo=ihep /tmp/expanded.spec
		(set +x; . /etc/profile; set -x;
		rpmbuild -bb --clean --define "_topdir $PWD" SPECS/"$1".spec)
	shift; done; repo_mk
}

pypi_toggle() {
	if [ -f /etc/pip.conf ]; then
		sudo rm /etc/pip.conf /usr/lib64/python3."$py3rel"/distutils/distutils.cfg
	else
		inst misc/docker/pip.conf /etc
		sudo ln -s /etc/pip.conf /usr/lib64/python3."$py3rel"/distutils/distutils.cfg
	fi
}

pypi_link() {
	if [ "$#" -eq 0 ]; then mkdir RPMS/pypi; return; fi
	mkdir RPMS/pypi; (cd RPMS/pypi; pip3 download pip setuptools "$@")
}

pypi_prune() {
	(cd pypi; mv orig/* . || true; rm -rf orig simple; mkdir .keep;
	vcat ../misc/SHA512SUMS pypi |
		awk '{ print $2 }' | xargs mv -t .keep || true;
	ls | xargs rm -vf; cd .keep; ls | xargs mv -t ..; cd -; rmdir .keep)
}

pypi_get() {
	local f; yyum wget
	if [ "$#" -gt 0 ]; then
		for f in "$@"; do ./misc/pybuild.sh "$f" 'echo $src' 2> /dev/null;
			done | grep '://' | sort -u > /tmp/fetch.txt
		./misc/fetch.sh /tmp/fetch.txt
		return; fi
	pypi_toggle; sudo pip3 install -U pip
	#(cd pypi; pip3 download $pipdl_args $pkgs_pypi $pkgs_pip)
	for f in $pkgs_pyfetch; do ./misc/pybuild.sh "$f" 'echo $src' 2> /dev/null;
		done | grep '://' | sort -u > /tmp/fetch.txt
	./misc/fetch.sh /tmp/fetch.txt; chk_bad SOURCES pyfetch
	vcat misc/SHA512SUMS pypi | awk '{ print $2 }' |
		sed -r 's/-([0-9][^-]+).*/==\1/; s/(\.zip|\.tar.[^.]+)$//' |
		(cd pypi; xargs pip3 download --no-deps $pipdl_args)
	chk_bad pypi pypi; ./misc/dir2pi.py pypi; pypi_toggle
}

pybuild() {
	mkdir -p pypi/orig BUILD
	while [ "$#" -gt 0 ]; do
		./misc/pybuild.sh "$1" do_build
	shift; done; ./misc/dir2pi.py pypi
}

set -x
eval "$@"

