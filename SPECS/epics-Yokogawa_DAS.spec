%define repo Yokogawa_DAS
%define commit R2-0-1
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Yokogawa GM10 and MW100
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps}

