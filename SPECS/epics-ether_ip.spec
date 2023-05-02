%define repo ether_ip
%define commit %{repo}-3-2
%{meta name license=EPICS github=EPICSTools}

Version:        %(echo %{commit} | sed 's/^%{repo}-//; s/-/_/g')
Release:        3.el%{rhel}
Summary:        EPICS - EtherIP support for Allen Bradley PLCs
Patch0:         %{name}-3_2-bugs.patch
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps}

