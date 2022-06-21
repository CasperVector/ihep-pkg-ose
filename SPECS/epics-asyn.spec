%define repo asyn
%define commit R4-42
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - Generic-purpose interfacing to lower level
Patch0:         %{name}-4_42-files.patch
BuildRequires:  epics-ipac, epics-seq, gcc-c++, make
Requires:       epics-ipac, epics-seq

%description

%{inherit synapps}

