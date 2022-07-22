%define repo mca
%define commit R7-9
%define cmd_flags CMD_FLAGS='%{optflags} -Wno-error=format-security' \
	CMD_CXXFLAGS='%{optflags} -Wno-error=format-security'
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - Multi-channel analysers and multi-channel scalers
Patch0:         %{name}-7_9-scaler.patch
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc, epics-scaler
BuildRequires:  epics-seq, epics-sscan, gcc-c++, make, libusbx-devel
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc, epics-scaler
Requires:       epics-seq, epics-sscan, libusbx

%description

%{inherit synapps}

