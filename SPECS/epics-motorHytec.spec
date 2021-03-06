%define repo motorHytec
%define commit R1-0-2
%define cmd_flags CMD_FLAGS='%{optflags} -Wno-error=format-security' \
	CMD_CXXFLAGS='%{optflags} -Wno-error=format-security'
%{meta name license=EPICS github=epics-motor version=commit,1}

Summary:        EPICS - Hytec motion controllers
BuildRequires:  epics-ipac
Requires:       epics-ipac

%{inherit motor + deps}
%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'IPAC=$(SUPPORT)/ipac' > %{repo}/configure/RELEASE.local

