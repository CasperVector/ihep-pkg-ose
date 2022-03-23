%define repo busy
%define commit R1-7-3

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Signal operation completion with putNotify

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-1_7_3-config.patch

BuildRequires:  epics-asyn, gcc-c++, make
Requires:       epics-asyn

%description

%{inherit synapps}

