%define repo motorNewport
%define commit 070c93e1

Name:           epics-%{repo}
Version:        1_1_3
Release:        1.%{commit}
Summary:        EPICS - Newport motion controllers

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}

BuildRequires:  epics-motor, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor}

