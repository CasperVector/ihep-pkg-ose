%define repo measComp
%define commit R3-0
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - USB and ethernet I/O modules from Measurement Computing
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc
BuildRequires:  epics-mca, epics-scaler, epics-seq, epics-sscan
BuildRequires:  gcc-c++, make, libusbx-devel, hidapi-devel
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc
Requires:       epics-mca, epics-scaler, epics-seq, epics-sscan, libusbx, hidapi

%{inherit synapps + global}
%description

%{inherit synapps}

