%define repo quadEM
%define commit R9-4
%{meta name license=EPICS github=epics-modules version=commit,4}

Summary:        EPICS - Quad electrometers and picoammeters
BuildRequires:  epics-ADCore, epics-ipac, epics-ipUnidig
BuildRequires:  gcc-c++, make, libXext-devel
Requires:       epics-ADCore, epics-ipac, epics-ipUnidig, libXext

%{inherit synapps + global}
%description

%{inherit synapps}

