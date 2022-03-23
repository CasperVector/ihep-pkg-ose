Name:           npreal2
Version:        10.1
Release:        2
Summary:        Moxa Linux Real TTY Driver

License:        GPLv2
URL:            https://github.com/CasperVector/%{name}
Source0:        %{github_archive_ver CasperVector %{name} %{version} v}
Source1:        %{name}-services.patch

BuildRequires:  gcc, make, kernel-devel
Requires:       gcc, make, kernel-devel
Requires(pre):  shadow-utils

%description

%prep
%autosetup

%build
make %{?_smp_mflags} KERNEL="$(ls -d /usr/src/kernels/* | sed 1q)" \
	CFLAGS="%{optflags} -Wno-strict-aliasing -Wno-unused-result"

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system
cd %{buildroot}%{_prefix}/lib/systemd/system; patch -p1 < %{S:1}

%files
%{_bindir}/*
/var/%{name}/module/*
%{_prefix}/lib/systemd/system/*.service
%config(noreplace) /etc/npreal2d.cf
%doc *.TXT

%pre
getent passwd npreal2 > /dev/null || useradd -r npreal2

%preun
if [ "$1" -eq 0 ]; then mxmkdrv clean || true; fi

