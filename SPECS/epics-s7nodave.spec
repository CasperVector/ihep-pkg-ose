%define repo s7nodave
%define commit 3.0.2
%define cmd_flags CMD_FLAGS='%{optflags}' CMD_CXXFLAGS='%{optflags} --std=c++11'

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        2
Summary:        EPICS - Siemens S7 PLCs

License:        GPLv3+
URL:            https://oss.aquenos.com/epics/%{repo}/
Source0:        %{url}/download/%{repo}-%{commit}.tar.gz
Patch0:         %{name}-3.0.2-app-libs-files.patch

BuildRequires:  epics-autosave, epics-asyn, epics-iocStats
BuildRequires:  gcc-c++, make, boost-devel
Requires:       epics-autosave, epics-asyn, epics-iocStats, boost

%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
%_moreapps_prep
chmod 0755 iocBoot/iocNodave/st.cmd
cp %{epics_root}/utils/appMain.c s7nodaveApp/src/s7nodaveMain.cpp
%_iocboot_makefiles iocBoot; cd ..
_mv_build %{repo} %{epics_root}/%{repo}
cd %{epics_root}/%{repo}/iocBoot; make %{?_smp_mflags}

