%define repo ca-gateway
%{meta license=EPICS version=2.1.3,3}

Name:           epics-cagateway
Summary:        EPICS - Channel Access PV Gateway
URL:            https://epics.anl.gov/extensions/gateway/index.php
Source0:        %{github_archive_ver epics-extensions %{repo} %{version} v}
Patch0:         %{name}-2.1.2-killer.patch
BuildRequires:  epics-base, epics-pcas, gcc-c++, make, perl
Requires:       epics-base, epics-pcas

%description

%prep
%autosetup -p 1 -n %{repo}-%{version}

%build

%install
. %{_specdir}/fn-build.sh
sed -i '/EPICS_BASE=/ { s/^#//; s@=.*@=%{etop_base}@ }' configure/RELEASE
make %{?_smp_mflags} %{cmd_flags} DESTDIR=%{buildroot} \
	INSTALL_LOCATION=%{buildroot}%{etop_base} install
rm -rf %{buildroot}%{etop_base}/configure
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst

