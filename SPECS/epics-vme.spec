%define repo vme
%define commit R2-9-4
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Perform generic VME I/O
BuildRequires:  epics-asyn, epics-scaler, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-scaler, epics-seq

%{inherit synapps + global}
%description

%{inherit synapps}

