%define repo motorHytec
%define commit R1-0-2

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Hytec motion controllers

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}

BuildRequires:  epics-motor, epics-ipac, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'IPAC=$(SUPPORT)/ipac' > %{repo}/configure/RELEASE.local

