%define repo modbus
%define commit R3-2
%{meta name license=MIT github=epics-modules version=commit,3}

Summary:        EPICS - PLCs and other devices using the Modbus protocol
Patch0:         %{name}-3_2-libs.patch
BuildRequires:  epics-asyn, epics-autosave, epics-iocStats, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-iocStats

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%{inherit synapps + prep}
mv iocBoot/iocTest iocBoot/iocModbus

