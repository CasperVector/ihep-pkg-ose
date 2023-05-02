%define repo pcas
%define __arch_install_post true
%{meta name license=EPICS version=4.13.3,4}

Summary:        EPICS - Portable Channel Access Server
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive_ver epics-modules %{repo} %{version} v}
BuildRequires:  epics-base, gcc-c++, make, perl
Requires:       epics-base

%{inherit epics + global}
%description

%prep
%autosetup -n %{repo}-%{version}

%build

%install
. %{_specdir}/fn-build.sh
sed -i '/^EPICS_BASE =/ s@=.*@= %{etop_base}@' configure/RELEASE
make %{?_smp_mflags} %{cmd_flags} DESTDIR=%{buildroot} \
	INSTALL_LOCATION=%{buildroot}%{etop_base} install
rm -rf %{buildroot}%{etop_base}/configure
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst

