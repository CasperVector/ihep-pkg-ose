%{eval arch}

Name:           npreal2
Version:        11.0
Release:        1.el%{rhel}
Summary:        Moxa Linux Real TTY Driver

License:        GPLv2
URL:            https://github.com/CasperVector/%{name}
Source0:        %{github_archive_ver CasperVector %{name} %{version} v}
Source1:        %{name}-services.patch

BuildRequires:  gcc, make
Requires:       gcc, make, kernel-devel
Requires(pre):  shadow-utils
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%prep
%autosetup
mv VERSION-%{_linux}.TXT VERSION.TXT
rm VERSION-*.TXT

%build
make %{?_smp_mflags} LINUX=%{_linux} \
	CFLAGS="%{optflags} -Wno-strict-aliasing -Wno-unused-result -Wno-error=format-security"

%install
make LINUX=%{_linux} DESTDIR=%{buildroot} install
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

