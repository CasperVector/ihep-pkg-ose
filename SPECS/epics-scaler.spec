%define repo scaler
%define commit 4.0
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - scaler record and related software
BuildRequires:  epics-asyn, gcc-c++, make
Requires:       epics-asyn

%{inherit synapps + global}
%description

%{inherit synapps}

