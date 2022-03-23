%define repo motorAMCI
%define commit R1-0-1

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - AMCI motion controllers

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}

BuildRequires:  epics-motor, epics-modbus, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'MODBUS=$(SUPPORT)/modbus' > "$(cat ioc.lst)"/configure/RELEASE.local

