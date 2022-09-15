%define repo busy
%define commit R1-7-3
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Signal operation completion with putNotify
Patch0:         %{name}-1_7_3-config.patch
BuildRequires:  epics-asyn, gcc-c++, make
Requires:       epics-asyn

%description

%{inherit synapps}

