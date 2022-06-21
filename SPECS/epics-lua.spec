%define repo lua
%define commit R3-0-2
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - Lua scripting record
BuildRequires:  epics-asyn, gcc-c++, make
Requires:       epics-asyn

%description

%{inherit synapps}

