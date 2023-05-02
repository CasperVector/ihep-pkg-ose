%define repo motor
%define commit R7-2-2
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Core motor support
Patch0:         %{name}-7_2_2-config-libs.patch
Patch1:         %{name}-7_2_2-bugs.patch
BuildRequires:  epics-asyn, epics-busy, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-busy, epics-seq
Requires:       epics-autosave, epics-iocStats

%{inherit synapps + global}
%description

%{inherit synapps}

