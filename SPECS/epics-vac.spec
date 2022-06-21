%define repo vac
%define commit R1-9-1
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - Certain ion pump and vacuum gauge controllers
BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

