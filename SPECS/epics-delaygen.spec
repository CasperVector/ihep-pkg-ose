%define repo delaygen
%define commit R1-2-2
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Delay generators
BuildRequires:  epics-asyn, epics-calc, epics-ip, epics-ipac, epics-StreamDevice
BuildRequires:  gcc-c++, make
Requires:       epics-asyn, epics-calc, epics-ip, epics-ipac, epics-StreamDevice

%{inherit synapps + global}
%description

%{inherit synapps}

