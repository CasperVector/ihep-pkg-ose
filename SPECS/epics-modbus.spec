%define repo modbus
%define commit R3-2

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - PLCs and other devices using the Modbus protocol

License:        MIT
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-3_2-libs.patch

BuildRequires:  epics-asyn, epics-autosave, epics-iocStats, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-iocStats

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
mv iocBoot/iocTest iocBoot/iocModbus

