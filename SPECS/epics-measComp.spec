%define repo measComp
%define commit R4-3
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - USB and ethernet I/O modules from Measurement Computing
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc
BuildRequires:  epics-mca, epics-scaler, epics-seq, epics-sscan
BuildRequires:  gcc-c++, make, uldaq
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc
Requires:       epics-mca, epics-scaler, epics-seq, epics-sscan, uldaq

%{inherit synapps + global}
%description

%{inherit synapps}

