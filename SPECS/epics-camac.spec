%define repo camac
%define commit R2-7-4
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - CAMAC controllers and modules
Patch0:         %{name}-2_7_4-config.patch
BuildRequires:  epics-calc, epics-motor, epics-scaler, gcc-c++, make
Requires:       epics-calc, epics-motor, epics-scaler

%description

%{inherit synapps}

