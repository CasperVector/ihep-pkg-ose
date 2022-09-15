%define repo ipUnidig
%define commit R2-12
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Industry Pack digital I/O modules
BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

