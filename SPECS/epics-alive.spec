%define repo alive
%define commit R1-3-1
%define cmd_flags CMD_FLAGS='%{optflags} -Wno-error=format-security' \
	CMD_CXXFLAGS='%{optflags} -Wno-error=format-security'
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - alive record and related software
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

