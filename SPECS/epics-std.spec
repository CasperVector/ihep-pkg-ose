%define repo std
%define commit R3-6-3
%define opimask */arrayPlot.*
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - epid and throttle records
BuildRequires:  epics-asyn, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-seq

%{inherit synapps + global}
%description

%{inherit synapps}

