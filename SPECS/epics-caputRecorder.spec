%define repo caputRecorder
%define commit R1-7-4
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Recording and playback of caputs sequences
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps}

