%define repo motorOms
%define commit 5219f8ce

Name:           epics-%{repo}
Version:        1_1_7
Release:        1.%{commit}
Summary:        EPICS - OMS motion controllers

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}

BuildRequires:  epics-motor, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor}

