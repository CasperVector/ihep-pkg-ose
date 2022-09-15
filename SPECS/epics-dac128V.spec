%define repo dac128V
%define commit R2-10-1
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Systran DAC128V 8-channel 12-bit Industry Pack DAC
BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

