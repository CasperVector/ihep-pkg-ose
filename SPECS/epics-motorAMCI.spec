%define repo motorAMCI
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,3}

Summary:        EPICS - AMCI motion controllers
BuildRequires:  epics-modbus
Requires:       epics-modbus

%{inherit motor + global deps}
%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'MODBUS=$(SUPPORT)/modbus' > "$(cat ioc.lst)"/configure/RELEASE.local

