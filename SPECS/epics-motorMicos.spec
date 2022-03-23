%define repo motorMicos
%define commit R2-0

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Micos motion controllers

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}

BuildRequires:  epics-motor, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor}

