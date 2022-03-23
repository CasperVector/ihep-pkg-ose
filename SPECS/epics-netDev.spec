%define repo netDev
%define commit 1.1.0

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        2
Summary:        EPICS - Device and Driver Support for General Network Devices

License:        EPICS Open License
URL:            https://www-linac.kek.jp/cont/epics/netdev/
Source0:        %{github_archive shuei %{repo} %{commit}}
Patch0:         %{name}-1.1.0-epics7-app-libs-files.patch

BuildRequires:  epics-autosave, epics-iocStats, gcc-c++, make
Requires:       epics-autosave, epics-iocStats

%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
%_moreapps_prep
chmod 0755 iocBoot/iocNetDev/st.cmd
cp %{epics_root}/utils/appMain.c src/netDevMain.cpp
%_iocboot_makefiles iocBoot; cd ..
_mv_build %{repo} %{epics_root}/%{repo}
cd %{epics_root}/%{repo}/iocBoot; make %{?_smp_mflags}

