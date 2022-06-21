%define repo ip330
%define commit R2-10
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - Acromag IP330 16-channel 16-bit Industry Pack ADC
BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

