%define repo calc
%define commit R3-7-4
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - [as]Calcout and transform records
Patch0:         %{name}-3_7_4-config.patch
BuildRequires:  epics-seq, gcc-c++, make
Requires:       epics-seq

%{inherit synapps + global}
%description

%{inherit synapps}

