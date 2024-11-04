%define skaver 2.13.1.1
%define execver 2.9.3.0

Name:           s6
Version:        2.11.3.2
Release:        2.el%{rhel}
Summary:        skarnet's small and secure supervision software suite

License:        ISC
URL:            https://skarnet.org/software/s6/
Source0:        https://skarnet.org/software/skalibs/skalibs-%{skaver}.tar.gz
Source1:        https://skarnet.org/software/execline/execline-%{execver}.tar.gz
Source2:        https://skarnet.org/software/s6/s6-%{version}.tar.gz
Patch0:         %{name}-files.patch

BuildRequires:  gcc, make

%description

%prep
%setup -T -c -n %{name}
. %{_specdir}/fn-build.sh
tar xpf %{S:0}; _mv_commit skalibs %{skaver}
tar xpf %{S:1}; _mv_commit execline %{execver}
tar xpf %{S:2}; _mv_commit s6 %{version}
patch -p1 < %{P:0}

%build
stat -c '%a' %{_bindir} > bin.mod; stat -c '%a' %{_libdir} > libdir.mod
sudo chmod 0755 %{_bindir} %{_libdir}
%_chown_me %{_bindir} %{_libexecdir} %{_libdir} %{_includedir}
confargs='--bindir=%{_bindir} --libexecdir=%{_libexecdir} --disable-shared'
confargs="$confargs --with-sysdep-devurandom=yes --with-sysdep-posixspawn=no"
for pkg in skalibs execline s6; do cd "$pkg"
	sed -i 's@/usr/lib\>@%{_libdir}@' configure
	./configure $confargs; make %{?_smp_mflags}
	mkdir image; make install; make DESTDIR="$PWD"/image install
cd -; done

%install
. %{_specdir}/fn-build.sh; mkdir rm
_mv_me "$PWD"/rm %{_bindir} %{_libexecdir} %{_libdir} %{_includedir}
sudo chmod "$(cat bin.mod)" %{_bindir}
sudo chmod "$(cat libdir.mod)" %{_libdir}
for pkg in skalibs execline s6; do
	cp -a "$pkg"/image/* %{buildroot}
done
cd %{buildroot}%{_bindir}; rm cd umask; mv wait execline-wait; cd -
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system \
	%{buildroot}/var/service/.s6-svscan
install -m 0644 *.service %{buildroot}%{_prefix}/lib/systemd/system
install -m 0755 crash SIGTERM %{buildroot}/var/service/.s6-svscan
%_file_list %{_bindir} %{_libexecdir} > files.lst

%files -f files.lst
%{_includedir}/skalibs
%{_includedir}/execline
%{_includedir}/s6
%{_libdir}/skalibs
%{_libdir}/execline
%{_libdir}/s6
%{_prefix}/lib/systemd/system/*.service
/var/service/.s6-svscan/*

