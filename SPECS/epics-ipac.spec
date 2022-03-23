%define repo ipac
%define commit 2.16

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - IPAC carrier boards and I/O modules

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-2.16-config.patch

BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

