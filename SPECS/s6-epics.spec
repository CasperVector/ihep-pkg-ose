Name:           s6-epics
Version:        0.0.3
Release:        1.el%{rhel}
Summary:        Managing EPICS IOCs with s6

License:        CC0
URL:            https://codeberg.org/CasperVector/%{name}
Source0:        %{codeberg_archive CasperVector %{name} v%{version}}

AutoReqProv:    0
BuildRequires:  gcc, make, s6
Requires:       s6, socat

%description

%prep
%autosetup -n %{name}
sed -i 's@/usr/lib\>@%{_libdir}@' bin/Makefile

%build

%install
DESTDIR=%{buildroot} ./install.sh

%files
/var/s6-epics
/usr/share/s6-epics
%{_bindir}/*
%{_prefix}/lib/systemd/system/*.service

