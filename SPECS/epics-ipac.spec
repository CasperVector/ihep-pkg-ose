%define repo ipac
%define commit 2.16
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - IPAC carrier boards and I/O modules
Patch0:         %{name}-2.16-config.patch
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

