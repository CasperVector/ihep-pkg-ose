%define repo dxp
%define commit R6-0
%{meta name license=EPICS github=epics-modules version=commit,4}

Summary:        EPICS - DSP-based multi-channel analysers from XIA
BuildRequires:  epics-ADCore, epics-mca
BuildRequires:  gcc-c++, make, libXext-devel, libusb-devel
Requires:       epics-ADCore, epics-mca, libXext, libusb

%{inherit synapps + global}
%description

%{inherit synapps}

