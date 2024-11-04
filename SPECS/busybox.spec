%define acommit 3.16.1

Name:           busybox
Version:        1.35.0
Release:        1.%(echo %{acommit} | tr '.' '_').el%{rhel}
Summary:        Swiss Army Knife of Embedded Linux

License:        GPLv2
URL:            https://busybox.net/
Source0:        https://busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1:        %{github_archive_ver alpinelinux aports %{acommit} v}
Source2:        busybox-config.py
Source3:        index_cgi-20200731.patch

BuildRequires:  gcc, make, perl, kernel-headers

%description

%prep
%autosetup
tar xpf %{S:1}; mv aports-*/main/busybox cfg
cd cfg; %{S:2} busyboxconfig busyboxconfig-extras > ../.config
rm 0001-avoid-redefined-warnings-when-building-with-utmps.patch
cd -; cat cfg/*.patch | patch -p1
cd networking; patch -p0 < %{S:3}; cd -

%build
yes '' | make oldconfig; make %{?_smp_mflags}
cd networking; gcc -Wall -O2 -mtune=generic \
	-funsigned-char httpd_indexcgi.c -o index.cgi; cd -

%install
mkdir -p %{buildroot}%{_bindir}
cp busybox_unstripped %{buildroot}%{_bindir}/busybox
mkdir -p %{buildroot}%{_datadir}/%{name}
cp networking/index.cgi %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
cp docs/busybox.1 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/*/*

