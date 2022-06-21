%define repo alive
%define commit R1-3-1
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - alive record and related software
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

