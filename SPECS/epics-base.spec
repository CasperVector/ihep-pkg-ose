%define etop_dest %{buildroot}%{etop_base}
%define __arch_install_post true
%{meta license=EPICS version=7.0.6.1,3}

Name:           epics-base
Summary:        Experimental Physics and Industrial Control System - Base
URL:            https://epics.anl.gov/
Source0:        https://epics.anl.gov/download/base/base-%{version}.tar.gz
Source1:        epics-base.profile.sh
Patch0:         %{name}-7.0.3-rdeplib_dirs.patch
Patch1:         %{name}-7.0.6.1-cas_tcp_port.patch
Patch2:         %{name}-7.0.3.1-softIoc.patch
BuildRequires:  gcc-c++, make, perl, readline-devel
Requires:       perl, readline

%{inherit epics + global}
%description

%prep
%autosetup -p 1 -n base-%{version}
grep -rl 'RPATH_.*_DEPLIB_DIRS' . | xargs sed -i \
	'/RPATH_/ s/_DEPLIB_DIRS/_RDEPLIB_DIRS/'
grep -rl 'FINAL_LOCATION.*INSTALL_LOCATION' . | xargs sed -i \
	'/FINAL_LOCATION./ s@INSTALL_LOCATION@&:$(DESTDIR)/%=/%@'
sed -i '/_PERMISSIONS =/ { s/444/644/; s/555/755/ }' configure/CONFIG_COMMON

%build

%install
. %{_specdir}/fn-build.sh
LD_LIBRARY_PATH=%{etop_dest}/lib/%{epics_arch} \
	make %{?_smp_mflags} %{cmd_flags} \
	EPICS_HOST_ARCH=%{epics_arch} INSTALL_LOCATION=%{etop_dest} \
	DESTDIR=%{buildroot} install
rm %{etop_dest}/dbd/softIoc.dbd
cd %{etop_dest}/bin/%{epics_arch}
	rm S99caRepeater S99logServer caRepeater.service; cd -
mkdir -p %{buildroot}/etc/profile.d
sed 's,@etop_base@,%{etop_base},g; s,@epics_arch@,%{epics_arch},g' \
	< %{S:1} > %{buildroot}/etc/profile.d/epics-base.sh
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst
%config(noreplace) /etc/profile.d/epics-base.sh

