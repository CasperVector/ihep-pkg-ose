%define repo lua
%define commit R3-0-2
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Lua scripting record
BuildRequires:  epics-asyn, gcc-c++, make
Requires:       epics-asyn

%{inherit synapps + global}
%description

%{inherit synapps}

