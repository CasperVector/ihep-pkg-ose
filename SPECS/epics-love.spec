%define repo love
%define commit R3-2-8
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Love controller support
BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

