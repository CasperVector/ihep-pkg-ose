%define repo ether_ip
%define commit %{repo}-3-2

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^%{repo}-//; s/-/_/g')
Release:        1
Summary:        EPICS - EtherIP support for Allen Bradley PLCs

License:        EPICS Open License
URL:            https://github.com/EPICSTools/%{repo}
Source0:        %{github_archive EPICSTools %{repo} %{commit}}
Patch0:         %{name}-3_2-bugs.patch

BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

