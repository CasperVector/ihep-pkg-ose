%define repo procServControl
%define commit v20221107
%{meta name license=Apache codeberg=CasperVector version=commit,2}

Summary:        EPICS - Control of running procServ instances
Patch0:         %{name}-20221107-libs.patch
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-iocStats
BuildRequires:  gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-busy, epics-iocStats

%{inherit synapps + global}
%description

%{inherit synapps}

