%define repo motorMotorSim
%define commit R1-1

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Module for a simulated motor

License:        EPICS Open License
URL:            https://github.com/epics-motor/%{repo}
Source0:        %{github_archive epics-motor %{repo} %{commit}}
Patch0:         %{name}-1_1-config-bugs.patch

BuildRequires:  epics-motor, gcc-c++, make
Requires:       epics-motor

%description

%{inherit motor}

