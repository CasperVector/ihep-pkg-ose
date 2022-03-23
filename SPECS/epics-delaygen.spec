%define repo delaygen
%define commit R1-2-2

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Delay generators

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-asyn, epics-calc, epics-ip, epics-ipac, epics-StreamDevice
BuildRequires:  gcc-c++, make
Requires:       epics-asyn, epics-calc, epics-ip, epics-ipac, epics-StreamDevice

%description

%{inherit synapps}

