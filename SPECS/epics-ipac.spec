%define repo ipac
%define commit 2.16
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - IPAC carrier boards and I/O modules
Patch0:         %{name}-2.16-config.patch
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps}

